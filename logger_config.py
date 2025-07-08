# logger_config.py

import logging
import sys

def setup_logger():
    """Sets up the logger to output to console and a file."""
    # Create a logger
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Prevent logs from being propagated to the root logger
    logger.propagate = False

    # Remove existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler to log to a file 
    file_handler = logging.FileHandler("trading_bot.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler to show logs in the console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Initialize the logger
logger = setup_logger()