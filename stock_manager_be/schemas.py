from pydantic import BaseModel
from typing import Optional

# Common Inventory logic
class InventoryBase(BaseModel):
    name: str
    category: str
    stock_count: int

class InventoryCreate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    id: int
    class Config:
        from_attributes = True # Allows Pydantic to read SQLAlchemy models

# User schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str