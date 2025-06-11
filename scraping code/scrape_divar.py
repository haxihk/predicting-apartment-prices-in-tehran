from playwright.sync_api import sync_playwright
import csv
import time

TOKENS_FILE = "tokens.txt"
OUTPUT_CSV = "divar_real_estate.csv"
BASE_URL = "https://divar.ir/v/{token}"

def safe_int(value):
    
    try:
        return int(value.strip())
    except (ValueError, AttributeError):
        return -1

def fetch_ad_data(token, page):
    url = BASE_URL.format(token=token.strip())
     
    page.goto(url, timeout=60000, wait_until="domcontentloaded")
    time.sleep(5)  
    
    address_element = page.locator(".kt-page-title__subtitle--responsive-sized").first
    if address_element.is_visible():
        full_address = address_element.text_content().strip()
        address_parts = full_address.split("، ")  
        address = address_parts[-1] if len(address_parts) > 1 else full_address  
    else:
        address = "نامشخص"


    
    price_elements = page.locator(".kt-unexpandable-row__value").all()
    full_price = price_elements[1].text_content().replace("تومان", "").replace("٬", "").strip() if len(price_elements) > 3 else \
                 price_elements[0].text_content().replace("تومان", "").replace("٬", "").strip() if len(price_elements) > 2 else "نا مشخص"
    price = safe_int(full_price)
    
    
    floor_elements = page.locator(".kt-unexpandable-row__value").all()
    floor_text = floor_elements[3].text_content().strip() if len(floor_elements) > 3 else \
                 floor_elements[2].text_content().strip() if len(floor_elements) > 2 else "نامشخص"

    if "همکف" in floor_text:
        floor = 0
    elif "زیرهمکف" in floor_text:
        floor = -1
    else:
        floor = safe_int(floor_text.split(" ")[0])

    
    details = page.locator(".kt-group-row-item__value").all()
    area = safe_int(details[0].text_content()) if len(details) > 0 else -1
    year_built = safe_int(details[1].text_content()) if len(details) > 1 else -1
    rooms = safe_int(details[2].text_content()) if len(details) > 2 else -1

    
    features = [f.text_content().strip() for f in page.locator(".kt-body--stable").all()]
    elevator = "ندارد" if any("آسانسور ندارد"in f for f in features) else "دارد"
    parking = "ندارد" if any("پارگینگ ندارد" in f for f in features) else "دارد"
    warehouse = "ندارد" if any("انباری ندارد" in f for f in features) else "دارد"

    return {
        "token": token.strip(),
        "address": address,
        "price": price,
        "floor": floor,
        "area": area,
        "year_built": year_built,
        "rooms": rooms,
        "elevator": elevator,
        "parking": parking,
        "warehouse": warehouse
    }

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) 
    page = browser.new_page()

    with open(TOKENS_FILE, "r", encoding="utf-8") as file:
        tokens = file.readlines()

    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as csvfile: 
        fieldnames = ["token", "address", "price", "floor", "area", "year_built", "rooms", "elevator", "parking", "warehouse"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for token in tokens:
            ad_data = fetch_ad_data(token.strip(), page)
            writer.writerow(ad_data)
            print(f"✅ آگهی {token.strip()} پردازش شد.")
            time.sleep(3)

    browser.close()

print(f"\n✅ done,save in a csv file: {OUTPUT_CSV}")

