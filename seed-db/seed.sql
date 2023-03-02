-- postgresql
-- Create table users (name, email, password, created_at, updated_at) and seed it with 10 users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

INSERT INTO
  users (username, password, created_at, updated_at)
VALUES
  ('email1@mail.com', 'password1', NOW(), NOW()),
  ('email2@mail.com', 'password2', NOW(), NOW()),
  ('email3@mail.com', 'password3', NOW(), NOW()),
  ('email4@mail.com', 'password4', NOW(), NOW()),
  ('email5@mail.com', 'password5', NOW(), NOW()),
  ('email6@mail.com', 'password6', NOW(), NOW()),
  ('email7@mail.com', 'password7', NOW(), NOW()),
  ('email8@mail.com', 'password8', NOW(), NOW()),
  ('email9@mail.com', 'password9', NOW(), NOW()),
  ('email10@mail.com', 'password10', NOW(), NOW());