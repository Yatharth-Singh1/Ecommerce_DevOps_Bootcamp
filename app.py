from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Product catalog
products = [
    {
        'id': 1,
        'name': 'Product 1',
        'price': 10.99
    },
    {
        'id': 2,
        'name': 'Product 2',
        'price': 19.99
    },
    {
        'id': 3,
        'name': 'Product 3',
        'price': 5.99
    }
]

# Shopping cart
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    # Perform checkout logic here
    return render_template('checkout.html', cart=cart)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    else:
        return render_template('404.html'), 404

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    orders = []  # Retrieve user's order history
    addresses = []  # Retrieve user's saved addresses
    return render_template('profile.html', orders=orders, addresses=addresses)

@app.route('/order_confirmation')
def order_confirmation():
    order = {}  # Retrieve the order details
    return render_template('order_confirmation.html', order=order)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')