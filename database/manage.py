import sqlite3
from loader.socios.utils import ID,ACC,NAME,IS_OK,VAR





def are_all_null(*args):
    return all(arg==None for arg in args)

def get_actual_data(*,key,dict):

    if key==0: 
        _id = dict[ID]
        try:
            if not _id[IS_OK]: return None
        except:
            return None
        name = dict[NAME]
        acc= dict[ACC]
        name = name[VAR]
        new_acc = (acc[0][VAR],acc[1][VAR])
        _id = _id[VAR]
        return {NAME:name,ID:_id,ACC:new_acc}  if not are_all_null(name , _id  ,new_acc[0] ,new_acc[1]) else None



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
    NAME TEXT,CEDULA_CHAR TEXT,CEDULA TEXT ,ACCOUNT_ONE TEXT ,ACCOUNT_TWO TEXT 
    )""")
    socio_key = 0
    for socio in socios:
        try:
            data = get_actual_data(dict=socio,key=socio_key)
            
            if data is not None:
                cur.execute(""" INSERT INTO socios(NAME,CEDULA_CHAR,CEDULA,ACCOUNT_ONE,ACCOUNT_TWO)
                VALUES(?,?,?,?,?)
                """,(data[NAME] , data[ID][0],data[ID][1],data[ACC][0],data[ACC][1]))

        except sqlite3.Error as e:
            print(e)
    conn.commit()

