'''
Emily Ng
MatPlotLib Lab
'''

import numpy as np
import pandas as pd
import matplotlib .pyplot as plt

def main():
    #read file
    df = pd.read_csv('company_sales_data.csv')

    #profits
    profitList = df['total_profit']

    #months
    monthList = df['month_number'].tolist()

    #plot
    plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
    plt.xlabel('Month number')
    plt.ylabel('Profit in dollar')
    plt.xticks(monthList)
    plt.title('Company profit per month')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()

    #red line
    plt.plot(monthList, profitList, label='Profit data of last year',
             color='r', marker='o', markerfacecolor='k',
             linestyle='--', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Profit in dollar')
    plt.legend(loc='lower right')
    plt.title('Company Sales data of last year')
    plt.xticks(monthList)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()

    #all products
    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()
    toothPasteSalesData = df['toothpaste'].tolist()
    bathingsoapSalesData = df['bathingsoap'].tolist()
    shampooSalesData = df['shampoo'].tolist()
    moisturizerSalesData = df['moisturizer'].tolist()

    plt.plot(monthList, faceCremSalesData, label='Face cream Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, faceWashSalesData, label='Face Wash Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, toothPasteSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, bathingsoapSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, shampooSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, moisturizerSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(monthList)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.title('Sales data')
    plt.show()

    #toothpaste scatter plot
    plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
    plt.xlabel('Month Number')
    plt.ylabel('Number of units Sold')
    plt.legend(loc='upper left')
    plt.title(' Tooth paste Sales data')
    plt.xticks(monthList)
    plt.grid(True, linewidth= 1, linestyle="--")
    plt.show()

    #face cream and face wash bar chart
    plt.bar([a - 0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face Cream sales data', align='edge')
    plt.bar([a + 0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face Wash sales data', align='edge')
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title(' Sales data')

    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()

    #bar chart of soap
    plt.bar(monthList, bathingsoapSalesData)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.title(' Sales data')
    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('bathingsoap sales data')
    plt.show()

    #total profit histogram
    labels = ['low', 'average', 'Good', 'Best']
    profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    plt.hist(profitList, profit_range, label='Profit data')
    plt.xlabel('profit range in dollar')
    plt.ylabel('Actual Profit in dollar')
    plt.legend(loc='upper left')
    plt.xticks(profit_range)
    plt.title('Profit data')
    plt.show()

    #piechart
    labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
    salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
                 df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
    plt.axis("equal")
    plt.pie(salesData, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title('Sales data')
    plt.show()

    #read bathing soap face wash of all months and displaying it
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(monthList, bathingsoap, label='Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
    axarr[0].set_title('Sales data of  a Bathingsoap')
    axarr[1].plot(monthList, faceWashSalesData, label='Face Wash Sales Data', color='r', marker='o', linewidth=3)
    axarr[1].set_title('Sales data of  a facewash')

    plt.xticks(monthList)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.show()

    #stack plot
    plt.plot([], [], color='m', label='face Cream', linewidth=5)
    plt.plot([], [], color='c', label='Face wash', linewidth=5)
    plt.plot([], [], color='r', label='Tooth paste', linewidth=5)
    plt.plot([], [], color='k', label='Bathing soap', linewidth=5)
    plt.plot([], [], color='g', label='Shampoo', linewidth=5)
    plt.plot([], [], color='y', label='Moisturizer', linewidth=5)

    plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
                  bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
                  colors=['m', 'c', 'r', 'k', 'g', 'y'])

    plt.xlabel('Month Number')
    plt.ylabel('Sales unints in Number')
    plt.title('Alll product sales data using stack plot')
    plt.legend(loc='upper left')
    plt.show()



main()




