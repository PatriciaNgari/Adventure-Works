"""
create table salesorderheader
"""

from yoyo import step

__depends__ = {'20230506_01_5Hw8T-create-table-address'}

steps = [
    step("CREATE TABLE sales_order_header (account_number VARCHAR(100), bill_to_address_id INTEGER, customer_id TIMESTAMP WITHOUT TIME ZONE,due_date BOOL,modified_date TIMESTAMP WITHOUT TIME ZONE,online_order_flag VARCHAR(100),order_date INTEGER,purchase_order_number VARCHAR(200),revision_number INTEGER, rowguid VARCHAR(100), sales_order_id TIMESTAMP WITHOUT TIME ZONE, sales_order_number VARCHAR(100), ship_date TIMESTAMP WITHOUT TIME ZONE,ship_method VARCHAR(200),ship_to_address_id INTEGER,freight INTEGER,status INTEGER,sub_total INTEGER,tax_amt INTEGER,total_due INTEGER,id INTEGER)",
         "DROP TABLE sales_order_header")
]
