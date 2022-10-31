import PySimpleGUI as sg
from modules.csv_alterations import open_csv
from modules.set_date import get_current_date, string_to_date

def unique_product_list():
    unique_products= []
    items_from_bought_csv = open_csv('bought')
    if len(items_from_bought_csv) > 0:
        for items in items_from_bought_csv:
            unique_products.append(items[1])
            unique_product = set(unique_products)  
        return unique_product
    else:
        return ['none']
 
# create data for  pySimpleGui overview of selected fruit
def create_overview():
    
    items_from_bought_csv = open_csv('bought')
    items_from_sell_csv = open_csv('sell')
    items_expired = []
    items_sellable =[]
    items_bought_before_current_date =[]
    item_sold_before_current_date = []
    current_date = get_current_date()

    # get every id from product bought before current date
    for bought_item in items_from_bought_csv:
        if string_to_date(bought_item[3]) <= current_date:
            items_bought_before_current_date.append(bought_item[0])
 
    # get every bought_id from already sold before current date        
    for sold_item in items_from_sell_csv:
        if string_to_date(sold_item[2]) <= current_date:
           item_sold_before_current_date.append(sold_item[1])
    
    # get the actual inventory (incl possible expired products)
    for item in item_sold_before_current_date:
        if item in items_bought_before_current_date:
            items_bought_before_current_date.remove(item)
 
    # seperate expired from sellable products.
    for item in items_bought_before_current_date:
        for bought_item in items_from_bought_csv:
            if item == bought_item[0]:
                if string_to_date(bought_item[5]) < current_date:
                    items_expired.append(bought_item)
                else:
                    items_sellable.append(bought_item)
  
    # prepare data for overview in PySimpleGui
    output = []
    inventory_value = []
    value_stock = 0
    value_expired = 0
    for unique_item in unique_product_list():
        sellable_amount = 0
        expired_amount = 0
        for item_sellable in items_sellable:
            if item_sellable[1] == unique_item:
                sellable_amount += 1
                value_stock += float(item_sellable[4])
        for item_expired in items_expired:
            if item_expired[1] == unique_item:
                expired_amount +=1
                value_expired += float(item_expired[4])

        output.append([unique_item, sellable_amount, expired_amount])

    inventory_value.append([f'Stock goods:', value_stock])
    inventory_value.append([f'Expired goods:', value_expired])

    # setting up and running pySimpleGui inventory table
    headings=['ProductName', 'Sellable', 'Expired']
    headings_value=['           Inventory', 'Value', ' ']
    button = [sg.Button('Ok'), sg.Button('Create XML')]
    layout = [
            [sg.Table(values=output, 
            headings=headings, max_col_width =35,
            auto_size_columns=True,
            display_row_numbers=False,
            justification = 'center',
            num_rows = len(unique_product_list())+1,
            key='TABLE',
            row_height=25
            )],
            [sg.Table(values=inventory_value, 
            headings=headings_value,
            auto_size_columns=True,
            display_row_numbers=False,
            justification = 'center',
            num_rows = 3,
            key='TABLE',
            row_height=25
            )],                  
            button,  
            ]
            
    window = sg.Window(f'INVENTORY   @{current_date}', layout, element_justification='c')

    while True:
            event, values = window.read()
            if event == 'Ok' or event == sg.WIN_CLOSED:
                break
            elif event == 'Create XML':
                print('------------ > Sorry, not available yet')

    window.close