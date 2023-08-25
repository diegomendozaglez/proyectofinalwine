""" Principal module of the model Wine """

import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from train.train_data import WineModelPipeline

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
DATASETS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "data"))

SEED_SPLIT = 42
TRAIN_DATA_FILE = DATASETS_DIR + '\\train.csv'
TEST_DATA_FILE = DATASETS_DIR + '\\test.csv'


TARGET = 'quality'
NUMERICAL_VARS = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                  'chlorides', 'free_sulfur_dioxide', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                  'pH', '	sulphates', 'alcohol']

NUMERICAL_VARS_WITH_NA = ['chlorides','free sulfur dioxide']
NUMERICAL_VARS_T = ['fixed acidity','volatile acidity']

SEED_MODEL = 404

TRAINED_MODEL_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "models"))
PIPELINE_NAME = 'RFC'
PIPELINE_SAVE_FILE = f'\\{PIPELINE_NAME}_output.pkl'
DROPCOL = ['ID']


if __name__ == "__main__":

    # Instantiate the Mobile Price class
    mobile_price_pipeline = WineModelPipeline(seed_model=SEED_MODEL,
                                                numerical_vars=NUMERICAL_VARS,
                                                numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
                                                numerical_vars_t=NUMERICAL_VARS_T)

    # Read data
    train = pd.read_csv(TRAIN_DATA_FILE)
    test = pd.read_csv(TEST_DATA_FILE)

    # Split data

    Y = train[TARGET]
    X = train.drop(TARGET, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0)

    # Instatiate the pipeline model
    RFC_model = wine_model_pipeline.fit_RFC(X_train, y_train)

    y_pred = RFC_model.predict(X_test)

    class_pred = RFC_model.predict(X_test)

    print(
        f'test precision: {precision_score(y_test, class_pred, average="weighted")}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')

    # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(RFC_model, save_path)
    print(f"Model saved in {save_path}")
