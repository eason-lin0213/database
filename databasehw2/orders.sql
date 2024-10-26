SELECT * FROM dbhw2.orders;
-- 插入範例資料到 orders 表格
INSERT INTO orders (user_id, product_id, quantity, total_price, order_date) VALUES

(5, 5, 2, 499.50, NOW());    -- 使用者5訂購了2支智慧手錶