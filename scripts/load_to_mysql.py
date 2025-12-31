import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql

#DB Connection details
db_config = {
    'user': 'root',#Add your MySQL username here
    'password': '', #Add your MySQL password here
    'host': 'localhost',#Add your MySQL host here
    'database': 'supply_chain_db'#Add your MySQL database name here
}

def load_data_to_mysql(file_path):
    #Create database connection
    engine = create_engine(f'mysql+pymysql://',connect_args=db_config)

    #Load cleaned data
    data = pd.read_csv(file_path)

    #Load data to MySQL
    data.to_sql(name='orders',con=engine,if_exists='replace',index=False,chunksize=1000,method='multi')
    #Chunksize and method used for efficient loading (1000 rows at a time)
    print("Data loaded to MySQL database successfully.")

#Test queries to verify data load
def test_queries():
    engine = create_engine(f'mysql+pymysql://',connect_args=db_config)
    with engine.connect() as connection:
        test_query = pd.read_sql("SELECT COUNT(*) AS total_orders FROM orders",connection)
        print(test_query)
        test_query2 = pd.read_sql("SELECT ROUND(AVG(delay_days),2) AS avg_delay_days FROM orders",connection)
        print(test_query2)

#Main function
def main():
    file_path = 'data/processed/cleaned_dataco_supply_chain_dataset.csv'
    load_data_to_mysql(file_path)
    test_queries()
    
if __name__ == "__main__":
    main()