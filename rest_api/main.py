import subprocess
import sys


from .models.models import whine
from starlette.responses import JSONResponse
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from predictor.predict import ModelPredictor

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    return 'whine classifier is all ready to go!'


@app.post('/predict')
def extract_name(whine_features: whine):
    try:
        predictor = ModelPredictor(
            "C:/Users/IOR_C/OneDrive/Documentos/GitHub/mlops-whinepc/whinepc/whinepc/models/SVM_output.pkl")
        X = {'fixed acidity': [whine_features.'fixed acidity'],
             'volatile acidity': [whine_features.'volatile acidity'],
             'citric acid': [whine_features.'citric acid'],
             'residual sugar': [whine_features.'residual sugar'],
             'chlorides': [whine_features.'chlorides'],
             'free sulfur dioxide': [whine_features.'free sulfur dioxide'],
             'total sulfur dioxide': [whine_features.'total sulfur dioxide'],
             'density': [whine_features.'density'],
             'pH': [whine_features.'pH'],
             'sulphates': [whine_features.'sulphates'],
             'alcohol': [whine_features.pc]}
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
            ["C:\Users\diego.mendoza\Desktop\WINE\proyectofinalwine\venv3_10\Scripts\python",
             "C:\Users\diego.mendoza\Desktop\WINE\proyectofinalwine\venv3_10\Scripts\whinequality.py"],
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

        return JSONResponse(content=response_data)
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e}\n{e.stderr}"
        return JSONResponse(content={"error": error_message}, status_code=500)


