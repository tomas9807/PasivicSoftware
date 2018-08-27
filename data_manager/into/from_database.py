
from .. import data_utils


def get_table(key_str,identifier_str):
    return f'movimientos_{key_str}_{identifier_str}'
def get_rows(cur,table):
    data = cur.execute(f'SELECT * FROM {table}')
    return data.fetchall()

def get_sum_from_fields(cur,key_str,identifier_str,field):
    table = get_table(key_str,identifier_str)
    data = cur.execute(f'SELECT SUM({field}) FROM {table}')
    return data.fetchall()
    


def get_total_num_socios(cur):
    data = cur.execute(f'SELECT MAX(id) FROM socios')
    return data.fetchone()[0]

def get_selected_socios(cur,key_str):

    data = cur.execute(f'SELECT id,cedula_char,cedula,ACCOUNT_ONE,account_two FROM socios WHERE {key_str[:-1]}=1')
    return data.fetchall()

def get_nonsocios_from_date(cur,key_str,identifier_str,date_str,socio_id):
    table = get_table(key_str,identifier_str)
    data = cur.execute(f'SELECT {date_str} FROM {table} WHERE socio_id=?',(socio_id,))
    return data.fetchall()
        
