import sqlite3
from loader.socios.utils import ID,ACC,NAME,IS_OK,VAR

def are_all_null(*args):
    return all(arg==None for arg in args)

def evaluate_errors(dict,key):
    if key=='socios':
        name = dict.get(NAME)
        _id = dict.get(ID)
        acc = dict.get(ACC)
        is_ok = name[IS_OK] and _id[IS_OK] and acc[0][IS_OK] and acc[1][IS_OK]
        name = name[VAR]
        _id = ''.join(_id[VAR]) if  _id[VAR] is not None else None
        new_acc = []
        new_acc.append(acc[0][VAR])
        new_acc.append(acc[1][VAR])
        dict = {NAME:name,ID:_id,ACC:new_acc,IS_OK:is_ok}



def connect():
    try:
        conn = sqlite3.connect('db.sqlite3')
        return conn
    except sqlite3.Error as e:
        print(e)

def insert_socios(socios):
    conn = connect()
    cur = conn.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS socios(ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # NAME TEXT NOT NULL,CEDULA TEXT NOT NULL,ACCOUNT_ONE TEXT NOT NULL,ACCOUNT_TWO TEXT 
    # )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS socios(ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,CEDULA TEXT ,ACCOUNT_ONE TEXT ,ACCOUNT_TWO TEXT 
    )""")
    for socio in socios:
        name = socio[NAME]
        _id = socio[ID]
        acc= socio[ACC]
        try:
            if not are_all_null(name , _id  ,acc[0] ,acc[1]):
                def get_socios_asdict(name,_id,acc): 

    
    

                cur.execute(""" INSERT INTO socios(NAME,CEDULA,ACCOUNT_ONE,ACCOUNT_TWO)
                VALUES(?,?,?,?)
                """,(name , _id  ,acc[0] ,acc[1]))

        except sqlite3.Error as e:
            print(e)
            print(name,_id,acc)
    conn.commit()

