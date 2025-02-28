import pandas as pd
import pymysql
from sqlalchemy import create_engine
from urllib.parse import quote_plus

#details to connect to database
host = '127.0.0.1'
user = Your Username
password = Your Password
Database = Your database Name


# URL-encode the password
encoded_password = quote_plus(password)

#data
agro_data_df = pd.read_csv("agro_data.csv")

#connecting to Mysql

connection = pymysql.connect(host=host, user=user, password=password)
cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Database}")
cursor.execute(f"use {Database}")
connection.commit()
# Connect to MySQL server using sqlalchemy create_engine with help of pymysql
connection_url = f"mysql+pymysql://{user}:{encoded_password}@{host}/{Database}"

engine = create_engine(connection_url)

engine_connection = engine.connect()

# Insert order DataFrame into SQL, creating table if it doesn't exist
agro_data_df.to_sql('agrodata', con=engine_connection, if_exists='replace', index=False)

print("table_formed")
cursor.close()
connection.close()
