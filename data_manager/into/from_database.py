
from .. import data_utils

def get_rows(cur,table):
    data = cur.execute(f'SELECT * FROM {table}')
    return data.fetchall()

def get_sum_from_fields(cur,table,field):
    data = cur.execute(f'SELECT SUM({field}) FROM {table}')
    return data.fetchall()
    


def get_total_num_socios(cur):
    data = cur.execute(f'SELECT MAX(id) FROM socios')
    return data.fetchone()[0]
