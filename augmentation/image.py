from PIL import Image, ImageEnhance, ImageFilter
import random
import numpy as np

# Rotate image by a random degree
def random_rotate(image, max_degrees=30):
    degrees = random.uniform(-max_degrees, max_degrees)
    return image.rotate(degrees)

# Flip image horizontally with a 50% chance
def horizontal_flip(image):
    if random.random() > 0.5:
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

# Apply random brightness and contrast
def random_brightness_contrast(image, brightness_factor=0.5, contrast_factor=0.5):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(random.uniform(1 - brightness_factor, 1 + brightness_factor))
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(random.uniform(1 - contrast_factor, 1 + contrast_factor))
    
    return image

# Add random Gaussian noise
def add_gaussian_noise(image, mean=0, stddev=0.1):
    np_image = np.array(image) / 255.0
    noise = np.random.normal(mean, stddev, np_image.shape)
    noisy_image = np.clip(np_image + noise, 0, 1) * 255
    return Image.fromarray(noisy_image.astype('uint8'))

# Blurring (Gaussian)
def apply_blur(image, blur_radius=2):
    return image.filter(ImageFilter.GaussianBlur(blur_radius))

# Image augmentation pipeline
def augment_image(image, rotate=False, flip=False, brightness_contrast=False, noise=False, blur=False):
    if rotate:
        image = random_rotate(image)
    if flip:
        image = horizontal_flip(image)
    if brightness_contrast:
        image = random_brightness_contrast(image)
    if noise:
        image = add_gaussian_noise(image)
    if blur:
        image = apply_blur(image)

    return image
