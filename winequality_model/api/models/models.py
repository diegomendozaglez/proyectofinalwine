from pydantic import BaseModel


class wine(BaseModel):
    """
    Represents a mobile phone with various attributes.

    Attributes:

        "fixed acidity" (float): Placeholder for "fixed acidity" attribute
        "volatile acidity" (float): Placeholder for "volatile acidity" attribute
        "citric acid" (float): Placeholder for "citric acid" attribute
        "residual sugar" (float): Placeholder for "residual sugar" attribute
        "chlorides" (float): Placeholder for "chlorides" attribute
        "free sulfur dioxide" (float): Placeholder for "free sulfur dioxide" attribute
        "total sulfur dioxide" (float): Placeholder for "total sulfur dioxide" attribute
        "density" (float): Placeholder for "density" attribute
        "pH" (float): Placeholder for "pH" attribute
        "sulphates" (float): Placeholder for "sulphates" attribute
        "alcohol" (float): Placeholder for "alcohol" attribute
        """

    "fixed acidity": float
    "volatile acidity": float
    "citric acid": float
    "residual sugar": float
    "chlorides": float
    "free sulfur dioxide": float
    "total sulfur dioxide": float
    "density": float
    "pH": float
    "sulphates": float
    "alcohol": float
