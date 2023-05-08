"""
create table address
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE address (address_id INTEGER, addressline1 VARCHAR(200), addressline2 VARCHAR(200) NULL, city VARCHAR(100), country_region VARCHAR(100), modified_date TIMESTAMP WITHOUT TIME ZONE,postal_code VARCHAR(100), rowguid VARCHAR(200), state_province VARCHAR(100), id INTEGER)",
         "DROP TABLE address")
]
