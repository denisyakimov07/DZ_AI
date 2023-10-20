import json
import streamlit as st
from typing import List, Optional, Union
import uuid
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

class WeaponeInventoryBody(BaseModel):
    SlotName: str
    Items: List[Clothing]

class Weapone(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[WeaponeInventoryBody]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List[str]
    Sets: List[str]

class Bot(BaseModel):
    ClassName: str
    Chance: float
    Quantity: Quantity
    Health: List[Health]
    InventoryAttachments: List[BotInventoryBody]
    InventoryCargo: List[Item]
    ConstructionPartsBuilt: List[str]
    Sets: List[Weapone]








st.set_page_config(layout="wide")
if "rows" not in st.session_state:
    st.session_state["rows"] = []

rows_collection = []

def add_row():
    element_id = uuid.uuid4()
    st.session_state["rows"].append(str(element_id))
    print(rows_collection)


def remove_row(row_id):
    st.session_state["rows"].remove(str(row_id))

def generate_row(row_id):
    row_container = st.empty()
    row_columns = row_container.columns([5,1,1,1,1,1,1])
    class_name = row_columns[0].text_input("Class Name", key=f"class_name_{row_id}")
    chans = row_columns[1].number_input("Chans", step=0.1, key=f"chans_{row_id}", value=1.0, min_value=0.0, max_value=1.0)
    QuantityMin = row_columns[2].number_input("Quantity Min", step=0.1, key=f"QuantityMin_{row_id}", value=0.0, min_value=0.0, max_value=1.0)
    QuantityMax = row_columns[3].number_input("Quantity Max", step=0.1, key=f"QuantityMax_{row_id}", value=0.0,min_value=0.0, max_value=1.0)
    HealthMin = row_columns[4].number_input("Health Min", step=0.1, key=f"HealthMin_{row_id}", value=0.0, min_value=0.0, max_value=1.0)
    HealthyMax = row_columns[5].number_input("Health Max", step=0.1, key=f"HealthMax_{row_id}", value=0.0, min_value=0.0, max_value=1.0)
    row_columns[6].button(f"🗑️", key=f"del_{row_id}", on_click=remove_row, args=[row_id])
    return {"class_name": class_name, "chans": chans, "QuantityMin": QuantityMin, "QuantityMax":QuantityMax,
            "HealthMin":HealthMin, "HealthyMax": HealthyMax}


st.title("Bot Cargo Inventory")

for row in st.session_state["rows"]:
    row_data = generate_row(row)
    rows_collection.append(row_data)

menu = st.columns(2)

with menu[0]:
    st.button("Add Item", on_click=add_row)

