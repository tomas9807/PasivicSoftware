
#HEAD_DATE = date.strftime('%d%m%y')
from ..into import from_database
from .. import data_utils 


import traceback
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




def get_content(meta,cur,key_str,identifier_str,date_str):
    selected_socios = from_database.get_selected_socios(cur,key_str)
    
    for socio in selected_socios:
        _id = socio['id']
        mov = from_database.get_mov_from_socio(cur,key_str,identifier_str,date_str,_id)[0][date_str]
        if mov:
            nacionalidad = socio['cedula_char']
            cedula = socio['cedula']
            account_one = socio['ACCOUNT_ONE']
            account_two = socio['account_two']
            full_acc = str(account_one if not account_two else account_one+account_two).replace('-','')

            #here goes final variables
            cedula = apply_zeros(cedula,meta.LEN_CEDULA)
            mov = apply_zeros(round_decimal_two(mov),meta.LEN_MOV_INDIV)
            tipo_mov = meta.tipo_mov["APORTE"]

            one_line_content = apply_zeros(''.join((
                meta.CONST,nacionalidad,cedula,tipo_mov,full_acc,meta.ZEROS_CONTENT,mov
            )),meta.LEN_HEAD,left=False)
            if not len(one_line_content)==60:
                idx = selected_socios.index(socio) +1 
                raise Exception(f'Line {idx} surpassed 60 length')
            yield one_line_content

        




   
    # for person in data:
    #     print(person)
    





def make_file(
    meta,cur,identifier_str,key_str,pardir,HEAD_DATE,date_str,n_socios
    ): 
    try:
        with open(f'{pardir}/{date_str}.txt','a') as f:

            sum_of_movs = from_database.get_sum_from_fields(cur,key_str,identifier_str,data_utils.get_date_fields(meta,key_str,'+'))

            sum_of_movs = apply_zeros(round_decimal_two(sum_of_movs[0]["mov_sum"]),meta.LEN_MONTO_TOTAL)
           
            HEAD_LINE = apply_zeros(
                ''.join((meta.HEAD_CONST,meta.FONDO,HEAD_DATE, n_socios,sum_of_movs,meta.NUM_OFFICINA)),
                meta.LEN_HEAD,
                left=False,
            )

            if not len(HEAD_LINE)==60:
                raise Exception('Head line surpassed 60 length')

            f.write(HEAD_LINE + '\n')

            for content_line in get_content(meta,cur,key_str,identifier_str,date_str):
                f.write(content_line + '\n')

    except Exception as e:
        print(traceback.format_exc())
        print(f'In file {date_str}.txt : {e}')
    







    
