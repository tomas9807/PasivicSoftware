
#HEAD_DATE = date.strftime('%d%m%y')
from ..into import from_database
from .. import data_utils 



def round_decimal_two(str_num):
    return str(round(float(str_num),2)).replace(r'.','')



def apply_zeros(num,nzeros,left=True):
    num = str(num)
    length= len(num)
    if length<nzeros:

        offset = nzeros-length
        zero_string = ''.join('0' for i in range(offset))
        return zero_string+num if left else num+zero_string
    return num




def get_dates_per_row(key_str,rows):
    return (int(date) for date in rows[2:])




def get_content(cur,key_str,identifier_str,date_str):
    selected_socios = from_database.get_selected_socios(cur,key_str)
    from pprint import pprint
    for socio in selected_socios:
        xd = from_database.get_nonsocios_from_date(cur,key_str,identifier_str,date_str,socio['id'])
        pprint(xd)




   
    # for person in data:
    #     print(person)
    





def make_file(
    meta,cur,identifier_str,key_str,pardir,HEAD_DATE,date_str
    ): 
    get_content(cur,key_str,identifier_str,date_str)
    
    # with open('test.txt','a') as f:
    #     table = f'movimientos_{key_str}_{identifier_str}'
    #     sum_of_movs = from_database.get_sum_from_fields(cur,table,data_utils.get_date_fields(meta,key_str,'+'))
    #     sum_of_movs = apply_zeros(round_decimal_two(sum_of_movs[0][0]),meta.LEN_MONTO_TOTAL)
    #     print(from_database.get_total_num_socios(cur))
    #     n_socios  = apply_zeros(from_database.get_total_num_socios(cur),meta.LEN_SOCIOS)
    #     HEAD_LINE = apply_zeros(
    #         ''.join((meta.HEAD_CONST,meta.FONDO,HEAD_DATE, n_socios,sum_of_movs,meta.NUM_OFFICINA)),
    #         meta.LEN_HEAD,
    #         left=False,
    #     )
    #     f.write(HEAD_LINE)










    
