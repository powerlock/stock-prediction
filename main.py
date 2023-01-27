

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from model import predict, convert
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str
    days: int

class StockOut(StockIn):
    forecast: dict
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker
    days = payload.days

    prediction_list = predict(ticker, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "ticker": ticker, 
        "days": days,
        "forecast": convert(prediction_list)}
    return response_object

""" 
from auto_run import *
if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
    for st in stlist:
        data = yf.download(st, TODAY.strftime("%Y-%m-%d"), TODAY.strftime("%Y-%m-%d"))
        prediction_list = predict(ticker=args.ticker, days=args.days)
        output = convert(prediction_list)
        print(output)
        val = (data.y.iloc[-1] - next(iter(output.values())))/data.y.iloc[-1]
        print("change percentage: ", 100*val)
        if abs(val) > 0.15:
            print("****************5 percent more increase, High chance to invest*************") """
