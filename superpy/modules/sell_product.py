import PySimpleGUI as sg
from modules.csv_alterations import open_csv, add_to_csv
from modules.set_date_and_time import string_to_date, get_current_date, get_advance_time
from modules.PySimpleGui import create_window


def sell(product_name, price):

    sold = False
    in_stock = False
    expired = True
    already_sold = False
    bought_items = open_csv('bought')
    
    #  on a 'First in First out' principle this procuct will be sold
    sold_item_bought_id = []
    # find the specified product in the bought.csv
    for bought_item in bought_items:
        if bought_item[1] == product_name:
            in_stock = True
            # check if this bought item is not expired.
            if string_to_date(bought_item[5]) >= get_current_date():  
                expired = False
                # check if item is not already sold.             
                sold_items = open_csv('sold')
                # if sold list is empty. then the item can be sold directly.
                if len(sold_items) == 0: 
                    sold = True                             
                    add_to_csv('sell', bought_item[0], price )
                    break
                else:
                    for sold_item in sold_items:
                        sold_item_bought_id.append(sold_item[1])
                    if bought_item[0] not in sold_item_bought_id:     
                        sold = True                                   
                        add_to_csv('sell', bought_item[0], price )
                        break
                    else:
                        already_sold = True

    # only if advance_time is 0 a message can be shown 
    advance_timer = get_advance_time()
    if advance_timer == 0:

        # conditions for specific messages to the user.
        if sold is True and expired is False and in_stock is True:
            information = [sg.Text(f'{product_name} has been succesfully registered as sold', size=(50,2), justification='center')]
        if in_stock and expired is False and already_sold is True:
            information = [sg.Text(f'every sellable {product_name} was sold', size=(50,2), justification='center')]  
        elif in_stock and expired is True:
            information = [sg.Text(f' {product_name} is expired and can not be sold', size=(50,2), justification='center')]  
        elif in_stock is False:
            information = [sg.Text(f'{product_name} is not in stock', size=(50,2), justification='center')]

        create_window(information)
    