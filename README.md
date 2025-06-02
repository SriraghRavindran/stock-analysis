# Stock Analysis

A command-line tool to fetch and plot stock data for a given ticker and date range.

## Features

- Fetches stock data for a specified ticker symbol and date range
- Plots the closing price using Matplotlib

## Requirements

- Python 3.7+
- pandas
- matplotlib

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

```sh
python main.py --stock TATASTEEL.NS --start_date 2023-03-01 --end_date 2023-04-05
```

**Arguments:**
- `--stock` or `-stk`: Stock ticker symbol (e.g., `TATASTEEL`)
- `--start_date` or `-s`: Start date in `YYYY-MM-DD` format
- `--end_date` or `-e`: End date in `YYYY-MM-DD` format

## Example

```sh
python main.py --stock TATASTEEL --start_date 2023-03-01 --end_date 2023-04-05
```

## Project Structure

```
stock-analysis/
├── main.py
├── stocks/
│   ├── stocks_data.py
│   └── stock_analysis.py
```

## License

MIT License