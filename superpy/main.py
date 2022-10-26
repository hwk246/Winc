# Imports
import argparse
from csv_alterations import init_csv, add_to_csv
from buy_sell import sell
from inventory import create_overview
from mpl_graph import create_profit_graph
import os
from set_date import get_current_date, string_to_date


__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    
    parser = argparse.ArgumentParser(description='fruit-machine')
    parser.add_argument('operation', type=str, metavar='', help='A buy or a sell action', choices=['buy', 'sell', 'profit_graph', 'inventory'])
    parser.add_argument('--product_name', type=str, metavar='', help='What kind of fruit you want to buy or sell?')
    parser.add_argument('--price', type=int, metavar='', help='At what price the fruit is sold or bought?')
    parser.add_argument('--expiration_date', type= lambda x: string_to_date(x), metavar='', help='When you buy, what is the expiration date?')
    parser.add_argument('--advance_time', type=int, help='This gives you the opportunity to change the current date.')
   
    args = parser.parse_args()

    if args.operation == 'buy'  and args.product_name and args.price and args.expiration_date:
        add_to_csv(args.operation, args.product_name, get_current_date(), args.price, args.expiration_date)
    elif args.operation == 'sell' and args.product_name and args.price:
        sell(args.product_name, args.price)
    elif args.operation == 'inventory':
        create_overview()
    elif args.operation == 'profit_graph':
        create_profit_graph()
    else: print('--- invalid input, check arguments')


if __name__ == "__main__":   

    # create bought.csv and sold.csv if they do not exist yet
    if os.path.isfile(os.path.abspath('bought.csv')) == False:
        init_csv('bought')
    if os.path.isfile(os.path.abspath('sold.csv')) == False:
        init_csv('sold')

    # start main()
    main()
   


