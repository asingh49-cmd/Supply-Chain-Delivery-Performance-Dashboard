import pandas as pd
import numpy as np

#Load dataset
data = pd.read_csv('data/raw/DataCoSupplyChainDataset.csv', encoding='latin1',low_memory=False)

# Display initial data info
print("Inital Data Info:")
print(data.info())
print("\n")

# Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)
print("\n")

print("Data Cleaning...")

#Clean column names by stripping whitespace
data.columns = data.columns.str.strip().str.lower().str.replace(" ","_").str.replace("(","").str.replace(")","")

#Convert date columns to datetime format
date_columns = ['order_date_dateorders','shipping_date_dateorders']
for col in date_columns:
    data[col] = pd.to_datetime(data[col],errors='raise')

#Drop product description and order zipcode column due to high missing values
data = data.drop(columns=['product_description'])
data = data.drop(columns=['order_zipcode'])

# Fill missing values for numerical columns with median
numerical_cols = data.select_dtypes(include=[np.number]).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median)

# Fill missing values for categorical columns with mode
categorical_cols = data.select_dtypes(include=['object']).columns
data[categorical_cols] = data[categorical_cols].fillna('Unknown', inplace=True)

print("Data cleaning completed")

#Feature engineering
print("Feature Engineering...")

data['order_year'] = data['order_date_dateorders'].dt.year
data['order_month'] = data['order_date_dateorders'].dt.month
data['order_quarter'] = data['order_date_dateorders'].dt.quarter
data['order_day'] = data['order_date_dateorders'].dt.day_name()
data['on_time_delivery'] = np.where(data['days_for_shipping_real'] <= data['days_for_shipment_scheduled'], 1, 0)
data['delay_days'] = data['days_for_shipping_real'] - data['days_for_shipment_scheduled'].clip(lower=0)
data['is_weekend'] = data['order_day'].isin([5,6]).astype(int)
data['is_bulk_order'] = data['order_item_quantity'] >= data['order_item_quantity'].quantile(0.75).astype(int)
data['is_international'] = np.where(data['order_country'] != data['customer_country'], 1, 0)

#Market Volume (orders per market) feature
market_volume = data.groupby('market').size()
data['market_volume'] = data['market'].map(market_volume)
#Country Volume (orders per country) feature
country_volume = data.groupby('order_country').size()
data['country_volume'] = data['order_country'].map(country_volume)

print("Feature engineering completed")
#Save cleaned data
print("Saving cleaned data...")
data.to_csv('data/processed/cleaned_dataco_supply_chain_dataset.csv',index=False)
print(f"Cleaned data saved with shape: {len(data)} rows and {len(data.columns)} columns") #180519 rows and 62 columns
