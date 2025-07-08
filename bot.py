# bot.py

from binance import Client, enums
from binance.exceptions import BinanceAPIException, BinanceRequestException
from logger_config import logger
from config import BASE_URL

class BasicBot:
    """A simplified trading bot for Binance Futures Testnet."""

    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """Initializes the bot with API credentials."""
        # This parameter was added to increase the request timeout.
        request_params = {'timeout': 20}
        
        self.client = Client(
            api_key, 
            api_secret, 
            testnet=testnet, 
            requests_params=request_params
        )
        
        if testnet:
            self.client.FUTURES_URL = BASE_URL
        
        logger.info("Bot initialized for Binance Futures Testnet.")

    def _place_order(self, **kwargs):
        """A private helper method to place an order and handle responses."""
        try:
            logger.info(f"Placing order with parameters: {kwargs}")
            order = self.client.futures_create_order(**kwargs)
            logger.info(f"Successfully placed order: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            return {"error": f"API Error: {e.message}"}
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error: {e.status_code} - {e.message}")
            return {"error": f"Request Error: {e.message}"}
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"error": f"An unexpected error: {e}"}

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """Places a market order."""
        side_enum = enums.SIDE_BUY if side.upper() == 'BUY' else enums.SIDE_SELL
        return self._place_order(
            symbol=symbol,
            side=side_enum,
            type=enums.ORDER_TYPE_MARKET,
            quantity=quantity
        )

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """Places a limit order."""
        side_enum = enums.SIDE_BUY if side.upper() == 'BUY' else enums.SIDE_SELL
        return self._place_order(
            symbol=symbol,
            side=side_enum,
            type=enums.ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=enums.TIME_IN_FORCE_GTC  # Good 'Til Canceled
        )

    # Bonus Feature: Stop-Limit Order
    def place_stop_limit_order(self, symbol: str, side: str, quantity: float, price: float, stop_price: float):
        """Places a stop-limit order."""
        side_enum = enums.SIDE_BUY if side.upper() == 'BUY' else enums.SIDE_SELL
        return self._place_order(
            symbol=symbol,
            side=side_enum,
            # This was changed to the string 'STOP' to work with the Futures API.
            type='STOP',
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce=enums.TIME_IN_FORCE_GTC
        )