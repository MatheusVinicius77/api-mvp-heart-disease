from fastapi import FastAPI
from pydantic import BaseModel
from model.model import __version__, model


class ParamIn(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


app = FastAPI()

@app.get("/")
def home():
    return{"status":"OK", "Model Version":__version__}


@app.post("/predict")
def predict(payload:ParamIn):
    model_input = [list(payload.dict().values())]
    model_output = int(model.predict(model_input)[0])
    return {"diagnostic":model_output}
