from modules.csv_alterations import open_csv
from modules.mpl_graph import create_profit_graph
import numpy as np

def calculate_profit():

    sold_items = open_csv('sell')
    bought_items = open_csv('bought')
    dates = []
   
    ''' 
    find all dates where something was bought or sold this can be used
    for x-axes in the profit-graph and for a loop to find the profit at that time
    this list has to have unique dates and be oredered 
    '''

    for item in bought_items:
        dates.append(item[3])
  
    for item in sold_items:
      dates.append(item[2])

    unique_data_list = list(set(dates))
    unique_data_list.sort()
    x_axis = []
    y_axis =[]

    for operation_date in unique_data_list:
        bought_on_date = 0
        sold_on_date = 0
        for item in bought_items:
            if operation_date == item[3]:
                bought_on_date += float(item[4])
        for item in sold_items:
            if operation_date == item[2]:
                sold_on_date += float(item[3])
        profit_on_date = sold_on_date - bought_on_date
        x_axis.append(operation_date)
        y_axis.append(profit_on_date)

    company_result = np.cumsum(y_axis)

    create_profit_graph(x_axis, y_axis, company_result)
    
    

    

  





