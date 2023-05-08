"""
creating another table salesorder header
"""

from yoyo import step

__depends__ = {'20230506_02_Wr5U9-create-table-salesorderheader'}

steps = [
    step("CREATE TABLE sales_order_header (account_number VARCHAR(100), bill_to_address_id INTEGER, customer_id INTEGER, due_date TIMESTAMP WITHOUT TIME ZONE, modified_date TIMESTAMP WITHOUT TIME ZONE, online_order_flag BOOL, order_date TIMESTAMP WITHOUT TIME ZONE, purchase_order_number VARCHAR(200), revision_number INTEGER, rowguid VARCHAR(200), sales_order_id INTEGER, sales_order_number VARCHAR(100), ship_date TIMESTAMP WITHOUT TIME ZONE, ship_method VARCHAR(200), ship_to_address_id INTEGER, freight INTEGER, status INTEGER, sub_total INTEGER, tax_amt INTEGER, total_due INTEGER, id INTEGER)",
         "DROP TABLE sales_order_header")
]
