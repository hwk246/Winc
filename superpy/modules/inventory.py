import PySimpleGUI as sg
from modules.csv_alterations import open_csv
from modules.set_date_and_time import get_current_date, string_to_date

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
    current_date = get_current_date()
    items_bought_before_current_date =[]
    item_sold_before_current_date = []
    inventory_value = []
    output = []
    value_stock = 0
    value_expired = 0


    # get every id from product bought before current date
    for bought_item in items_from_bought_csv:
        if string_to_date(bought_item[3]) <= current_date:
            items_bought_before_current_date.append(bought_item[0]) # list op id's
 
    # get every bought_id from already sold before current date        
    for sold_item in items_from_sell_csv:
        if string_to_date(sold_item[2]) <= current_date:
           item_sold_before_current_date.append(sold_item[1]) # list of bought id''s
    
    # get the actual inventory by excluding the already sold items but still incl possible expired products
    for item in item_sold_before_current_date:
        if item in items_bought_before_current_date:
            items_bought_before_current_date.remove(item)
    # seperate expired from sellable products.
    for item in items_bought_before_current_date:
        for bought_item in items_from_bought_csv:
            if item == bought_item[0]:
                if string_to_date(bought_item[5]) < current_date:
                    output.append([bought_item[0], bought_item[1], bought_item[4], 'no', bought_item[5]])
                    value_expired += float(bought_item[4])
                else:
                    output.append([bought_item[0], bought_item[1], bought_item[4], 'yes', bought_item[5]])
                    value_stock += float(bought_item[4])
 

    
    inventory_value.append([f'Stock goods:', value_stock])
    inventory_value.append([f'Expired goods:', value_expired])

    # setting up and running pySimpleGui inventory table
    headings=['ID','ProductName','Price', 'Sellable', 'Expired']
    headings_value=['            Inventory', 'Value    ', '']
    button = [sg.Button('Ok'), sg.Button('Create XML')]
    output_length = len(output)
    layout = [
            [sg.Table(values=output, 
            headings=headings, max_col_width =35,
            auto_size_columns=True,
            display_row_numbers=False,
            justification = 'center',
            num_rows = output_length+1,
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
                print('------------ > Sorry, not available yet - BetaRelease 2023 < --------------' )

    window.close
  