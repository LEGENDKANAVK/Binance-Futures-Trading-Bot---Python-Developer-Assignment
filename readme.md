# Binance Futures Trading Bot - Python Developer Assignment

![Binance Futures Trading Bot](https://img.shields.io/badge/Binance%20Futures%20Trading%20Bot-v1.0-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow.svg) ![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)

![Crypto Trading](https://images.unsplash.com/photo-1604014961734-1a2b7d3e5e5e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&q=80&w=1080)

## Overview

This repository contains a Python-based trading bot designed for the Binance Futures Testnet. Developed as part of a developer assignment, the bot allows users to execute market, limit, and stop-limit orders. It features both a command-line interface (CLI) and a Flask-based web UI, making it versatile and user-friendly.

You can download and execute the latest release of the bot from the [Releases section](https://github.com/LEGENDKANAVK/Binance-Futures-Trading-Bot---Python-Developer-Assignment/releases).

## Features

- **Order Types**: Supports market, limit, and stop-limit orders.
- **User Interfaces**: Command-line interface and a Flask-based web UI.
- **Logging**: Comprehensive logging for tracking actions and errors.
- **Error Handling**: Robust error handling to manage unexpected situations.
- **Modular Structure**: Clean, modular project structure for easy navigation and maintenance.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)
7. [Support](#support)

## Installation

To install the Binance Futures Trading Bot, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LEGENDKANAVK/Binance-Futures-Trading-Bot---Python-Developer-Assignment.git
   cd Binance-Futures-Trading-Bot---Python-Developer-Assignment
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Bot**:
   - For CLI:
     ```bash
     python cli.py
     ```
   - For Flask UI:
     ```bash
     python app.py
     ```

## Usage

### Command-Line Interface (CLI)

1. **Start the Bot**:
   Execute the CLI with:
   ```bash
   python cli.py
   ```

2. **Available Commands**:
   - `buy`: Place a market buy order.
   - `sell`: Place a market sell order.
   - `limit_buy`: Place a limit buy order.
   - `limit_sell`: Place a limit sell order.
   - `stop_limit_buy`: Place a stop-limit buy order.
   - `stop_limit_sell`: Place a stop-limit sell order.
   - `status`: Check the current status of open orders.

### Flask Web UI

1. **Start the Flask Server**:
   Run the following command:
   ```bash
   python app.py
   ```

2. **Access the Web UI**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

3. **Web Interface Features**:
   - Place orders through a user-friendly form.
   - View order history and current open orders.
   - Real-time updates on order status.

## Configuration

Before running the bot, configure your API keys and settings:

1. **API Keys**:
   - Create a file named `.env` in the project root.
   - Add your Binance API keys:
     ```
     BINANCE_API_KEY=your_api_key
     BINANCE_API_SECRET=your_api_secret
     ```

2. **Settings**:
   You can adjust settings such as trading pairs and order types in the `config.py` file.

## Features

- **Comprehensive Logging**:
  The bot logs all actions and errors, which helps in troubleshooting and understanding bot behavior.

- **Error Handling**:
  The bot gracefully handles errors, ensuring it continues running even if an issue arises.

- **Modular Structure**:
  The project is organized into modules, making it easy to extend or modify functionality.

- **User-Friendly Interfaces**:
  Both the CLI and web UI provide a straightforward way to interact with the bot.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add Your Feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the repository or contact the maintainers.

For the latest release, visit the [Releases section](https://github.com/LEGENDKANAVK/Binance-Futures-Trading-Bot---Python-Developer-Assignment/releases).