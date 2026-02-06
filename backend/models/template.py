from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class FieldCoordinate(BaseModel):
    x: int
    y: int
    width: int
    height: int

class TemplateField(BaseModel):
    field_name: str
    field_type: str  # text, number, date, table
    coordinates: FieldCoordinate
    keywords: List[str] = []
    regex_pattern: Optional[str] = None

class TemplateBase(BaseModel):
    name: str
    vendor_name: Optional[str] = None
    description: Optional[str] = None

class TemplateCreate(TemplateBase):
    user_id: str
    fields: List[TemplateField]

class TemplateInDB(TemplateBase):
    id: str = Field(alias="_id")
    user_id: str
    fields: List[TemplateField]
    usage_count: int = 0
    accuracy_score: float = 0
    created_at: datetime
    updated_at: datetime
    
    class Config:
        populate_by_name = True

class TemplateResponse(TemplateBase):
    id: str
    fields: List[TemplateField]
    usage_count: int
    accuracy_score: float
    created_at: datetime
    
    class Config:
        from_attributes = True
