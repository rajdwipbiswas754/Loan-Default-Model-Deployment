from fastapi import FastAPI, Request
import json
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

def model_response(input_dict, loc):    
    with open(loc,"rb") as file:
        model = pickle.load(file)
        
    if model.predict(pd.DataFrame([input_dict]))[0] == 0:
        fo = "No"
    else: fo = "Yes"
    return fo

app = FastAPI()
@app.post("/predict")
async def pred(request:Request):
    input_features = await request.json()
    output = model_response(input_features["data"], "./Loan_Default_Model.pkl")
    return {"Will Default":output}