from pyexpat import model
#import schedule
from model import *
#import time
import pandas as pd
import argparse
def pred(yesterday, stlist):
        invest = []
        for s,t in zip(yesterday,stlist):
            print("Analyzing stock--: ", t)
            parser = argparse.ArgumentParser(description='predict')
            parser.add_argument('--ticker', type=str, default=t, help='Stock Ticker')
            parser.add_argument('--days', type=int, default=7, help='Number of days to predict')
            args = parser.parse_args()
            prediction_list = predict(ticker=args.ticker, days=args.days)
            output = convert(prediction_list)
            
            val = (s - next(iter(output.values())))/s
            if abs(val) > 0.15:
                invest.append(s)
                print("****************15 percent more change, High chance to invest*************")
                print(s, t, val, output)
                print("                                                    ")
        print("Invest list is  ",invest)
print("prediction starts..")
file = 'nasdaq_screener_1664091848249.csv'
df = pd.read_csv(str(BASE_DIR)+'/data'+'/'+file)
stlist = df['Symbol'].iloc[0:300]

y_file = 'current.csv'
yesterday_f = pd.read_csv(str(BASE_DIR)+'/data'+'/'+y_file)
yesterday = yesterday_f['Price'].iloc[0:300]
pred(yesterday, stlist)