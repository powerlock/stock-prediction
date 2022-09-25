from pyexpat import model
#import schedule
from model import *
#import time
import pandas as pd
def auto(stlist):
    #stlist = ['SQ','AZO','TSLA','MSFT','ROKU','NFLX','TXG','ENVX']
    #stlist = ['SQ','NFLX','TSLA']
    #stlist = ['ADBE','ZM','COST','CRM']
    #stlist = ['AI', 'NKLA','OXY','USO', 'XL']
    #stlist = ['QQQ']

    for t in stlist:

        parser = argparse.ArgumentParser(description='Predict')
        parser.add_argument('--ticker', type=str, default=t, help='Stock Ticker')
        parser.add_argument('--days', type=int, default=7, help='Number of days to predict')
        args = parser.parse_args()
        train(args.ticker)
        #time.sleep(5)

df = pd.read_csv(str(BASE_DIR)+'/data'+'/Nasdaq_companylist.csv')
stlist = df['Symbol'].iloc[0:100]
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