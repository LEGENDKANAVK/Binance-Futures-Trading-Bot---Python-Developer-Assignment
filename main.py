# main.py

from bot import BasicBot
from config import API_KEY, API_SECRET
from cli import get_cli_parser, validate_inputs, display_order_confirmation
from logger_config import logger
from rich import print as rprint

def main():
    """Main function to run the trading bot."""
    # Check for placeholder API keys
    if API_KEY == "YOUR_API_KEY" or API_SECRET == "YOUR_API_SECRET":
        rprint("[bold red]ERROR:[/bold red] Please replace placeholder API credentials in 'config.py'.")
        logger.error("API keys are placeholders. Exiting.")
        return

    # Setup CLI and parse arguments [cite: 23]
    parser = get_cli_parser()
    args = parser.parse_args()

    # Validate inputs [cite: 23]
    errors = validate_inputs(args)
    if errors:
        for error in errors:
            rprint(f"[bold red]Input Error:[/bold red] {error}")
        logger.error(f"Input validation failed: {errors}")
        return

    # Initialize and run the bot
    try:
        bot = BasicBot(api_key=API_KEY, api_secret=API_SECRET)
        response = None

        if args.order_type == 'market':
            response = bot.place_market_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                quantity=args.quantity
            )
        elif args.order_type == 'limit':
            response = bot.place_limit_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                quantity=args.quantity,
                price=args.price
            )
        elif args.order_type == 'stop_limit': # 
            response = bot.place_stop_limit_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                quantity=args.quantity,
                price=args.price,
                stop_price=args.stop_price
            )

        if response:
            display_order_confirmation(response) # [cite: 24]

    except Exception as e:
        logger.critical(f"A critical error occurred in main execution: {e}", exc_info=True)
        rprint(f"[bold red]A critical error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()