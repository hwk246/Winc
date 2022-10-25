import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def create_profit_graph():
    year = [1920,1921,1922, 1923, 1924, 1925,1926,1927,1928,1929,1930 ]
    revenue = [2,4,6,8,8,9,9,8,8,7,6 ]
    costs = [1,2,3,4,5,6,5,4,3,2,1 ]
    profit = [1,2,3,4,3,3,4,4,5,5,5 ]


    plt.plot(year, revenue, color= 'blue', marker='o')
    plt.plot(year, costs, color= 'red', marker='o')
    plt.plot(year, profit, color= 'green', marker='o')
    plt.title('profit')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('profit', fontsize=14)

    plt.grid(True)
    plt.show()
     
    