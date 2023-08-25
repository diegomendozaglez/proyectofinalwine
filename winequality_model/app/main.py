## LOGGING

import logging
import subprocess
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from models.models import Mobile
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse

PIPELINE_NAME = 'RFC'
PIPELINE_SAVE_FILE = f'models_ml/{PIPELINE_NAME}_output.pkl'
TRAIN_MAIN_DIR = 'winemodel.py'


logger = logging.getLogger(__name__)  # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG)  # Configuramos el nivel de logging
formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')  # Creamos el formato
# Indicamos el nombre del archivo
file_handler = logging.FileHandler('main_api.log')
file_handler.setFormatter(formatter)  # Configuramos el formato
logger.addHandler(file_handler)  # Agregamos el archivo


app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    logger.info("Mobile classifier is all ready to go!")
    return 'Mobile classifier is all ready to go!'


@app.post('/predict')
def extract_name(mobile_features: Mobile):
    try:
        predictor = ModelPredictor(PIPELINE_SAVE_FILE)
        X = {'fixed_acidity': [wine_features.fixed_acidity],
             'volatile_acidity': [wine_features.volatile_acidity],
             'clock_speed': [wine_features.clock_speed],
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
        logger.info(f"Predicted result: {prediction}")
        return JSONResponse(f"Predicted Price Range: {prediction}")
    except Exception as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error: {str(e)}")
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
            ['python', TRAIN_MAIN_DIR],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        if result.returncode == 0:
            message = "Model training script executed successfully"
            response_text = result.stdout
        else:
            message = f"An error occurred: {result.stderr}"
            response_text = result.stderr

        response_data = {
            "message": message,
            "response_text": response_text
        }
        logger.info(f"Succesfully runned: {response_data}")
        return JSONResponse(content=response_data)
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e}\n{e.stderr}"
        logger.error(error_message)
        return JSONResponse(content={"error": error_message}, status_code=500)
