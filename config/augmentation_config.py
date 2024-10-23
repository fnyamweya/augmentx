# Tabular Data Augmentation Configurations
SMOTE_SAMPLING_STRATEGY = "auto"  # Define SMOTE's sampling strategy
NOISE_LEVEL = 0.01                # Noise level for tabular data augmentation
OUTLIER_THRESHOLD = 3             # Z-score threshold for detecting outliers in tabular data

# Image Data Augmentation Configurations
IMAGE_ROTATION_DEGREES = 30        # Maximum degree for random image rotation
BRIGHTNESS_FACTOR = 0.5            # Brightness variation factor for images
CONTRAST_FACTOR = 0.5              # Contrast variation factor for images
BLUR_RADIUS = 2                    # Radius for Gaussian blur
NOISE_STDDEV = 0.1                 # Standard deviation for Gaussian noise added to images

# Text Data Augmentation Configurations
SYNONYM_REPLACEMENT_PROB = 0.1     # Probability of replacing a word with a synonym
WORD_INSERTION_COUNT = 1           # Number of random words to insert in text
WORD_DELETION_PROB = 0.1           # Probability of deleting a word from the text
BACK_TRANSLATION_SRC_LANG = "en"   # Source language for back-translation
BACK_TRANSLATION_TGT_LANG = "fr"   # Target language for back-translation
