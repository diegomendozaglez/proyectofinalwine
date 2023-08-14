#!/usr/bin/env python

""" Tests for `wine quality` package."""

import os
import pandas as pd
import numpy
import pytest

from mobilepc.preprocess.preprocess_data import (CFixedValues,
                                                 OutlierFixTransformer)


def test_outlierfix_transform():
    """
    Test function for the OutlierFixTransformer class.

    """

    # Sample DataFrame with only numeric values
    data = {'col1': [10, 200, 30, 30, 500, 900, 700, 300],
            'col2': [50, 100, 150, 200, 250, 300, 350, 400]}
    df = pd.DataFrame(data)

    # Low and Upper limits to compare

    perlow = df.quantile(0.03)
    perupp = df.quantile(0.97)

    # Instantiate the custom transformer with specified variables
    outfix_transf = OutlierFixTransformer()

    # Transform the DataFrame using the custom transformer
    transformed_df = outfix_transf.fit_transform(df)

    # Check if the values are whitin the spected range
    assert all([perlow[x] <= transformed_df[x].min() for x in df.columns]
               ), f"The transformed DataFrame should have values equal or above the minimum values: {perlow}"

    assert all([perupp[x] >= transformed_df[x].max() for x in df.columns]
               ), f"The transformed DataFrame should have values equal or below the maximum values: {perlow}"


def test_custom_value_fixed_transform():
    """
    Test function for the CFixedValues class.

    """

    # Sample DataFrame with only numeric values
    data = {'sc_w': [5, 10, 1.5, 2.0, 2.5, 3, 3.5, 4.0],  # 30
            'px_height': [200, 400, 600, 800, 1000, 1200, 1400, 1600]}
    df = pd.DataFrame(data)

    # Instantiate the custom transformer with specified variables
    custom_val_fix_transf = CFixedValues()

    # Transform the DataFrame using the custom transformer
    transformed_df = custom_val_fix_transf.fit_transform(df)

    # Check if the values are whitin the spected range
    assert 2.5 <= transformed_df['sc_w'].min(
    ), "The column sc_w should have all values equal or above 2.5"

    assert 217 <= transformed_df['px_height'].min(
    ), "The column sc_w should have all values equal or above 217"


def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    csv_file_path = "C:\Users\diego.mendoza\Desktop\WINE\proyectofinalwine\winequality_model\trai\train.csv"

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists is True, f"The CSV file at '{csv_file_path}' does not exist."


def does_pkl_file_exist(file_path):
    """
    Check if a pkl model file exists at the specified path.

    Parameters:
        file_path (str): The path to the pkl file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


def test_pkl_file_existence():
    """
    Test case to check if the pkl file exists.
    """
    # Provide the path to your pkl file that needs to be tested
    pkl_file_path = "C:\Users\diego.mendoza\Desktop\WINE\proyectofinalwine\winequality_model\models\SVM_output.pkl"

    # Call the function to check if the pkl file exists
    file_exists = does_pkl_file_exist(pkl_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists is True, f"The pkl file at '{pkl_file_path}' does not exist."


if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])
