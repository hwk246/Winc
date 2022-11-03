import matplotlib.pyplot as plt
import pandas as pd


def create_profit_graph(x_axis, profit, company_result):
    line = []
    # create red horizontal line to reference 0
    for i in range(len(x_axis)):
        line.append(0)

    data = {'date': x_axis, 
            'profit': profit, 
            'result': company_result,
            'zero_line': line}

    # table overview from profit and result in command line
    df = pd.DataFrame.from_dict(data); df
    print('')
    print('-------------------------------------------')
    print(df)
    print('-------------------------------------------\n')
 
    plt.figure(figsize= (13,5), dpi=100)
    ax1 = plt.subplot(1,1,1)
    ax1.bar(df.date, df.profit, color='lightGreen')
    ax1.plot(df.date, df.result, linewidth = 3)
    ax1.plot(df.date, df.zero_line, '--', color='red')
    ax1.yaxis.grid(linestyle = '--', linewidth =0.3)
    ax1.spines['top'].set_linewidth(0.5)
    ax1.spines['bottom'].set_linewidth(0.5)
    ax1.spines['right'].set_linewidth(0)
    ax1.spines['left'].set_linewidth(0)

    plt.title('Profit & Result', fontsize=18, weight= 'bold')
    plt.ylabel('results', fontsize=12)
    plt.legend(['company result','line_zero','profit' ])
    plt.show()