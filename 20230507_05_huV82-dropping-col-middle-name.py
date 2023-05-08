"""
dropping col middle name
"""

from yoyo import step

__depends__ = {'20230507_04_TALHt-adding-null-for-col-lastname'}

steps = [
    step("ALTER TABLE customer DROP COLUMN middle_name",
         "ALTER TABLE customer ADD COLUMN middle_name VARCHAR(50)")
]
