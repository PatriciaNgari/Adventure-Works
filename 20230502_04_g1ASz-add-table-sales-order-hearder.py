"""
add table sales order hearder
"""

from yoyo import step

__depends__ = {'20230502_03_wP54R-add-table-customer-address'}

steps = [
    step("CREATE TABLE sales_order_header(account_number VARCHAR(50), bill_to_address_id INTEGER, comment VARCHAR(20) NULL, credit_card_approval_code INTEGER NULL, customer_id INTEGER, due_date TIMESTAMPTZ, modified_date TIMESTAMPTZ, online_order_flag BOOL, order_date TIMESTAMPTZ, purchase_order_number VARCHAR(50), revision_number INTEGER, rowguid VARCHAR(100), sales_order_id INTEGER, sales_order_number VARCHAR(50), ship_date TIMESTAMPTZ, ship_method VARCHAR(20), ship_to_address_id INTEGER, freight BIGINT, status INTEGER, sub_total BIGINT, tax_amt BIGINT, total_due BIGINT)",
         "DROP TABLE sales_order_header")
]
