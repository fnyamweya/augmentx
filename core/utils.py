import pandas as pd
from PIL import Image
import os

def validate_data(data, data_type):
    """
    Validate the data before applying augmentation.
    
    Args:
        data: The data to validate.
        data_type: Type of data ('tabular', 'image', 'text').
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if data_type == 'tabular':
        return isinstance(data, pd.DataFrame)
    elif data_type == 'image':
        return isinstance(data, Image.Image)
    elif data_type == 'text':
        return isinstance(data, str)
    return False

def load_image(image_path):
    """
    Load an image from a file path.
    
    Args:
        image_path: Path to the image file.
    
    Returns:
        Image object or None if invalid.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    return Image.open(image_path)

def save_image(image, save_path):
    """
    Save an image to the specified file path.
    
    Args:
        image: Image object to save.
        save_path: Destination file path.
    """
    image.save(save_path)

def summarize_dataframe(df):
    """
    Summarize a pandas DataFrame, showing key statistics.
    
    Args:
        df: pandas DataFrame to summarize.
    
    Returns:
        Summary statistics as a pandas DataFrame.
    """
    return df.describe()
