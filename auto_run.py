from pyexpat import model
#import schedule
from model import *
#import time
import pandas as pd
def auto(stlist):


    for t in stlist:

        parser = argparse.ArgumentParser(description='Predict')
        parser.add_argument('--ticker', type=str, default=t, help='Stock Ticker')
        parser.add_argument('--days', type=int, default=7, help='Number of days to predict')
        args = parser.parse_args()
        train(args.ticker)
        #time.sleep(5)
file = 'nasdaq_screener_1664091848249.csv'
df = pd.read_csv(str(BASE_DIR)+'/data'+'/'+file)
stlist = df['Symbol'].iloc[0:300]

# clear previous day's price in current.csv file
filed_names = ['Symbol','Price']
with open(str(BASE_DIR)+'/data/current.csv', 'a') as csv_file:
    csv_file.truncate()
    writer_row = csv.writer(csv_file)
    writer_row.writerow(filed_names)
csv_file.close()
# train the model with new incoming data and save the yesterday's price in current csv file.
auto(stlist)
#schedule model update everyday midnight
#schedule.every().day.at("00:00").do(auto)
#schedule.every(2).minutes.do(auto(stlist))
# Loop so that the scheduling task
# keeps on running all time.
#while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    #schedule.run_pending()
    #time.sleep(1)