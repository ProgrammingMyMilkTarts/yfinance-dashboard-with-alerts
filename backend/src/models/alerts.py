# backend/src/models/alert.py
"""
    What the API expects when a user creates a new alert.
    This is the REQUEST body for POST /api/alerts
    
    Example request:
    {
        "symbol": "BTC-USD",
        "target_price": 50000.00,
        "condition": "above",
        "contact": "user@example.com",
        "notification_method": "email"
    }
"""

from pydantic import BaseModel, field_validator, ValidationInfo,ConfigDict
from datetime import datetime
from typing import Optional

class AlertCreate(BaseModel):
    symbol: str
    target_price: float
    condition: str
    notification_method:str
    contact: str

    @field_validator('condition')
    @classmethod
    def validate_condition(cls, v:str) -> str:
        if v not in ['above','below']:
            raise ValueError("Condition must be above or below")
        return v

    @field_validator('notification_method')
    @classmethod
    def validate_method(cls, v: str) -> str:
        if v not in ['email', 'whatsapp']:
            raise ValueError('notification_method must be "email" or "whatsapp"')
        return v

    @field_validator('contact')
    @classmethod
    def validate_contact(cls, v:str, info:ValidationInfo):
        method = info.data.get('notification_method')

        if method == 'email' and '@' not in v:
            raise ValueError('Invalid email format')
        elif method == 'whatsapp' and not v.startswith('+'):
            raise ValueError('Phone number must start with + (e.g., +123456789)')
        return v

    @field_validator('target_price')
    @classmethod
    def validate_price(cls, v:float):
       if v <= 0:
           raise ValueError("target_price must be greater than 0")
       return v


class AlertResponse(BaseModel):
    #model for retruning alert data

    id: int
    symbol: str
    target_price: float
    condition: str
    contact: str
    notification_method: str
    is_active: bool
    created_at: datetime
    unsubscribe_token: str

    model_config = ConfigDict(from_attributes = True)

class AlertUpdate(BaseModel):
    """Model for updating alert status"""
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
    
