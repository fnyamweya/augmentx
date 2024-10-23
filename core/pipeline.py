def apply_pipeline(data, augmentations):
    """
    Apply a sequence of augmentations to the data.
    
    Args:
        data: The data (tabular, image, or text) to augment.
        augmentations: A list of augmentation functions to apply.
        
    Returns:
        Augmented data after applying the augmentation pipeline.
    """
    augmented_data = data
    
    for augmentation in augmentations:
        augmented_data = augmentation(augmented_data)
    
    return augmented_data
