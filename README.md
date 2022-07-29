# stock-prediction
stock prediction and deployment on AWS
Use this curl command to get the prediction:
    curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"ticker":"MSFT", "days":7}' \
    http://54.193.94.113:8000/predict