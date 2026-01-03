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
    'order_year',
    'order_quarter',
    'is_weekend',
    'is_bulk_order',
    'sales',
    'order_profit_per_order',
    'order_item_discount'
]
categorical_features = [
    'market',
    'category_name',
    'type',
    'order_country'
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
def evaluate_model(y_true, y_pred, y_prob, model_name):
    print(f"Evaluation Metrics for {model_name}:")
    print(classification_report(y_true, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"Recall: {recall_score(y_true, y_pred):.4f}")
    print(f"F1 Score: {f1_score(y_true, y_pred):.4f}")
    print(f"ROC AUC Score: {roc_auc_score(y_true, y_prob):.4f}")
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    plt.figure()
    plt.plot(fpr, tpr, label=f'{model_name} (area = {roc_auc_score(y_true, y_prob):.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve - {model_name}')
    plt.legend(loc='lower right')
    plt.show()

evaluate_model(y_test, y_pred_logreg, y_prob_logreg, "Logistic Regression")
evaluate_model(y_test, y_pred_rf, y_prob_rf, "Random Forest")

#Plot Feature Importances
def plot_feature_importance(feature_importance_df, model_name, importance_col):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importance_col, y='feature', data=feature_importance_df.head(10))
    plt.title(f'Top 10 Feature Importances - {model_name}')
    plt.xlabel(importance_col)
    plt.ylabel('Feature')
    plt.show()

plot_feature_importance(feature_importance_lr, "Logistic Regression", 'abs_coefficient')
plot_feature_importance(feature_importance_rf, "Random Forest", 'importance')
print('Using Random Forest predictions as metrics are generally better')
#Save predictions to CSV
predictions_df = X_test.copy()
predictions_df['actual_late_delivery_risk'] = y_test
predictions_df['predicted_late_delivery_risk'] = y_pred_rf
predictions_df['risk_probability'] = y_prob_rf
predictions_df.to_csv('data/processed/model_predictions.csv', index=False)
print("Model predictions saved to 'data/processed/model_predictions.csv' using Random Forest Predictions")