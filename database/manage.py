import sqlite3
from loader.utils import ID,ACC,NAME


def connect():
    try:
        conn = sqlite3.connect('db')
        return conn
    except sqlite3.Error as e:
        print(e)

def insert_socios(socios):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS socios(ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,CEDULA TEXT NOT NULL,ACCOUNT_ONE TEXT NOT NULL,ACCOUNT_TWO TEXT 
    )""")
    for socio in socios:
        name = socio[NAME]
        _id = socio[ID]
        acc= socio[ACC]
        try:
            
            cur.execute(""" INSERT INTO socios(NAME,CEDULA,ACCOUNT_ONE,ACCOUNT_TWO)
            VALUES(?,?,?,?)
            """,(name if name else "empty", _id if _id else "empty" ,acc[0] if acc else "empty",acc[1] if acc else "empty"))
        except sqlite3.Error as e:
            print(e)
            print(name,_id,acc)
    conn.commit()

