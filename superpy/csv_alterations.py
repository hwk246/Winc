import os
import csv
import math
from random import random

# absolute pahts to csv-files used in superpy
abs_path_bought_csv = os.path.abspath('bought.csv')
abs_path_sold_csv = os.path.abspath('sold.csv')


fieldnames = ['prod_id', 'product_name','count' ,'buy_date', 'buy_price', 'expiration_date']

# creating and initialisation of the csv-file
def init_csv():
    with open(abs_path_bought_csv, encoding='utf_8', mode='w', newline='')as csv_file:
        thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        thewriter.writeheader()      

# add rows to the csv_file bought.csv or sold.csv
def add_to_csv(b,c,d,e):
    with open(abs_path_bought_csv, encoding='utf_8', mode='a', newline='')as csv_file:
        thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        thewriter.writerow({'prod_id':math.floor(random()*10000), 'count': 5, 'product_name':b, 'buy_date': c, 'buy_price': d, 'expiration_date': e})
       

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
       
  
 