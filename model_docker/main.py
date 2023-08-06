import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Prediction(BaseModel):
    sex_male: int
    smoker_yes: int
    region_northwest: int
    region_southeast: int
    region_southwest: int
    age: int
    bmi: float
    children: int

model = joblib.load('rfr_model.sav')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/predict')
def predict(data:Prediction):
    data = data.dict()
    prediction = model.predict([[data['sex_male'],
                                 data['smoker_yes'],
                                 data['region_northwest'],
                                 data['region_southeast'],
                                 data['region_southwest'],
                                 data['age'],
                                 data['bmi'],
                                 data['children']]])
    return {'cost': prediction[0]}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)