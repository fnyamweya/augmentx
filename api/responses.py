from pydantic import BaseModel
from typing import Any

class AugmentationResponse(BaseModel):
    message: str  # Status message
    augmented_data: Optional[Any] = None  # The augmented data, if applicable
