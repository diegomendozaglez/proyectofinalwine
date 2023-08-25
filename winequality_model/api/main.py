import os
import subprocess

import pandas as pd
from fastapi import FastAPI, HTTPException, status
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse

from .models.models import Wine

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
GRANDPARENT_DIR = os.path.abspath(os.path.join(PARENT_DIR, ".."))
ROOT_DIR = os.path.abspath(os.path.join(GRANDPARENT_DIR, ".."))
DATASETS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "data"))

PIPELINE_NAME = 'RFC'
PIPELINE_SAVE_FILE = PARENT_DIR + f'\\models\\{PIPELINE_NAME}_output.pkl'

TRAIN_MAIN_DIR = PARENT_DIR + '\\winemodel.py'

PYTHON_DIR = ROOT_DIR + '\\venv\\Scripts\\python'

app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    return 'Wine model is ready!'


@app.post('/predict')
def extract_name(wine_features: Wine:
    try:
        predictor = ModelPredictor(PIPELINE_SAVE_FILE)
        X = {'fixed_acidity': [wine_features.fixed_acidity],
             'volatile_acidity': [wine_features.volatile_acidity],
             'citric_acid': [wine_features.citric_acid],
             'residual_sugar': [wine_features.residual_sugar],
             'chlorides': [wine_features.chlorides],
             'free_sulfur_dioxide': [wine_features.free_sulfur_dioxide],
             'total_sulfur_dioxide': [wine_features.total_sulfur_dioxide],
             'density': [wine_features.density],
             'pH': [wine_features.pH],
             'sulphates': [wine_features.sulphates],
             'alcohol': [wine_features.alcohol]}
        prediction = predictor.predict(pd.DataFrame(X))
        return JSONResponse(f"Predicted Price Range: {prediction}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "result: invalid format",
                "hints": [
                    "Check the numbers",
                    "Must be float",
                    "It is recommended avoid all zeros in petition"
                ],
            },
        ) from e


@app.post("/train-model/")
async def train_model():
    try:
        result = subprocess.run(
            [PYTHON_DIR, TRAIN_MAIN_DIR],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        if result.returncode == 0:
            message = "Model training executed successfully"
            response_text = result.stdout
        else:
            message = f"An error occurred: {result.stderr}"
            response_text = result.stderr

        response_data = {
            "message": message,
            "response_text": response_text
        }

        return JSONResponse(content=response_data)
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e}\n{e.stderr}"
        return JSONResponse(content={"error": error_message}, status_code=500)
