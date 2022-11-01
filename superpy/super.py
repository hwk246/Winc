import argparse
import os
import modules.revenue
from modules.csv_alterations import init_csv, add_to_csv
from modules.sell_product import sell
from modules.inventory import create_overview
from modules.set_date import get_current_date, string_to_date
from modules.set_date import set_current_date
from modules.profit import calculate_profit


__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    parser = argparse.ArgumentParser(description='fruit-machine')
    parser.add_argument('operation', 
                        type=str, metavar='buy, sell, inventory, revenue, profit',
                        help='A buy or a sell action or to get an overview', 
                        choices=['buy', 'sell', 'inventory', 'revenue', 'profit'],
                        nargs='?'
                        )
    parser.add_argument('--product_name', 
                        type=str, 
                        metavar='', 
                        help='What kind of fruit you want to buy or sell?')
    parser.add_argument('--price', 
                        type=float, 
                        metavar='', 
                        help='At what price the fruit is sold or bought?')
    parser.add_argument('--expiration_date', 
                        type=str, 
                        metavar='', 
                        help='When you buy, what is the expiration date?')
    parser.add_argument('--date', type=str,
                        metavar='', 
                        help='To get the revenue for a specific month of the year')
    parser.add_argument('--now', 
                        action=('store_true'), 
                        help='To show inventory at current date')
    parser.add_argument('--today', 
                        action=('store_true'), 
                        help='To show revenue at current date')
    parser.add_argument('--yesterday', 
                        action=('store_true'), 
                        help='To show results at current date - 1day')
    parser.add_argument('--advance_time', 
                        type=int, metavar='', 
                        help='This gives you the opportunity to change the current date.')
    
   
    args = parser.parse_args()

    if args.operation == 'buy'  and args.product_name and args.price and args.expiration_date:
        add_to_csv(args.operation, args.product_name, get_current_date(), args.price, args.expiration_date)
    elif args.operation == 'sell' and args.product_name and args.price:
        sell(args.product_name, args.price)
    elif args.operation == 'inventory' and args.now:
        create_overview()
    elif args.operation == 'inventory' and args.yesterday:
        set_current_date(-1)
        create_overview()
        set_current_date(1)
    elif args.operation == 'profit':
        calculate_profit()
    elif args.advance_time:
        set_current_date(args.advance_time)
    elif args.operation == 'revenue' and args.today:
        modules.revenue.get_revenue('today')
    elif args.operation == 'revenue' and args.yesterday:
        modules.revenue.get_revenue('yesterday')
    elif args.operation == 'revenue' and args.date:
        modules.revenue.get_revenue(args.date)
    else: print('--- invalid input, check arguments ---')

if __name__ == "__main__":   
 
    # create bought.csv and sold.csv if they do not exist yet
    if os.path.isfile(os.path.join(os.path.abspath('csv_files'),'bought.csv' )) == False:
        init_csv('bought')
    if os.path.isfile(os.path.join(os.path.abspath('csv_files'),'sold.csv' )) == False:
        init_csv('sold')
    
    main()