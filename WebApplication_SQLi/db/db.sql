-- db.sql - VERSION WITH DEBUG

-- TABLE: users 
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users(username, password, email) VALUES
('admin', 'admin123', 'administrator123@gmail.com'),
('conmeo', 'conmeooOOohd', 'conmeo@yahoo.com'),
('alice', 'aliceinborderland', 'alicetwo@gmail.com'),
('bob', 'bobo7723', 'bob@student.hcmus.edu.vn');

-- TABLE: products
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price NUMERIC(10,2),
    image TEXT
);

INSERT INTO products (name, description, price, image) VALUES
('Chocolate Cookie', 'Bánh quy socola thơm ngon', 2.50, 'choco.jpg'),
('Vanilla Cake', 'Bánh bông lan vani mềm mại', 5.00, 'vanila.jpg'),
('Strawberry Tart', 'Bánh tart dâu tây tươi', 4.50, 'straw.jpg');

-- DEBUG: Thông báo thành công
DO $$ BEGIN
    RAISE NOTICE 'Tables created successfully';
END $$;

-- Cấp quyền cho user helios (CHẠY VỚI USER POSTGRES)
GRANT USAGE ON SCHEMA public TO helios;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO helios;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO helios;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO helios;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON SEQUENCES TO helios;

DO $$ BEGIN
    RAISE NOTICE 'Permissions granted to helios';
END $$;