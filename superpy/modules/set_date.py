from datetime import datetime, timedelta

def string_to_date(date_string):
    return  (datetime.strptime(date_string, "%Y-%m-%d").date())
 
def set_current_date(number_of_days):
    date_today = get_current_date()
    new_date = date_today + timedelta(days=number_of_days) 
    change_date = open('text_files/current_date.txt', 'w' )
    change_date.write(str(new_date))

def get_current_date():
    read = open('text_files/current_date.txt', 'r' )
    string_date = read.readline()
    return string_to_date(string_date) # retuns a date

def increment(operation):
    if operation == 'buy':
        file_name = 'text_files/bought_prod_number.txt'
    elif operation == 'sell':
        file_name = 'sell_prod_number.txt'
    
    current_number = open(file_name, 'r')
    number = int(current_number.readline())+1
    new_number = open(file_name, 'w')
    new_number.write(str(number))
    return number

def subtract_one_day(input_date):
    return input_date - timedelta(days = 1)


