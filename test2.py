from typing import List, Optional

from pydantic import BaseModel

class Quantity(BaseModel):
    Min: float
    Max: float

class HealthItem(BaseModel):
    Min: float
    Max: float
    Zone: str

class Item(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity2
    Health: List
    InventoryAttachments: List
    InventoryCargo: List[InventoryCargoItem]
    ConstructionPartsBuilt: Optional[List] = None
    Sets: Optional[List] = None

class Model(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List[Item]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List
    Sets: List[Set]