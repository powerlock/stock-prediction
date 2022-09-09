# Stock prediction with prophet and yahoo finance
1. Use prophet model for stock prediction.
2. Use Yahoo finanace to download data.
3. Deploy the model on EC2.

## Run FASTAPI on local:
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000

## Steps:
1. Create a vir. env. with requirements.
2. pretrain the model by running python model.py
3. Run main.py with uvicorn
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
4. Do the prediction.

## Stock prediction and deployment on AWS
Use this curl command to get the prediction:

    curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"ticker":"MSFT", "days":7}' \
    http://54.193.94.113:8000/predict
