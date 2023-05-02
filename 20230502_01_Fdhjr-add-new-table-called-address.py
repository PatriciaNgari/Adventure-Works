"""
add new table called address 
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE address(address_id INTEGER, address_line1 INTEGER NULL, address_line2 VARCHAR(200) NULL, city VARCHAR(200), country_region VARCHAR(200), modified_date TIMESTAMPTZ, postal_code VARCHAR(200), rowguid VARCHAR(200), state_province VARCHAR(200) )",
         "DROP TABLE address"
         )
]
