# app.py

from flask import Flask, render_template, request, flash, redirect, url_for
from bot import BasicBot
from config import API_KEY, API_SECRET
from logger_config import logger

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_change_it' # Necessary for flashing messages

# Initialize the bot once
bot = None
try:
    if API_KEY != "YOUR_API_KEY" and API_SECRET != "YOUR_API_SECRET":
        bot = BasicBot(api_key=API_KEY, api_secret=API_SECRET)
        logger.info("Bot initialized successfully for the web UI.")
    else:
        logger.error("API keys are placeholders. The bot will not function.")
except Exception as e:
    logger.critical(f"Failed to initialize bot: {e}")


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the main page and handles form submission for placing orders.
    """
    # Check if the bot was initialized
    if not bot:
        flash("Bot could not be initialized. Please check your API keys in config.py and restart the server.", "danger")
        return render_template('index.html')

    if request.method == 'POST':
        # --- Extract form data ---
        order_type = request.form.get('order_type')
        symbol = request.form.get('symbol').upper()
        side = request.form.get('side').upper()
        quantity = request.form.get('quantity')

        # --- Validate inputs ---
        if not all([order_type, symbol, side, quantity]):
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for('index'))

        try:
            quantity = float(quantity)
            if quantity <= 0:
                raise ValueError()
        except ValueError:
            flash("Quantity must be a positive number.", "danger")
            return redirect(url_for('index'))

        # --- Place order based on type ---
        response = None
        if order_type == 'market':
            response = bot.place_market_order(symbol, side, quantity)
        
        elif order_type == 'limit':
            price = request.form.get('price')
            try:
                price = float(price)
                if price <= 0: raise ValueError()
                response = bot.place_limit_order(symbol, side, quantity, price)
            except (ValueError, TypeError):
                flash("A valid positive price is required for a limit order.", "danger")
                return redirect(url_for('index'))

        elif order_type == 'stop_limit':
            price = request.form.get('price')
            stop_price = request.form.get('stop_price')
            try:
                price = float(price)
                stop_price = float(stop_price)
                if price <= 0 or stop_price <= 0: raise ValueError()
                response = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
            except (ValueError, TypeError):
                flash("Valid positive values for price and stop price are required.", "danger")
                return redirect(url_for('index'))

        # --- Flash response to the user ---
        if response and 'error' in response:
            flash(f"Order Failed: {response['error']}", "danger")
        elif response:
            flash(f"Order Successfully Placed! Order ID: {response.get('orderId')}, Status: {response.get('status')}", "success")
        else:
            flash("An unknown error occurred.", "danger")

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    # Use debug=True for development, but turn it off for production
    app.run(debug=True)
