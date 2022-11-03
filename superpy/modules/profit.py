from modules.csv_alterations import open_csv
from modules.mpl_graph import create_profit_graph
import numpy as np

def calculate_profit():

    sold_items = open_csv('sell')
    bought_items = open_csv('bought')
    dates = []

    for item in bought_items:
        dates.append(item[3])
  
    for item in sold_items:
      dates.append(item[2])

# because selling and buying actions can be done on the same date,make a list of unique dates to avoid doubles . 
    unique_data_list = list(set(dates))
    unique_data_list.sort()
    x_axis = [] # dates presented on the x-axis of the graph
    profit =[]

    for operation_date in unique_data_list:
        bought_on_date = 0
        sold_on_date = 0
        for item in bought_items:
            if operation_date == item[3]:
                bought_on_date += float(item[4])
        for item in sold_items:
            if operation_date == item[2]:
                sold_on_date += float(item[3])
        # the actual profit on a unique date  
        profit_on_date = sold_on_date - bought_on_date
        x_axis.append(operation_date)
        profit.append(profit_on_date)

# calculating the cumulative by numpy
    company_result = np.cumsum(profit)

    create_profit_graph(x_axis, profit, company_result)