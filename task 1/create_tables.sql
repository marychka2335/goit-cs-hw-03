CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
fullname VARCHAR(100),
email VARCHAR(100) UNIQUE);

CREATE TABLE IF NOT EXISTS status (
id SERIAL PRIMARY KEY,
name VARCHAR(50),
CONSTRAINT valid_status CHECK (name IN ('new', 'in progress', 'completed')));

CREATE TABLE IF NOT EXISTS tasks (
id SERIAL PRIMARY KEY,
title VARCHAR(100),
description TEXT,
user_id INTEGER,
status_id INTEGER,
CONSTRAINT fk_users FOREIGN KEY(user_id) 
REFERENCES users(id) ON DELETE CASCADE,
CONSTRAINT fk_status FOREIGN KEY(status_id) 
REFERENCES status(id));