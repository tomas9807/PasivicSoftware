from .meta import SOCIOS,EMPLEADOS,OBREROS,get_default_patterns

import pandas as pd

import pandas as pd



from database.manage import insert_socios












def get_data_excel(df,patterns,key):

    if key==SOCIOS: 
        from .socios.excel import evaluate_row_pattern
        func = evaluate_row_pattern
    else: 
        from .empleados.excel import get_ids
        func = get_ids

        
    for row in  df.itertuples():

        try:
            

            yield func(row=row,patterns=patterns) # here i should warn that there are some problems with some cells
            
        except TypeError:
            print(traceback.format_exc())
            break 



def read_file(path,patterns,key):
    
    df = pd.read_excel(path, header=None,na_filter=False) #reading excel file
    insert_socios(get_data_excel(df=df,patterns=patterns,key=key),key)
   
