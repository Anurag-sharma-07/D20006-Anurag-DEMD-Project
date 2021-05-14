import uvicorn
from fastapi import FastAPI
import pickle
import os
import pandas as pd
import numpy as np
from datetime import datetime


app = FastAPI()


# Load model
pickle_file_open = open("ARIMA-Model-TSF.pkl", "rb") # open pickle file in read mode
ARIMA_Model = pickle.load(pickle_file_open) # to load the pickle file

# loading dataset 
df = pd.read_csv("ICICI-STOCK-PRICE.csv")

#Train - Test Split
icici_stock_close = df[['Date','Close Price']]


@app.get('/')
def home():
    return "Welcome to FastAPI input n-number of days and you will get ICICI stock price for n number of days from 05-May-2021"


@app.post('/predict')
def ICICI_Stock_price(date:int):
    
    pred_frcst1 = ARIMA_Model.predict(n_periods=date)
    #pred_frcst1.columns = ['Predicted_close_price']
    
    result=str(pred_frcst1)
    return (f" predicted stock price for  ICICI next {date} days from 05-May-2021 are INR {result}")
    


if __name__=="__main__":
    #port = int(os.environ.get("PORT",8000))
    uvicorn.run(app, host='127.0.0.1', port=5000)