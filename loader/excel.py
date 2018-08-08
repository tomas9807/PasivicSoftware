from .meta import SOCIOS,EMPLEADOS,OBREROS,get_default_patterns

import pandas as pd

import pandas as pd

import traceback

from database.manage import insert_socios,connect,check_data_base












def get_data_excel(df,patterns,key,func):
     for row in  df.itertuples():

        try:

            yield func(row=row,patterns=patterns) # here i should warn that there are some problems with some cells
            
        except TypeError:
            print(traceback.format_exc())
            break 

   


def read_file(path,patterns,key):
    
    
    df = pd.read_excel(path, header=None,na_filter=False) 

    if key==SOCIOS: 
        from .socios.excel import evaluate_row_pattern
        func = evaluate_row_pattern
    else: 
        from .empleados.excel import get_ids
        func = get_ids
    conn = connect()
    with conn:
        cur = conn.cursor()   
        check_data_base(cur) 
        for data in get_data_excel(df=df,patterns=patterns,key=key,func=func):
            
            insert_socios(socio=data,key=key,cur=cur)

   
