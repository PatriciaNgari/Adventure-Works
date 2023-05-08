"""
creating table customer
"""

from yoyo import step

__depends__ = {'20230507_01_iRLHn-creating-another-table-salesorder-header'}

steps = [
    step("CREATE TABLE customer(company_name VARCHAR(100), customer_id INTEGER, email_address VARCHAR(200), first_name VARCHAR(50), last_name VARCHAR(50), middle_name VARCHAR(50), modified_date TIMESTAMP WITHOUT TIME ZONE, name_style BOOL, password_hash BOOL, password_salt VARCHAR(200), phone VARCHAR(200), rowguid VARCHAR(200), sales_person_suffix VARCHAR(200), title VARCHAR(50), id INTEGER)")
]
