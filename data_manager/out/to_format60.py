
#HEAD_DATE = date.strftime('%d%m%y')
from ..into import from_database
from .. import data_utils 



def round_decimal_two(str_num):
    return str(round(float(str_num),2))



def apply_0_front(num,nzeros):
    num = str(num)
    length= len(num)
    if length<nzeros:

        offset = nzeros-length
        return ''.join('0' if offset-1<idx else num[idx] for idx in range(5) )




def get_dates_per_row(key_str,rows):
    return (int(date) for date in rows[2:])





def apply_relleno(line_str):
    length = len(line_str)
    if length<60:
        return ''.join(line_str[idx] if idx<length else '0' for idx in range(60))



def make_file(
    meta,cur,identifier_str,key_str,pardir,HEAD_DATE
    ): 

    table = f'movimientos_{key_str}_{identifier_str}'
    sum_of_movs = from_database.get_sum_from_fields(cur,table,data_utils.get_date_fields(meta,key_str,'+'))
    sum_of_movs = apply_0_front(round_decimal_two(sum_of_movs[0][0]),meta.LEN_MONTO_TOTAL)
    n_socios  = apply_0_front(from_database.get_total_num_socios(cur),meta.LEN_SOCIOS)
    head = apply_relleno(''.join((meta.HEAD_CONST,meta.FONDO,HEAD_DATE, n_socios,sum_of_movs,meta.NUM_OFFICINA)))
    print(head)




    
