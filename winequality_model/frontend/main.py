import logging

import requests
from fastapi import Body, FastAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("frontend.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream


app = FastAPI()

# ML model prediction function using the prediction API request


def predict_mobilepc(input):
    url3 = "http://app.docker:8000/predict"

    response = requests.post(url3, json=input)
    response = response.text

    return response


@app.get("/")
def read_root():
    logger.info("Front-end is all ready to go!")
    return "Front-end is all ready to go!"


@app.post("/classify")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_mobilepc(payload)
    logger.debug(f"Prediction: {response}")
    return {"response": response}


@app.get("/healthcheck")
async def v1_healhcheck():
    url3 = "http://app.docker:8000/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response
