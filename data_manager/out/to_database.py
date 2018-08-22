import sqlite3
import os
import traceback


def get_strs(meta,key,identifier):
    identifier_str = 'aportes' if identifier==meta.APORTE else 'deducciones'
    key_str = 'obreros' if key==meta.OBREROS else 'empleados'
    date = 'semanas' if key==meta.OBREROS else 'quincenas'
    return {key:key_str,identifier:identifier_str,'date':date}


def insert_mov(meta,cur,key,identifier,date,socio_id,mov):
    strs = get_strs(meta,key,identifier)
    mov_strs = 'movimientos'
    data = cur.execute(f"""
        SELECT socio_id FROM {mov_strs}_{strs[key]}_{strs[identifier]} WHERE socio_id={socio_id[0]}
    """)

    if not data.fetchone():

        cur.execute(f""" 
        INSERT INTO {mov_strs}_{strs[key]}_{strs[identifier]}   (socio_id,{strs['date']}_{date})
        VALUES(?,?)
        """,(socio_id[0],mov,))
    else:

        cur.execute(f""" 
        UPDATE {mov_strs}_{strs[key]}_{strs[identifier]}  SET {strs['date']}_{date}=? WHERE socio_id=?

        """,(mov,socio_id[0]))






def get_date_fields(meta,key_str,identifier_str):
    num_fields = meta.SEMANAS if key_str=='obreros' else meta.QUINCENAS
    return ','.join(f'{identifier_str}_{num+1}' for num in range(num_fields))




    



def are_all_null(*args):
    return all(arg==None for arg in args)

def get_actual_data(meta,key,dict):
    
    try:
        if key==meta.SOCIOS:
            _id = dict[meta.ID] 
            if not _id[meta.IS_OK]: return None
        else:
            _id = dict[meta.VAR]
            if not dict[meta.IS_OK]: return None
    except:
        print(traceback.format_exc())

        return None
    if key==meta.SOCIOS: 

        name = dict[meta.NAME]
        acc= dict[meta.ACC]
        name = name[meta.VAR]
        new_acc = (acc[0][meta.VAR],acc[1][meta.VAR])
        _id = _id[meta.VAR]
        return {meta.NAME:name,meta.ID:_id,meta.ACC:new_acc}  if not are_all_null(name , _id  ,new_acc[0] ,new_acc[1]) else None
    else:
        return _id
        


def connect():
    try:
        # if os.path.isfile('db.sqlite3'): os.remove('db.sqlite3')
        conn = sqlite3.connect('database/db.sqlite3')
        return conn
    except sqlite3.Error as e:
        print(e)

def check_data_base(meta,cur):

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
    
    for i in range(4):
        identifier_str = 'aportes' if i%2==0 else 'deducciones'
        key_str = 'obreros' if i<=1 else 'empleados'
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS movimientos_{key_str}_{identifier_str}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        socio_id INTEGER UNIQUE,
        {get_date_fields(meta,key_str,identifier_str)},
        FOREIGN KEY(socio_id) REFERENCES socios(id)
        )""")


def setup_socios(meta,socio,key,cur):
    

     
    # cur.execute("""CREATE TABLE IF NOT EXISTS socioss(ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # NAME TEXT NOT NULL,CEDULA TEXT NOT NULL,ACCOUNT_ONE TEXT NOT NULL,ACCOUNT_TWO TEXT 
    # )""")
    
    if not key==meta.SOCIOS:
        to_whom = 'empleado' if key==meta.EMPLEADOS else 'obrero'
    try:
        data = get_actual_data(meta=meta,dict=socio,key=key)
        if data is not None:
            if key==meta.SOCIOS:
                cur.execute(""" INSERT INTO socios(NAME,CEDULA_CHAR,CEDULA,ACCOUNT_ONE,ACCOUNT_TWO)
                VALUES(?,?,?,?,?)
                """,(data[meta.NAME] , data[meta.ID][0],data[meta.ID][1],data[meta.ACC][0],data[meta.ACC][1]))
            
            else:
                
            
                cur.execute(f""" 
                UPDATE socios SET {to_whom} =? WHERE CEDULA=? 
                """,(1,data))
                
    except sqlite3.Error as e:
        print(e)
 

