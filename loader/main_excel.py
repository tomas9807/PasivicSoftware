from .meta import SOCIOS,EMPLEADOS,OBREROS,get_default_patterns,APORTE_DEDUC,APORTE,DEDUC,MOVIMIENTOS

import pandas as pd

import pandas as pd

import traceback

from database.manage import insert_socios,connect,check_data_base,insert_socios,insert_mov
from empleados.excel import get_date,get_ids
from .socios.excel import evaluate_row_pattern








def get_data_excel(df,patterns,key,func):
     for row in  df.itertuples():

        try:

            yield func(row=row,patterns=patterns) # here i should warn that there are some problems with some cells
            
        except TypeError:
            print(traceback.format_exc())
            break 

   
def check_date(cur,path,key,indentifier,list_of_files): #identitifier means aporte or deduccion
    for file in list_of_files:
        date = get_date(file_name=file,key=key)
            if date is None:
                return None
            elif isinstance(date,'dict'):
                return None
            else:
                df = pd.read_excel(file, header=None,na_filter=False) 
                #returns like this ('5')
                for row in df.itertuples():
                    _id = row[MOVIMIENTOS[ID]]
                    
                    mov = row[MOVIMIENTOS[APORTE_DEDUC]]

                    data = cur.execute(""" 

                    SELECT id FROM socios WHERE cedula=? LIMIT 1
                    """,_id)
                    socio_id = data.fetchone()
                    if socio_id:
                        insert_mov(cur,key,indentifier,date,socio_id,mov)
                    



                    


                     



            




def fill_database(path,patterns,key):
    
    
    df = pd.read_excel(path, header=None,na_filter=False) 

    if key==SOCIOS: 

        func = evaluate_row_pattern
    else: 
        
        func = get_ids
    conn = connect()
    with conn:
        cur = conn.cursor()   
        check_data_base(cur) 
        for data in get_data_excel(df=df,patterns=patterns,key=key,func=func):
            insert_socios(socio=data,key=key,cur=cur)

   
