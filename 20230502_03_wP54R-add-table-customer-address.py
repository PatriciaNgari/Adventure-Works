"""
add table customer address
"""

from yoyo import step

__depends__ = {'20230502_02_VWpCc-add-new-table-customer'}

steps = [
    step("CREATE TABLE customer_address(address_id INTEGER, address_type VARCHAR(100), customer_id INTEGER, modified_date TIMESTAMPTZ, rowguid VARCHAR(100) )",
         "DROP TABLE customer_address ")
]
