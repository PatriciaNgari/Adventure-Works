"""
editing data type for table customer
"""

from yoyo import step

__depends__ = {'20230507_02_6Itq2-creating-table-customer'}

steps = [
    step("ALTER TABLE customer ALTER COLUMN password_hash TYPE VARCHAR(200)",
         "ALTER TABLE customer ALTER COLUMN password_hash TYPE BOOL")
]
