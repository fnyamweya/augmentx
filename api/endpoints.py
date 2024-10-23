from fastapi import APIRouter, UploadFile, File, Form
from core.pipeline import apply_pipeline
from core.utils import validate_data, load_image
from augmentation.tabular import augment_tabular
from augmentation.image import augment_image
from augmentation.text import augment_text
from api.request_models import TabularAugmentationRequest, ImageAugmentationRequest, TextAugmentationRequest

router = APIRouter()

@router.post("/augment/tabular", summary="Apply tabular data augmentation")
async def augment_tabular_data(request: TabularAugmentationRequest):
    if not validate_data(request.data, "tabular"):
        return {"error": "Invalid tabular data format"}
    
    # Apply augmentation pipeline
    augmented_data, augmented_target = augment_tabular(
        request.data, 
        target_column=request.target_column, 
        smote=request.smote, 
        noise=request.noise, 
        outliers=request.outliers
    )
    
    return {"augmented_data": augmented_data.to_dict(), "augmented_target": augmented_target.tolist()}


@router.post("/augment/image", summary="Apply image augmentation")
async def augment_image_data(file: UploadFile = File(...), rotate: bool = Form(False), flip: bool = Form(False), brightness_contrast: bool = Form(False)):
    image = load_image(file.file)
    
    # Validate image
    if not validate_data(image, "image"):
        return {"error": "Invalid image data"}
    
    # Apply augmentation pipeline
    augmented_image = augment_image(
        image, 
        rotate=rotate, 
        flip=flip, 
        brightness_contrast=brightness_contrast
    )
    
    # Save or process augmented image (for now just return a success message)
    return {"message": "Image augmented successfully"}


@router.post("/augment/text", summary="Apply text data augmentation")
async def augment_text_data(request: TextAugmentationRequest):
    if not validate_data(request.text, "text"):
        return {"error": "Invalid text data"}
    
    # Apply text augmentation pipeline
    augmented_text = augment_text(
        request.text, 
        synonym=request.synonym_replacement, 
        insertion=request.random_insertion, 
        deletion=request.random_deletion, 
        back_translation=request.back_translation
    )
    
    return {"augmented_text": augmented_text}
