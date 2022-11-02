import PySimpleGUI as sg
from datetime import datetime
from modules.csv_alterations import open_csv
from modules.set_date_and_time import get_current_date, string_to_date, subtract_one_day 
from modules.PySimpleGui import create_window


def revenue_total(revenue_date, desired_date=None):
    sold_items = open_csv('sell')
    revenue = 0
    if desired_date == 'today' or desired_date == 'yesterday':
        for item in sold_items:
            if string_to_date(item[2]) <= revenue_date:
                revenue += float(item[3])
        return revenue

    else:
        year = revenue_date.split('-')[0]
        month = revenue_date.split('-')[1]
        month_name = datetime(1, int(month), 1).strftime("%B")
        for item in sold_items:
            if item[2].split('-')[0] == year  and item[2].split('-')[1] == month:
                revenue += float(item[3])
                revenue = round(revenue,1)
        return [revenue, month_name]


def get_revenue(desired_date):
    information =[]
   
    match desired_date:
        case 'today':
            revenue_date = get_current_date()
            revenue = revenue_total(revenue_date, desired_date)
            information = [sg.Text(f'Today\'s revenue so far: {revenue}' , size=(50,2), justification='center')]  
        case 'yesterday':
            revenue_date = subtract_one_day(get_current_date())  
            revenue = revenue_total(revenue_date, desired_date)
            information = [sg.Text(f'Yesterday\'s revenue: {revenue}' , size=(50,2), justification='center')]  
        case other:
            revenue = revenue_total(desired_date)
            information = [sg.Text(f'{revenue[1]} revenue: {revenue[0]}' , size=(50,2), justification='center')] 
 

    create_window(information, f'Revenue - {desired_date}')