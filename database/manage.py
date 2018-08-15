import sqlite3
from loader.meta import ID,ACC,NAME,IS_OK,VAR,SOCIOS,EMPLEADOS,OBREROS,SEMANAS_COUNT_PRECISE,QUINCENAS_COUNT_P,APORTE,DEDUC
import os
import traceback


def insert_mov(cur,key,indentifier,date,socio_id,mov):
    
    if key==OBREROS:
        if indentifier==APORTE:
            cur.execute(f""" 
            UPDARE movimientos_obreros_aportes SET semana_{date}=? WHERE socio_id=?
            """,mov,socio_id)





def get_semanas_fields():
    return ','.join(f'semana_{semana_num} TEXT' for semana_num in range(SEMANAS_COUNT_PRECISE))



def are_all_null(*args):
    return all(arg==None for arg in args)

def get_actual_data(*,key,dict):
    
    try:
        if key==SOCIOS:
            _id = dict[ID] 
            if not _id[IS_OK]: return None
        else:
            _id = dict[VAR]
            if not dict[IS_OK]: return None
    except:
        print(traceback.format_exc())

        return None
    if key==SOCIOS: 

        name = dict[NAME]
        acc= dict[ACC]
        name = name[VAR]
        new_acc = (acc[0][VAR],acc[1][VAR])
        _id = _id[VAR]
        return {NAME:name,ID:_id,ACC:new_acc}  if not are_all_null(name , _id  ,new_acc[0] ,new_acc[1]) else None
    else:
        return _id
        


def connect():
    try:
        # if os.path.isfile('db.sqlite3'): os.remove('db.sqlite3')
        conn = sqlite3.connect('db.sqlite3')
        return conn
    except sqlite3.Error as e:
        print(e)

def check_data_base(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS socios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cedula_char TEXT,
    cedula text ,ACCOUNT_ONE TEXT ,
    account_two TEXT,
    empleado INT DEFAULT 0 ,
    obrero INT DEFAULT 0
    )""")

    

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS movimientos_obreros_aportes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER,
    {get_semanas_fields()},
    FOREIGN KEY(socio_id) REFERENCES socios(id)
    )""")



    cur.execute("""
    CREATE TABLE IF NOT EXISTS movimientos_empleados_aportes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER,
    FOREIGN KEY(socio_id) REFERENCES socios(id)
    )""")



def insert_socios(socio,key,cur):
    

     
    # cur.execute("""CREATE TABLE IF NOT EXISTS socioss(ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # NAME TEXT NOT NULL,CEDULA TEXT NOT NULL,ACCOUNT_ONE TEXT NOT NULL,ACCOUNT_TWO TEXT 
    # )""")
    
    if not key==SOCIOS:
        to_whom = 'empleado' if key==EMPLEADOS else 'obrero'
    try:
        data = get_actual_data(dict=socio,key=key)
        if data is not None:
            if key==SOCIOS:
                cur.execute(""" INSERT INTO socios(NAME,CEDULA_CHAR,CEDULA,ACCOUNT_ONE,ACCOUNT_TWO)
                VALUES(?,?,?,?,?)
                """,(data[NAME] , data[ID][0],data[ID][1],data[ACC][0],data[ACC][1]))
            
            else:
                # if key==EMPLEADOS:

                #     cur.execute(f""" 
                #     SELECT CEDULA,NAME FROM socios LIMIT 2
                #     """,)
                #     cedulas = cur.fetchall()
                #     d = str(data)
                #     if d in cedulas:
                #         print(True)
                #     else:
                #         print(d,' - ',list(cedulas))
                        
                

                
                cur.execute(f""" 
                UPDATE socios SET {to_whom} =? WHERE CEDULA=? 
                """,(1,data))
                
    except sqlite3.Error as e:
        print(e)
 

