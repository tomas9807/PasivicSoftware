
from .. import data_utils


def get_table(key_str,identifier_str):
    return f'movimientos_{key_str}_{identifier_str}'
def get_rows(cur,table):
    data = cur.execute(f'SELECT * FROM {table}')
    return data.fetchall()

def get_sum_from_fields(cur,key_str,identifier_str,field):
    table = get_table(key_str,identifier_str)
    data = cur.execute(f'SELECT SUM({field}) as mov_sum FROM {table}')
    return data.fetchall()
    


def get_total_num_socios(cur):
    data = cur.execute(f'SELECT MAX(id) as max_id FROM socios')

    return data.fetchone()["max_id"]

def get_selected_socios(cur,key_str):

    data = cur.execute(f'SELECT id,cedula_char,cedula,ACCOUNT_ONE,account_two FROM socios WHERE {key_str[:-1]}=1')
    return data.fetchall()

def get_mov_from_socio(cur,key_str,identifier_str,date_str,socio_id):
    table = get_table(key_str,identifier_str)
    data = cur.execute(f'SELECT {date_str} FROM {table} WHERE socio_id=?',(socio_id,))
    return data.fetchall()
        
