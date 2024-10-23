from pydantic import BaseModel
from typing import Optional, List
import pandas as pd

class TabularAugmentationRequest(BaseModel):
    data: pd.DataFrame  # Tabular data as pandas DataFrame
    target_column: str  # The target column for augmentation
    smote: bool = False  # Whether to apply SMOTE
    noise: bool = False  # Whether to inject noise
    outliers: bool = False  # Whether to handle outliers

class ImageAugmentationRequest(BaseModel):
    rotate: Optional[bool] = False  # Apply random rotation
    flip: Optional[bool] = False  # Apply horizontal flip
    brightness_contrast: Optional[bool] = False  # Apply brightness/contrast augmentation

class TextAugmentationRequest(BaseModel):
    text: str  # The text to augment
    synonym_replacement: Optional[bool] = False  # Apply synonym replacement
    random_insertion: Optional[int] = 0  # Number of random words to insert
    random_deletion: Optional[float] = 0.0  # Probability of deleting words
    back_translation: Optional[bool] = False  # Apply back-translation
