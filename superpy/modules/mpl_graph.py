import PySimpleGUI as sg
import matplotlib.pyplot as plt



def create_profit_graph(x_axis, y_axis, company_result):
    line = []
    for i in range(len(x_axis)):
        line.append(0)
    

    plt.plot(x_axis, y_axis, ':k', marker='o')
    plt.plot(x_axis, company_result, color= 'g')
    plt.plot(x_axis, line, color= 'r')
  
    plt.title('profit & company result')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('results', fontsize=12)
    plt.legend(['profit', 'company result'])

    plt.grid(True)
    plt.show()
     
    