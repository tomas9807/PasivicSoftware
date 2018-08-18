import sqlite3
import os
import traceback


def insert_mov(meta,cur,key,indentifier,date,socio_id,mov):
    
    if key==meta.OBREROS:
        if indentifier==meta.APORTE:
            data = cur.execute(f"""
              SELECT socio_id FROM movimientos_obreros_aportes where socio_id={socio_id[0]}
            """)

            if not data.fetchone():

                cur.execute(f""" 
                INSERT INTO movimientos_obreros_aportes  (socio_id,semana_{date})
                VALUES(?,?)
                """,(socio_id[0],mov,))
            else:

                cur.execute(f""" 
                UPDATE movimientos_obreros_aportes SET semana_{date}=? WHERE socio_id=?

                """,(mov,socio_id[0]))






def get_semanas_fields(meta):
    return ','.join(f'semana_{semana_num+1} TEXT' for semana_num in range(meta.SEMANAS))



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

    

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS movimientos_obreros_aportes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER UNIQUE,
    {get_semanas_fields(meta)},
    FOREIGN KEY(socio_id) REFERENCES socios(id)
    )""")



    cur.execute("""
    CREATE TABLE IF NOT EXISTS movimientos_empleados_aportes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER,
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
 

