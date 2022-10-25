# Imports
import argparse
from csv_alterations import init_csv, add_to_csv, open_csv
from overview import create_overview
from mpl_graph import create_profit_graph
from datetime import datetime, date



# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# init_csv()

def main():
    
    parser = argparse.ArgumentParser(description='fruit-machine')
    parser.add_argument('operation', type=str, metavar='', help='A buy or a sell action', choices=['buy', 'sell', 'profit_graph'])
    parser.add_argument('--product_name', type=str, metavar='', help='What kind of fruit you want to buy or sell?')
    parser.add_argument('--price', type=int, metavar='', help='At what price the fruit is sold or bought?')
    parser.add_argument('--expiration_date', type= lambda x: datetime.strptime(x, '%Y-%m-%d').date(), metavar='', help='When you buy, what is the expiration date?')
    parser.add_argument('-o', '--overview', action='store_true' , help='When you buy, what is the expiration date?')

    
   
    args = parser.parse_args()

   
    if args.operation == 'buy' and args.overview == False and args.product_name and args.price and args.expiration_date:
        add_to_csv(args.product_name, date.today(), args.price, args.expiration_date)
    elif args.overview and (args.operation == 'buy' or args.operation == 'sell'):
        create_overview(args.operation)
    elif args.operation == 'profit_graph':
        create_profit_graph()
    else: print('--- invalid input, check arguments')






 
if __name__ == "__main__":
    main()
   


