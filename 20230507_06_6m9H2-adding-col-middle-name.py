"""
adding col middle name
"""

from yoyo import step

__depends__ = {'20230507_05_huV82-dropping-col-middle-name'}

steps = [
    step("ALTER TABLE customer ADD COLUMN middle_name VARCHAR(50) NULL",
         "ALTER TABLE customer DROP COLUMN middle_name")
]
