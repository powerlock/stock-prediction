import datetime
from pathlib import Path

import joblib
import pandas as pd
import yfinance as yf
from prophet import Prophet

import argparse
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()


def train(ticker="TSLA"):
    data = yf.download(ticker, "2020-07-01", TODAY.strftime("%Y-%m-%d"))

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Adj Close"]
    df_forecast = df_forecast[["ds", "y"]]
    
    model = Prophet(daily_seasonality=False)
    model.fit(df_forecast)
    #df_cv = cross_validation(model, initial='730 days', period='180 days', horizon = '365 days')
    #df_p = performance_metrics(df_cv)
    #print(df_p.head())

    joblib.dump(model, Path(str(BASE_DIR)+'/model').joinpath(f"{ticker}.joblib"))
    return df_forecast


def predict(ticker="TSLA", days=7):
    model_file = Path(str(BASE_DIR)+'/model').joinpath(f"{ticker}.joblib")
    if not model_file.exists():
        return False

    model = joblib.load(model_file)

    future = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2020-07-01", end=future.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})

    forecast = model.predict(df)

    #model.plot(forecast).savefig(f"{ticker}_plot.png")
    #model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    return forecast.tail(days).to_dict("records")

def convert(prediction_list):
    output = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output[date] = data["trend"]
    return output

""" if __name__ == "__main__":
    stlist = ['SQ','AZO','TSLA','MSFT','ROKU','NFLX','TXG','ENVX']
    #stlist = ['SQ','NFLX','TSLA']
    #stlist = ['ADBE','ZM','COST','CRM']
    #stlist = ['AI', 'NKLA','OXY','USO', 'XL']

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
            print("****************5 percent more increase, High chance to invest*************") """



