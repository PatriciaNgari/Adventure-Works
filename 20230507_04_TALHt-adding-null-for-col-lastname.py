"""
adding null for col lastname
"""

from yoyo import step

__depends__ = {'20230507_03_RieKV-editing-data-type-for-table-customer'}

steps = [
    step("ALTER TABLE customer ALTER COLUMN middle_name TYPE VARCHAR NULL",
         "ALTER TABLE customer ALTER COLUMN middle_name TYPE VARCHAR")
]
