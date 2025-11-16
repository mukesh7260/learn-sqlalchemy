from db import engine 
from sqlalchemy import Table, Column, Integer, String, MetaData   

metadata = MetaData() 
# user table
user = Table(
    "user", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(50)),
    Column("password", String(50)),
    Column("location", String(100)),
    Column("Qualification", String(50))

) 

address = Table(
    "address", metadata,
    Column("id", Integer, primary_key=True),
    Column("place", String(50)),
    Column("email", String(50))
) 



def create_tables():
    metadata.create_all(engine)