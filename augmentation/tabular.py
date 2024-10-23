import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Synthetic Data Generation (SMOTE)
def augment_smote(X, y, sampling_strategy='auto'):
    smote = SMOTE(sampling_strategy=sampling_strategy)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return X_resampled, y_resampled

# Noise Injection
def inject_noise(data, noise_level=0.01):
    noisy_data = data.copy()
    noise = np.random.randn(*data.shape) * noise_level
    noisy_data += noise
    return noisy_data

# Outlier Manipulation: Remove or Amplify
def handle_outliers(data, method='remove', threshold=3):
    z_scores = np.abs((data - data.mean()) / data.std())
    if method == 'remove':
        return data[(z_scores < threshold).all(axis=1)]
    elif method == 'amplify':
        data[z_scores > threshold] *= 1.5
        return data

# Feature Scaling (optional for numerical features)
def scale_features(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

# Example usage: augmenting a tabular dataset
def augment_tabular(data, target_column, smote=False, noise=False, outliers=False):
    X = data.drop(columns=[target_column])
    y = data[target_column]

    if smote:
        X, y = augment_smote(X, y)
    if noise:
        X = inject_noise(X)
    if outliers:
        X = handle_outliers(X)
    
    return pd.DataFrame(X, columns=data.columns.drop(target_column)), y
