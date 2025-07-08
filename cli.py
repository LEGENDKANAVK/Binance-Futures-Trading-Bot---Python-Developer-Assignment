# cli.py

import argparse
from rich.console import Console
from rich.table import Table
from rich import print as rprint

def validate_inputs(args):
    """Validates user command-line arguments. [cite: 23]"""
    errors = []
    if args.side.upper() not in ['BUY', 'SELL']:
        errors.append("Invalid order side. Must be 'BUY' or 'SELL'.")

    if args.quantity <= 0:
        errors.append("Quantity must be a positive number.")

    if args.order_type in ['limit', 'stop_limit']:
        if not args.price or args.price <= 0:
            errors.append("Price must be a positive number for limit and stop-limit orders.")

    if args.order_type == 'stop_limit':
        if not args.stop_price or args.stop_price <= 0:
            errors.append("Stop price must be a positive number for stop-limit orders.")

    return errors

def get_cli_parser():
    """Configures and returns the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="A simplified crypto trading bot for Binance Futures Testnet.",
        epilog="Example: python main.py market BTCUSDT BUY 0.001"
    )

    # Subparsers for different order types
    subparsers = parser.add_subparsers(dest='order_type', required=True, help='The type of order to place')

    # Market Order Parser
    market_parser = subparsers.add_parser('market', help='Place a market order')
    market_parser.add_argument('symbol', type=str, help='The trading symbol (e.g., BTCUSDT)')
    market_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side: BUY or SELL') # [cite: 21]
    market_parser.add_argument('quantity', type=float, help='The amount to trade')

    # Limit Order Parser
    limit_parser = subparsers.add_parser('limit', help='Place a limit order')
    limit_parser.add_argument('symbol', type=str, help='The trading symbol (e.g., BTCUSDT)')
    limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side: BUY or SELL') # [cite: 21]
    limit_parser.add_argument('quantity', type=float, help='The amount to trade')
    limit_parser.add_argument('price', type=float, help='The price at which to set the limit order')

    # Stop-Limit Order Parser (Bonus) 
    stop_limit_parser = subparsers.add_parser('stop_limit', help='Place a stop-limit order')
    stop_limit_parser.add_argument('symbol', type=str, help='The trading symbol (e.g., BTCUSDT)')
    stop_limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side: BUY or SELL') # [cite: 21]
    stop_limit_parser.add_argument('quantity', type=float, help='The amount to trade')
    stop_limit_parser.add_argument('price', type=float, help='The limit price for the order')
    stop_limit_parser.add_argument('stop_price', type=float, help='The price at which the limit order is triggered')

    return parser

def display_order_confirmation(response: dict):
    """
    Displays order confirmation in a formatted table. [cite: 24]
    Fulfills the bonus for an enhanced CLI. 
    """
    console = Console()

    if response.get("error"):
        rprint(f"[bold red]Order Failed:[/bold red] {response['error']}")
        return

    table = Table(title="[bold green]Order Execution Details[/bold green]", show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="yellow")

    table.add_row("Order ID", str(response.get('orderId')))
    table.add_row("Symbol", response.get('symbol'))
    table.add_row("Side", response.get('side'))
    table.add_row("Type", response.get('type'))
    table.add_row("Status", f"[bold green]{response.get('status')}[/bold green]")
    table.add_row("Quantity", response.get('origQty'))
    table.add_row("Price", response.get('price'))
    if response.get('stopPrice') and float(response.get('stopPrice')) > 0:
        table.add_row("Stop Price", response.get('stopPrice'))
    table.add_row("Client Order ID", response.get('clientOrderId'))
    table.add_row("Executed Quantity", response.get('executedQty'))

    console.print(table)