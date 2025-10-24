from db import engine 
from table import user , address 
from sqlalchemy import insert , select , update , delete , desc


# insert or create user 

def create_user(place:str,email:str):
    with engine.connect() as conn:
        ins = insert(address).values(place=place , email=email) 
        conn.execute(ins)
        conn.commit() 



def create_address(name:str , email:str, password:str):
    with engine.connect() as conn:
        ins = insert(user).values(name=name , email=email, password=password) 
        conn.execute(ins)
        conn.commit() 


def get_user_by_id(id:int):
    with engine.connect() as conn:
        stmt = select(user).where(user.c.id == id)
        # result = conn.execute(stmt).first()
        result = conn.execute(stmt).first()
        return result 


def get_all_data():
    with engine.connect() as conn:
        stmt = select(address)
        result = conn.execute(stmt).all()
        return result 
    

def user_update(id:int,name:str):
    with engine.connect() as conn:
        stmt = update(user).where(user.c.id == id).values(name=name)
        conn.execute(stmt)
        conn.commit()

def user_delete(id:int):
    with engine.connect() as conn:
        stmt = delete(user).where(user.c.id == id)
        conn.execute(stmt)
        conn.commit() 


def user_order_by_name():
    with engine.connect() as conn:
        stmt = select(user).order_by(desc(user.c.name))
        result = conn.execute(stmt).fetchall()
        return result
    


def user_order_by_id():
    with engine.connect() as conn:
        stmt = select(user).order_by(desc(user.c.id))
        result = conn.execute(stmt).fetchall()
        return result