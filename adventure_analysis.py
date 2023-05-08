import sqlalchemy as sa
import psycopg2
from io import open
import pandas as pd
import csv


     
constring: sa.engine.url.URL = sa.engine.URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    database="adventure_works"
)


dbEngine= sa.create_engine(
    url=constring,

)

try:
    with  psycopg2.connect("dbname=adventure_works user=postgres") as cur:
        conn = cur.cursor()
        f = open(r'C:\Users\User\Downloads\customeraddress.csv')
        
        conn.copy_from(f, 'customer_address', sep=",", null=" ")
        cur.commit() 
        
        
    print("Engine valid")
except Exception as e:
    print(f"Engine invalid: {e}")       