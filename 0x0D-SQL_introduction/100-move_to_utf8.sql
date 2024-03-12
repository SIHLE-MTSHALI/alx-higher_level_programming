-- Select the database hbtn_0c_0
USE hbtn_0c_0;

-- Convert table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert field to UTF8 (this step is actually redundant since the table conversion above will also convert all fields)
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

