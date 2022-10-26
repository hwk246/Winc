from datetime import datetime

def string_to_date(date_string):
    return  (datetime.strptime(date_string, "%Y-%m-%d").date())
 
def set_current_date(new_date):
    current_date = open('current_date.txt', 'w' )
    current_date.write(new_date)

def get_current_date():
    read = open('current_date.txt', 'r' )
    string_date = read.readline()
    return string_to_date(string_date)
    
   
