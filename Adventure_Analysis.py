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
    database="Adventure_Works"
)


dbEngine= sa.create_engine(
    url=constring,

)

try:
    with  psycopg2.connect("dbname=Adventure_Works user=postgres") as cur:
        conn = cur.cursor()
        f = open(r'C:\Users\User\Downloads\address.csv')
        
        conn.copy_from(f, 'address', sep=",",
                       columns=[
                          "address_id",
                          "address_line2",
                          "city",
                          "country_region",
                          "modified_date",
                          "postal_code",
                          "rowguid",
                          "state_province",
                          "id"
                       ])
        cur.commit() 
        
        
    print("Engine valid")
except Exception as e:
    print(f"Engine invalid: {e}")       