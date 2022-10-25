from csv_alterations import open_csv
import PySimpleGUI as sg
from datetime import datetime, date


# create data for  pySimpleGui overview of selected fruit
def create_overview(operation):
    output = []
    if operation == 'buy':
        items_from_bought_csv = open_csv('bought')
        list_of_unique_fruits = []

        # get a list of all unique fruits         
        for item in items_from_bought_csv:
            list_of_unique_fruits.append(item[1])
        list_of_unique_fruits = set(list_of_unique_fruits)
        print(list_of_unique_fruits)

        # create output for presentation table. create total of sellable and expired fruit
        for fruit in list_of_unique_fruits:
            total_sellable = 0
            total_expired = 0
            for item in items_from_bought_csv:
                if fruit == item[1]:
                    fruit_exp_date = datetime.strptime(item[5],'%Y-%m-%d').date()
                    if fruit_exp_date > date.today():
                        total_sellable += 1
                    else: total_expired += 1
                    
            output.append([fruit, total_sellable, total_expired])
            headings=['ProductName', 'Sellable', 'Expired']
    else: headings=['ProductName', 'Sellable', 'Expired']
  
    # setting up and running pySimpleGui overview

    

  
    button = [sg.Button('OK'), sg.Button('Create XML')]

    layout = [
        [sg.Table(values=output, 
        headings=headings, max_col_width =35,
        auto_size_columns=True,
        display_row_numbers=False,
        justification = 'center',
        num_rows = 5,
        key='TABLE',
        row_height=35
        )], 
        button
        ]

    window = sg.Window('FruitMachine', layout)


    while True:
        event, values = window.read()
        if event == 'OK' or event == sg.WIN_CLOSED:
            break
        elif event == 'Create XML':
            print('------------ > Sorry, not available yet')

    window.close

   
    '''
    for item in items_from_bought_csv:
        if item[1] == fruit:
            date_str_obj1 = datetime.strptime(item[5], '%Y-%m-%d').date()
            if date_str_obj1 > date.today() :
                total_amount_sellable_fruit += int(item[2])
            else: total_amount_expired_fruit += int(item[2])

    print('See overview on Fruit Machine of fruit in stock')
   
    '''


