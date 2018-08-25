
#HEAD_DATE = date.strftime('%d%m%y')
from ..into import from_database
from .. import data_utils 

def get_dates_per_row(key_str,rows):
    return (int(date) for date in rows[2:])





def apply_relleno(line_str):
    length = len(line_str)
    if length<60:
        return ''.join(line_str[idx] if idx<length else '0' for idx in range(length))



def make_file(
    meta,cur,identifier_str,key_str,pardir,HEAD_DATE,HEAD_CONST='01',CONST='02',FONDO='040013',NUM_OFFICINA='150'
    ): 
    table = f'movimientos_{identifier_str}_{key_str}'
    sum_of_movs = from_database.get_sum_from_field(cur,table,data_utils.get_date_fields(meta,key_str))
    print(sum_of_movs)
    head = apply_relleno(''.join((HEAD_CONST,FONDO,HEAD_DATE,sum_of_movs)))
    print(head)




    
