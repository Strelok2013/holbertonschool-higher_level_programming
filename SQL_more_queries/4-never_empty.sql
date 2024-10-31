-- Creates a table that always must have an ID in each
-- Entry and also defaults new entries' values to 1 if not specified
CREATE TABLE IF NOT EXISTS `id_not_null` (`id` INT NOT NULL DEFAULT 1, `name` VARCHAR(256));
