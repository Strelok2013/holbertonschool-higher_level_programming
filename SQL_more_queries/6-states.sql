-- Creates a database called hbtn_0d_usa
-- Followed by adding in a table called states
-- Which has columns id and name
-- id is unique, a primary key and auto-increments
-- name cannot be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (`id` INT UNIQUE AUTO_INCREMENT, `name` VARCHAR(256) NOT NULL, PRIMARY KEY(id));
