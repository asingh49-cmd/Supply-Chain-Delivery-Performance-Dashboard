import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    precision_score,
    recall_score,
    f1_score,
    accuracy_score,
    roc_auc_score,
    roc_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/processed/cleaned_dataco_supply_chain_dataset.csv')
print(f'Loaded {len(df)} records for modeling')
print(f'Loaded {len(df.columns)} columns for modeling')

#Feature Selection
numeric_features = [
    'order_item_quantity',
    'on_time_delivery',
    'delay_days',
    'order_year',
    'order_quarter',
    'is_weekend',
    'is_bulk_order'
    'sales',
    'order_profit_per_order'
]
categorical_features = [
    'market',
    'category_name',
    'delivery_status',
    'type'
]
target_variable = 'late_delivery_risk'

all_features = numeric_features + categorical_features

#Modeling Dataset
model_df = df[all_features + [target_variable]].copy()

#Encode categorical variables
for col in categorical_features:
    le = LabelEncoder()
    model_df[col] = le.fit_transform(model_df[col].astype(str))
    print(f'Encoded {col} with {len(le.classes_)} classes')

#Prepare training and testing datasets
X = model_df[all_features]
y = model_df[target_variable]
#Training split (80%) and Testing split (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f'Training set: {len(X_train)} records')
print(f'Testing set: {len(X_test)} records')

#Feature Scaling for logistic regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#Logistic Regression Model
log_reg = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced') #handles imbalances
#Training the model
log_reg.fit(X_train_scaled, y_train)
# Predictions
y_pred_logreg = log_reg.predict(X_test_scaled)
y_prob_logreg = log_reg.predict_proba(X_test_scaled)[:, 1]

# Feature importance (coefficients)
feature_importance_lr = pd.DataFrame({
    'feature': X.columns,
    'coefficient': log_reg.coef_[0],
    'abs_coefficient': np.abs(log_reg.coef_[0])
}).sort_values('abs_coefficient', ascending=False)

#Random Forest Classifier Model
rf_model = RandomForestClassifier(n_estimators=100,max_depth=10,min_samples_split=10,random_state=42, class_weight='balanced')
#Training the model
rf_model.fit(X_train, y_train)
# Predictions
y_pred_rf = rf_model.predict(X_test)
y_prob_rf = rf_model.predict_proba(X_test)[:, 1]

# Feature importance
feature_importance_rf = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

#Model Evaluation/Comparison