import pandas as pd
from sqlalchemy import create_engine

# database connection
user = "kenan"
password = "123"
host = "pgdatabase"
port = "5432"
database = "ecommerce"

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

print("Database connection successful")

# CSV oku
df = pd.read_csv("OnlineRetail.csv", encoding="latin1")

# ----- DATA CLEANING -----

# null customer sil
df = df.dropna(subset=["CustomerID"])

# return işlemleri sil
df = df[df["Quantity"] > 0]

# duplicate sil
df = df.drop_duplicates()

# datatype düzelt
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype(int)

# ----- LOAD TO POSTGRES -----

df.to_sql(
    name="online_retail",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded to PostgreSQL")