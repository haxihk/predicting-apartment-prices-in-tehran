# predicting-apartment-prices-in-tehran
predicting the price of any apartment in the city of tehran with real world data from divar.ir with the help of advance ML models and algorithms

# 🏠 Real Estate Price Prediction on Divar Data

A professional machine learning project for predicting real estate prices using property listings data from **Divar** (an Iranian classifieds platform). The project covers all major steps in a data science workflow including data preprocessing, feature engineering, modeling, tuning, interpretation, and evaluation.

---

## 📌 Table of Contents

1. [Introduction](#1-introduction)  
2. [Data Preparation](#2-data-preparation)  
3. [Model Development](#3-model-development)  
4. [Final Model and Testing](#4-final-model-and-testing)  
5. [Model Interpretation](#5-model-interpretation-and-analysis)  
6. [Model Saving & Reproducibility](#6-model-saving-and-reproducibility)  
7. [Key Achievements](#7-key-achievements-and-best-practices)  
8. [Conclusion](#8-conclusion)  
9. [Future Work](#9-recommendations-for-future-work)  

---

## 1. 📘 Introduction

This project aims to build a robust machine learning pipeline to predict property prices using data collected from **Divar**. The pipeline includes:

- Data cleaning and transformation  
- Feature engineering  
- Outlier removal  
- Regression modeling  
- Hyperparameter tuning  
- Model interpretation using SHAP  
- Final evaluation and deployment preparation  

---

## 2. 🧹 Data Preparation

### 2.1 Data Cleaning
- Raw data was loaded from an Excel file.
- Nulls and duplicates were identified and removed.
- Binary categorical columns (elevator, parking, warehouse) were mapped to `0/1`.
- Price was converted to Toman; `price_per_sqm` calculated.
- Neighborhoods were label encoded.

### 2.2 Feature Engineering
Created new features:
- `area_x_rooms`: Product of area and number of rooms
- `elevator_high_floor`: Indicates whether a high-floor property has an elevator
- `building_age`: Calculated from construction year
- `area_level`: Quantile-based price category (Low/Medium/Luxury)
- `area_bin`: Binned area ranges

All categorical features were encoded numerically.

### 2.3 Outlier Removal
- Outliers in `price_per_sqm` removed using IQR method.

### 2.4 Target Transformation
- Applied `log1p(price)` to normalize the target.

### 2.5 Dataset Splitting
- Train: 64%, Validation: 16%, Test: 20%
- Saved to separate Excel files for reproducibility.

---

## 3. 🤖 Model Development

### 3.1 Models Tested
- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- XGBoost  
- LightGBM  
- MLPRegressor (Neural Network)

### 3.2 Evaluation Metrics
- RMSE (Root Mean Squared Error)  
- R² Score

Random Forest consistently outperformed others in validation.

### 3.3 Hyperparameter Tuning
Used **GridSearchCV** to tune:
- `n_estimators`
- `max_depth`
- `min_samples_split`

---

## 4. 🧪 Final Model and Testing

- Final model = **Random Forest** with best hyperparameters.
- Trained on combined training + validation sets.
- Predictions on test set were inverse-transformed using `np.expm1(log_price)`.
- Final test performance showed strong accuracy and generalization.

---

## 5. 🔍 Model Interpretation and Analysis

### 5.1 Residual Analysis
- Residuals were symmetrically distributed around zero.

### 5.2 Feature Importance
- Top contributors: `price_per_sqm`, `area`, `area_x_rooms`

### 5.3 SHAP (SHapley Additive Explanations)
- Global and local interpretation with SHAP values.
- SHAP summary plots showed the contribution of each feature.

---

## 6. 💾 Model Saving and Reproducibility

- Final model saved with `joblib`.
- All data splits and intermediate files are stored and documented.

---

## 7. ✅ Key Achievements and Best Practices

- **Comprehensive Cleaning**: Nulls, duplicates, and outliers handled
- **Strong Feature Engineering**: Enhanced prediction power
- **Proper Target Transformation**: Handled skewness
- **Evaluation**: RMSE, R², residuals
- **Interpretability**: SHAP used for trust and transparency
- **Reproducibility**: All steps saved for replication

---

## 8. 🧾 Conclusion

This project showcases a complete ML pipeline for real estate price prediction. Through rigorous preprocessing, feature design, modeling, and interpretability, the final model achieves solid performance and generalization. The code is modular and ready for extension or deployment.

---

## 9. 🚀 Recommendations for Future Work

- Add geo-location or map-based features
- Use external economic indicators
- Train more advanced deep learning models
- Create a web-based app for prediction
- Update the model continuously with new listings

---

📁 **Repository Includes**:
- Cleaned dataset and splits  
- All notebooks and Python scripts  
- Final trained model  
- Visualizations and SHAP analysis  
- README documentation

---

