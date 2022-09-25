from pyexpat import model
import schedule
from model import *
import time
def auto():
    #stlist = ['SQ','AZO','TSLA','MSFT','ROKU','NFLX','TXG','ENVX']
    #stlist = ['SQ','NFLX','TSLA']
    #stlist = ['ADBE','ZM','COST','CRM']
    #stlist = ['AI', 'NKLA','OXY','USO', 'XL']
    stlist = ['QQQ']

    for t in stlist:

        parser = argparse.ArgumentParser(description='Predict')
        parser.add_argument('--ticker', type=str, default=t, help='Stock Ticker')
        parser.add_argument('--days', type=int, default=7, help='Number of days to predict')
        args = parser.parse_args()
        print("start training...  ", args.ticker)
        data = train(args.ticker)
        prediction_list = predict(ticker=args.ticker, days=args.days)
        output = convert(prediction_list)
        print(data.tail(1))
        print(output)
        val = (data.y.iloc[-1] - next(iter(output.values())))/data.y.iloc[-1]
        print("change percentage: ", 100*val)
        if abs(val) > 0.15:
            print("****************5 percent more increase, High chance to invest*************")


#schedule model update everyday midnight
#schedule.every().day.at("00:00").do(auto)
schedule.every(2).minutes.do(auto)
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)