-- Creates a table that has only allows unique ids, and has a default of 1
CREATE TABLE IF NOT EXISTS unique_id (`id` INT UNIQUE DEFAULT 1, `name` VARCHAR(256));
