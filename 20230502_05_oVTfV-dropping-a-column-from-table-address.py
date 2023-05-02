"""
dropping a column from table address
"""

from yoyo import step

__depends__ = {'20230502_04_g1ASz-add-table-sales-order-hearder'}

steps = [
    step("ALTER TABLE address DROP COLUMN address_line2",
         "ALTER TABLE address ADD COLUMN address_line2")
]
