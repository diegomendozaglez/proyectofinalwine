from pydantic import BaseModel


class wine(BaseModel):
    """
    Represents a mobile phone with various attributes.

    Attributes:

        fixed_acidity (float): Placeholder for fixed_acidity attribute
        volatile_acidity (float): Placeholder for volatile_acidity attribute
        citric_acid (float): Placeholder for citric_acid attribute
        residual sugar (float): Placeholder for residual_sugar attribute
        chlorides (float): Placeholder for chlorides attribute
        free_sulfur_dioxide (float): Placeholder for free_sulfur_dioxide attribute
        total_sulfur_dioxide (float): Placeholder for total_sulfur_dioxide attribute
        density (float): Placeholder for density attribute
        pH (float): Placeholder for pH attribute
        sulphates (float): Placeholder for sulphates attribute
        alcohol (float): Placeholder for alcohol attribute
        """

    fixed acidity": float
    volatile acidity": float
    citric acid": float
    residual sugar": float
    chlorides": float
    free sulfur dioxide": float
    total sulfur dioxide": float
    density: float
    pH": float
    sulphates: float
    alcohol: float
