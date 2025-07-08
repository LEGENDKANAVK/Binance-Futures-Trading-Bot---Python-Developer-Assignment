Simplified Binance Futures Trading Bot
This project is a comprehensive solution for the Junior Python Developer application task. It features a robust command-line trading bot that connects to the Binance Futures Testnet to place market, limit, and stop-limit orders. The project also includes a lightweight web interface built with Flask as a user-friendly alternative to the CLI.
The bot is built with a focus on reusability, clear input/output, and robust error handling, and it successfully implements all required and bonus features.

Features
Multiple Order Types: Place market, limit, and stop-limit orders.

Dual Interfaces:

Command-Line Interface (CLI): An easy-to-use CLI for placing orders with validated inputs and formatted table outputs.

Web UI (Bonus): A lightweight frontend built with Flask that allows users to place orders through a simple form in their web browser.

Binance Futures Testnet: All interactions are safely executed on the Binance Futures Testnet, ensuring no real funds are at risk.

Comprehensive Logging: Logs all API requests, responses, and errors to trading_bot.log for easy debugging and review.

Error Handling: Gracefully handles API errors, request issues, network timeouts, and invalid user inputs.

Structured Code: The project is organized into logical modules for configuration, core bot logic, CLI, and the web application.

Project Structure
trading_bot/
├── main.py             # Main entry point for the CLI application
├── app.py              # The Flask web server for the UI
├── bot.py              # Contains the core BasicBot class for API interaction
├── cli.py              # Defines the CLI and output formatting
├── config.py           # Stores API keys and configuration variables
├── logger_config.py    # Configures the application's logger
├── requirements.txt    # Lists all project dependencies
└── templates/
    └── index.html      # The HTML template for the web interface

Setup and Installation
1. Prerequisites
Python 3.8 or higher

A Binance Futures Testnet account

2. Clone the Repository
git clone <your-github-repository-url>
cd trading_bot

3. Install Dependencies
Install the necessary Python libraries using the requirements.txt file.

pip install -r requirements.txt

Configuration
Before running the bot, you must add your Binance Futures Testnet API credentials.

Get API Credentials:

Log in to your Binance Futures Testnet account.

Navigate to the API Key tab below the main chart.

Generate your API Key and Secret Key.

Update config.py:

Open the config.py file.

Replace the placeholder values "YOUR_API_KEY" and "YOUR_API_SECRET" with your actual credentials.

# config.py
API_KEY = "your_actual_api_key_here"
API_SECRET = "your_actual_api_secret_here"

How to Use the Bot
You can interact with the bot in two ways: through the command-line interface or the web UI.

Option 1: Using the Command-Line Interface (CLI)
The CLI is run using the main.py script.

Note: The notional value of an order (Price × Quantity) must be greater than 100 USDT to be accepted by the exchange.

CLI Examples
Place a Market Order:

python main.py market BTCUSDT BUY 0.002

Place a Limit Order:

python main.py limit ETHUSDT SELL 0.05 2550

Place a Stop-Limit Order:

python main.py stop_limit BTCUSDT BUY 0.002 65050 65000

CLI Output
A successful order will display a confirmation table in your console:

┌─ Order Execution Details ─┐
│ Parameter       │ Value   │
├─────────────────┼─────────┤
│ Order ID        │ 1234567 │
│ Symbol          │ BTCUSDT │
│ Side            │ BUY     │
│ Type            │ LIMIT   │
│ Status          │ NEW     │
│ ...             │ ...     │
└─────────────────┴─────────┘

Option 2: Using the Web Interface (UI)
The web interface provides a user-friendly form to place orders.

Start the Web Server:
Run the app.py script from your terminal.

python app.py

Open in Browser:
The terminal will show that the server is running. Open the following URL in your web browser:
http://127.0.0.1:5000

Place Orders:
Fill out the form on the web page to select the order type, symbol, side, and other parameters. Click "Place Order" to submit. Success or error messages will be displayed at the top of the page.

Logging
All actions performed by the bot, whether from the CLI or the Web UI, are recorded in the trading_bot.log file. This file is essential for debugging and provides a complete history of the bot's activity.