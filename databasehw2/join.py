from flask import Flask, Blueprint, render_template, request, redirect, url_for
import mysql.connector

# 定义 Blueprint
join_bp = Blueprint('join_bp', __name__)

db_config = {
    'user': 'root',
    'password': '86637711',
    'host': 'localhost',
    'database': 'dbhw2'
}

# 路由: 查询用户与订单
@join_bp.route('/join')
def join_query():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # 执行查询
    query = """
    SELECT orders.id AS order_id, users.name AS user_name, product.name AS product_name, 
           orders.Quantity, orders.Total_price
    FROM orders
    JOIN users ON orders.User_id = users.id
    JOIN product ON orders.Product_id = product.id
    ORDER BY orders.id;
    """
    cursor.execute(query)
    results = cursor.fetchall()  # 获取所有结果

    cursor.close()
    conn.close()

    return render_template('index.html', orders=results)

# 路由: 更新订单
@join_bp.route('/join', methods=['POST'])
def update_order():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    order_id = request.form['order_id']
    quantity = request.form['quantity']
    total_price = request.form['total_price']

    # 更新 SQL 语句
    update_query = """
    UPDATE orders
    SET Quantity = %s, Total_price = %s
    WHERE id = %s
    """
    cursor.execute(update_query, (quantity, total_price, order_id))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('join_bp.join_query'))  # 更新后重定向回查询页面

# 路由: 查询产品
@join_bp.route('/product')
def product_query():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    query_product = """
    SELECT id, name, description, price FROM product;
    """

    cursor.execute(query_product)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', products=results)

# 主应用
app = Flask(__name__)
app.register_blueprint(join_bp)

if __name__ == '__main__':
    app.run(debug=True)
