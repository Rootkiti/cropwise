from typing import Union
from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel


pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

app = FastAPI()

class soil(BaseModel):
    n: float
    p: float
    k:float
    temp:float
    hum:float
    ph:float


@app.post("/")
def recommend(nutr:soil):
    y =pd.DataFrame([{
    'N':nutr.n,
    'P':nutr.p,
    'K':nutr.k,
    'temperature':nutr.temp,
    'humidity':nutr.hum,
    'ph':nutr.ph
    }])   

    result = model.predict(y)[0]
    return {"Recommended Crop": result}