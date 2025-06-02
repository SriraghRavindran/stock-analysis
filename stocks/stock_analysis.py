import matplotlib.pyplot as plt

def plot_stock_data(stock_data):
    stock_name = stock_data.columns.get_level_values(1)[0].replace('.NS','')
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'],label = 'Close price', color ='blue')
    plt.title(f"{stock_name} Closing Price (2023)")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()