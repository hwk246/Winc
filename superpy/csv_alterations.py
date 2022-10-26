import os
import csv
import math
from random import random
from set_date import get_current_date

# absolute pahts to csv-files used in superpy
abs_path_bought_csv = os.path.abspath('bought.csv')
abs_path_sold_csv = os.path.abspath('sold.csv')


fieldnames_bought = ['prod_id', 'product_name','count' ,'buy_date', 'buy_price', 'expiration_date']
fieldnames_sold = ['id','bought_id','sell_date','sell_price']

# creating and initialisation of the csv-file
def init_csv(create):

    if create == 'bought':
        with open(abs_path_bought_csv, encoding='utf_8', mode='w', newline='')as csv_file:
            thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_bought)
            thewriter.writeheader()    
    else:
         with open(abs_path_sold_csv, encoding='utf_8', mode='w', newline='')as csv_file:
            thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_sold)
            thewriter.writeheader()  


# add rows to the csv_file bought.csv or sold.csv
def add_to_csv(a, b,c,d='empty',e='empty'):
    if a == 'buy':  
        with open(abs_path_bought_csv, encoding='utf_8', mode='a', newline='')as csv_file:
                thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_bought)
                thewriter.writerow({'prod_id':math.floor(random()*10000), 'count': 1, 'product_name':b, 'buy_date': c, 'buy_price': d, 'expiration_date': e})
    elif a == 'sell':
         with open(abs_path_sold_csv, encoding='utf_8', mode='a', newline='')as csv_file:
                thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_sold)
                thewriter.writerow({'id': math.floor(random()*10000), 'bought_id': b, 'sell_date': get_current_date(), 'sell_price': c})
    

# read content of csv-file
# using 'reader()' instead of 'DictReader()' for list-output wich in this case is more practical (although it is just a flatten(dict))
def open_csv(sell_buy):
    if sell_buy == 'bought':
        csv_path = abs_path_bought_csv
    else: 
        csv_path = abs_path_sold_csv

    with open(csv_path)as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        data = list(reader)
          
    return data
       
  
 