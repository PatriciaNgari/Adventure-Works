"""
add new table customer
"""

from yoyo import step

__depends__ = {'20230502_01_Fdhjr-add-new-table-called-address'}

steps = [
    step("CREATE TABLE customer(company_name VARCHAR(100), customer_id INTEGER, email_address VARCHAR(200), first_name VARCHAR(50), last_name VARCHAR(50), middle_name VARCHAR(50), modified_date TIMESTAMPTZ, name_style VARCHAR(100), password_hash VARCHAR(200), password_salt VARCHAR(200), phone VARCHAR(50), rowguid VARCHAR(100), sales_person VARCHAR(100), suffix VARCHAR(100), title VARCHAR(20) )",
         "DROP TABLE customer")
]
