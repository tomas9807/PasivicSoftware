import sqlite3
def connect():
    try:
        # if os.path.isfile('db.sqlite3'): os.remove('db.sqlite3')
        conn = sqlite3.connect('database/db.sqlite3')
        return conn
    except sqlite3.Error as e:
        print(e)



def get_date_fields(meta,key_str,separator=None):
    if separator is None: separator = ','
    num_fields = meta.SEMANAS if key_str=='obreros' else meta.QUINCENAS
    date_type = 'semanas' if key_str=='obreros' else 'quincenas'
    return f'{separator}'.join(f'{date_type}_{num+1}' for num in range(num_fields))
    
def are_all_null(*args):
    return all(arg==None for arg in args)

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
        {get_date_fields(meta,key_str)},
        FOREIGN KEY(socio_id) REFERENCES socios(id)
        )""")    