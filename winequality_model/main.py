"""Main module."""

import os

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from train.train_data import MobilePricePipeline

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
DATASETS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "data"))

SEED_SPLIT = 42
TRAIN_DATA_FILE = DATASETS_DIR + '\\train.csv'
TEST_DATA_FILE = DATASETS_DIR + '\\test.csv'


TARGET = 'price_range'
NUMERICAL_VARS = ['battery_power', 'clock_speed', 'fc', 'int_memory',
                  'm_dep', 'mobile_wt', 'pc', 'px_height', 'px_width',
                  'ram', 'sc_h', 'sc_w', 'talk_time']
CATEGORICAL_VARS = ['blue', 'dual_sim', 'four_g',
                    'n_cores', 'three_g', 'touch_screen', 'wifi']


NUMERICAL_VARS_CAD = ['px_height', 'sc_w']
CATEGORICAL_VARS_OH = ['n_cores']

SEED_MODEL = 404

TRAINED_MODEL_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "models"))
PIPELINE_NAME = 'SVM'
PIPELINE_SAVE_FILE = f'\\{PIPELINE_NAME}_output.pkl'
DROPCOL = ['ID']


if __name__ == "__main__":

    # Instantiate the Mobile Price class
    mobile_price_pipeline = MobilePricePipeline(seed_model=SEED_MODEL,
                                                numerical_vars=NUMERICAL_VARS,
                                                numerical_vars_cad=NUMERICAL_VARS_CAD,
                                                categorical_vars_oh=CATEGORICAL_VARS_OH)

    # Read data
    train = pd.read_csv(TRAIN_DATA_FILE)
    test = pd.read_csv(TEST_DATA_FILE)

    # Split data

    Y = train[TARGET]
    X = train.drop(TARGET, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0)

    # Instatiate the pipeline model
    SVC_model = mobile_price_pipeline.fit_SVC(X_train, y_train)

    y_pred = SVC_model.predict(X_test)

    class_pred = SVC_model.predict(X_test)

    print(
        f'test precision: {precision_score(y_test, class_pred, average="weighted")}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')

    # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(SVC_model, save_path)
    print(f"Model saved in {save_path}")
