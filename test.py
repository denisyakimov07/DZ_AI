from __future__ import annotations

import json
from typing import List, Optional

from pydantic import BaseModel


class Quantity(BaseModel):
    Min: float
    Max: float





class InventoryCargoItem(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class Item1(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List
    InventoryCargo: List[InventoryCargoItem]
    ConstructionPartsBuilt: Optional[List] = None
    Sets: Optional[List] = None


class InventoryAttachment1(BaseModel):
    SlotName: str
    Items: List[Item1]


class Quantity4(BaseModel):
    Min: float
    Max: float


class InventoryCargoItem1(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity4
    Health: List
    InventoryAttachments: List
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class Item(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[HealthItem]
    InventoryAttachments: List[InventoryAttachment1]
    InventoryCargo: List[InventoryCargoItem1]
    ConstructionPartsBuilt: List
    Sets: List


class InventoryAttachment(BaseModel):
    SlotName: str
    Items: List[Item]





class InventoryCargoItem2(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List



class Item4(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class InventoryAttachment4(BaseModel):
    SlotName: str
    Items: List[Item4]


class Item3(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List[InventoryAttachment4]
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class InventoryAttachment3(BaseModel):
    SlotName: str
    Items: List[Item3]


class Item2(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List[InventoryAttachment3]
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class InventoryAttachment2(BaseModel):
    SlotName: str
    Items: List[Item2]


class Quantity10(BaseModel):
    Min: float
    Max: float


class InventoryCargoItem3(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity10
    Health: List
    InventoryAttachments: List
    InventoryCargo: List
    ConstructionPartsBuilt: List
    Sets: List


class Set(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List[InventoryAttachment2]
    InventoryCargo: List[InventoryCargoItem3]
    ConstructionPartsBuilt: List
    Sets: List


class Bot(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List
    InventoryAttachments: List[InventoryAttachment]
    InventoryCargo: List[InventoryCargoItem2]
    ConstructionPartsBuilt: List
    Sets: List[Set]

with open("MMGPoliceLoadout.json", "r") as f:
    json_data = json.loads(f.read())
bot: Bot = Bot(**json_data)

print(bot.model_dump_json(indent=4))
