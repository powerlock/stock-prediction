# stock-prediction
1. Use prophet model for stock prediction.
2. Use Yahoo finanace to download data.
3. Deploy the model on EC2.

stock prediction and deployment on AWS
Use this curl command to get the prediction:

    curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"ticker":"MSFT", "days":7}' \
    http://54.193.94.113:8000/predict
