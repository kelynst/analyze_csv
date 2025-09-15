
import pandas as pd 

def analyze_csv():
    fname = input('Enter CSV file name: ')
    try:
        df = pd.read_csv(fname)

        print('\nCSV Analysis')
        print('---------------')
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        print('\nColumn Names:')
        print(df.columns.tolist())
        print('\nFirst 5 Rows:')
        print(df.head())
    except FileNotFoundError:
        print('File Not Found. Please check the name and try again.') 
if __name__ == '__main__':
    analyze_csv()