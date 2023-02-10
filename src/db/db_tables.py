import sqlite3

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float


metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("price", Float)
)

couriers = Table(
    "couriers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("phone", String(15)),
    
)

def create_db():
    con = sqlite3.connect("cafe.db")

create_db()