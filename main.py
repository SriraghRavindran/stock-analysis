import argparse
from stocks.stocks_data import getStockData
from stocks.stock_analysis import plot_stock_data


parser = argparse.ArgumentParser(  
        description='sum the integers at the command line')  

parser.add_argument('--stock', '-stk',required=True)
parser.add_argument('--start_date','-s', required=True)
parser.add_argument('--end_date','-e', required=True)
args = parser.parse_args()

stock_data = getStockData(args.stock,args.start_date,args.end_date)
print(stock_data)
plot_stock_data(stock_data)

