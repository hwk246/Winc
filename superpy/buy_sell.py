import csv_alterations
from csv_alterations import open_csv
from datetime import datetime
from set_date import string_to_date
from set_date import get_current_date
from csv_alterations import add_to_csv


def sell(product_name, price):
    in_stock = False
    expired = True
    sellable = False
  

    #  on a 'First in First out' principle this procuct will be sold

    # find the specified product in the bought.csv
    bought_items = open_csv('bought')
    for bought_item in bought_items:
        if bought_item[1] == product_name:
            in_stock = True
            # check if this bought item is not expired
            if string_to_date(bought_item[5]) > get_current_date():  
                expired = False
                # check if item is not already sold              
                sold_items = open_csv('sold')
                # if sold list is empty. then the item can be sold directly
                if len(sold_items) == 0:                              
                    sellable = True
                    add_to_csv('sell', bought_item[0], price )
                    break
                else:
                    for sold_item in sold_items:
                        if sold_item[1] !=  bought_item[0]:                             
                            sellable = True                           
                            add_to_csv('sell', bought_item[0], price )
                            break
     
    if sellable:
        print('')
        print('+---------------------------------------------------------+')
        print(f'     {product_name} has been succesfully registered as sold      ')
        print('+=========================================================+')
        print('')
    elif in_stock and expired is False:
        print('')
        print('+---------------------------------------------------------+')
        print (f'        every sellable {product_name} was sold          ')
        print('+=========================================================+')
        print('')
    elif in_stock is False:
        print('')
        print('+---------------------------------------------------------+')
        print (f'         {product_name} is not in stock        ')
        print('+=========================================================+')
        print('')
    print('maybe I forgot something here')



     



               
                
    
   

  
    
    

