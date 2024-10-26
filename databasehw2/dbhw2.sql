SELECT orders.id, users.name AS user_name, product.name AS product_name, orders.quantity, orders.total_price, orders.order_date
FROM orders
JOIN users ON orders.user_id = users.id
JOIN product ON orders.product_id = product.id;
