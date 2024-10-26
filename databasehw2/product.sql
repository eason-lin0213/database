SELECT * FROM dbhw2.product;
-- 插入範例資料到 product 表格
INSERT INTO product (name, description, price, create_at) VALUES
('Laptop', 'A high-performance laptop suitable for all tasks', 1500.00, NOW()),
('Smartphone', 'Latest model smartphone with a powerful camera', 899.99, NOW()),
('Headphones', 'Noise-cancelling headphones for immersive sound', 199.99, NOW()),
('Tablet', 'Portable tablet with 10-inch display', 499.50, NOW()),
('Smartwatch', 'Smartwatch with health tracking features', 249.75, NOW());
