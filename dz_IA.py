import json
from dataclasses import Field
from typing import List, Optional, Union

from pydantic import BaseModel


class Quantity(BaseModel):
    Min: float
    Max: float


class Health(BaseModel):
    Min: float
    Max: float
    Zone: str = Optional


class ItemAttachmentsToAttachment(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[str]
    InventoryCargo: List[str]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]


class ItemAttachments(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[ItemAttachmentsToAttachment]
    InventoryCargo: List[ItemAttachmentsToAttachment]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]


class ItemBody(BaseModel):
    SlotName: str
    Items: List[ItemAttachments]

class Item(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[ItemAttachments]
    InventoryCargo: List[ItemBody]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]


class ClothingAttachmentsBody(BaseModel):
    SlotName: str
    Items: List[Item]

class ClothingAttachments(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[ClothingAttachmentsBody]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]

class ClothingBody(BaseModel):
    SlotName: str
    Items: List[ClothingAttachments]

class Clothing(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[ClothingBody]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]


class BotInventoryBody(BaseModel):
    SlotName: str
    Items: List[Clothing]


class Bot(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[BotInventoryBody]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]


# with open("fileName.json", "r") as f:
#     json_data = json.loads(f.read())
# bot: Body = Body(**json_data)
#
# print(bot.model_dump_json(indent=4))

with open("MMGPoliceLoadout.json", "r") as f:
    json_data = json.loads(f.read())
bot: Bot = Bot(**json_data)

print(bot.model_dump_json(indent=4))
