"""
creating table customeraddress
"""

from yoyo import step

__depends__ = {'20230507_06_6m9H2-adding-col-middle-name'}

steps = [
    step("CREATE TABLE customer_address (address_id INTEGER, address_type VARCHAR(50), customer_id INTEGER, modified_date TIMESTAMP WITHOUT TIME ZONE, rowguid VARCHAR(200), id INTEGER)",
         "DROP TABLE customer_address")
]
