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


# with open("fileName.json", "r") as f:
#     json_data = json.loads(f.read())
# bot: Body = Body(**json_data)
#
# print(bot.model_dump_json(indent=4))

with open("MMGPoliceLoadout.json", "r") as f:
    json_data = json.loads(f.read())
bot: Bot = Bot(**json_data)


# for item in bot.InventoryCargo:
#     print (item.ClassName)


# for item in bot.InventoryAttachments:
#     print (item)

# print(bot)
# print(bot.model_dump_json(indent=4))







# CARGO_ITEMS=0
# def add_cargo_iyem():
#     CARGO_ITEMS =+ 1
#
#
# add_cargo_item = [{'ClassName': item.ClassName, 'Chance': item.Chance} for item in bot.InventoryCargo]
# print(add_cargo_item)
#
#
# st.header('BotCargo', divider='rainbow')
# dfColumns = st.columns(5)
# for item in add_cargo_item:
#     dfColumns[0].button('Remove', on_click=add_cargo_iyem)
#     dfColumns[1].text_input('ClassName', value=item.get('ClassName'))
#     # dfColumns[1].number_input(value=item.get('Chance'), label='Chance', key=f"{item.ClassName}Chance")
#
# # st.button('Add', on_click=add_cargo_iyem)
#

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
    row_columns = row_container.columns([5,2,2,2,2,1])
    class_name = row_columns[0].text_input("Class Name", key=f"class_name_{row_id}")
    chans = row_columns[1].number_input("Chans", step=1, key=f"chans_{row_id}", value=1, )
    QuantityMin = row_columns[2].number_input("QuantityMin", step=1, key=f"QuantityMin_{row_id}", value=0)
    QuantityMax = row_columns[3].number_input("QuantityMax", step=1, key=f"QuantityMax_{row_id}", value=0)
    HealthMin = row_columns[4].number_input("HealthMin", step=0.1, key=f"HealthMin_{row_id}", value=0)
    HealthyMax = row_columns[5].number_input("HealthMax", step=0.1, key=f"HealthMax_{row_id}", value=0)
    row_columns[6].button(f"🗑️", key=f"del_{row_id}", on_click=remove_row, args=[row_id])

    return {"class_name": class_name, "chans": chans, "QuantityMin": QuantityMin, "QuantityMax":QuantityMax,
            "HealthMin":HealthMin, "HealthyMax": HealthyMax}


st.title("Item Inventory")

for row in st.session_state["rows"]:
    row_data = generate_row(row)
    rows_collection.append(row_data)

menu = st.columns(2)

with menu[0]:
    st.button("Add Item", on_click=add_row)

