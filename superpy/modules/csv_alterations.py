import os
import csv
import PySimpleGUI as sg
from modules.set_date import get_current_date, increment
from modules.PySimpleGui import create_window


# absolute pahts to csv-files used in superpy
abs_path_bought_csv = os.path.join(os.path.abspath('csv_files'),'bought.csv' )
abs_path_sold_csv = os.path.join(os.path.abspath('csv_files'),'sold.csv' )


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
def add_to_csv(a,b,c,d='empty',e='empty'):
    if a == 'buy':  
        with open(abs_path_bought_csv, encoding='utf_8', mode='a', newline='')as csv_file:
                thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_bought)
                thewriter.writerow({'prod_id':increment('buy'), 'count': 1, 'product_name':b, 'buy_date': c, 'buy_price': d, 'expiration_date': e})
                create_window([sg.Text(f'{b} has been succesfully registered as bought', size=(50,2), justification='center')])
                
    elif a == 'sell':
         with open(abs_path_sold_csv, encoding='utf_8', mode='a', newline='')as csv_file:
                thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames_sold)
                thewriter.writerow({'id': increment('sell'), 'bought_id': b, 'sell_date': get_current_date(), 'sell_price': c})
    

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