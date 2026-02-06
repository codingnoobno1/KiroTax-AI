from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
from models.template import TemplateCreate, TemplateResponse
from security.rbac import get_current_user
try:
    from database import get_collection
except:
    from database_mock import get_collection
import uuid

router = APIRouter()

@router.post("/train", response_model=dict)
async def create_template(
    template_data: TemplateCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new template"""
    templates_collection = get_collection("templates")
    
    template_dict = {
        "_id": str(uuid.uuid4()),
        "user_id": current_user["_id"],
        "name": template_data.name,
        "vendor_name": template_data.vendor_name,
        "description": template_data.description,
        "fields": [field.dict() for field in template_data.fields],
        "usage_count": 0,
        "accuracy_score": 0,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    await templates_collection.insert_one(template_dict)
    
    return {
        "id": template_dict["_id"],
        "message": "Template created successfully"
    }

@router.get("", response_model=List[dict])
async def get_templates(
    current_user: dict = Depends(get_current_user)
):
    """Get user's templates"""
    templates_collection = get_collection("templates")
    
    templates = await templates_collection.find({
        "user_id": current_user["_id"]
    }).sort("created_at", -1).to_list(length=100)
    
    return templates

@router.get("/{template_id}", response_model=dict)
async def get_template(
    template_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific template"""
    templates_collection = get_collection("templates")
    
    template = await templates_collection.find_one({
        "_id": template_id,
        "user_id": current_user["_id"]
    })
    
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    return template

@router.delete("/{template_id}")
async def delete_template(
    template_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete a template"""
    templates_collection = get_collection("templates")
    
    result = await templates_collection.delete_one({
        "_id": template_id,
        "user_id": current_user["_id"]
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Template not found")
    
    return {"message": "Template deleted successfully"}
