from .meta import SOCIOS,EMPLEADOS,OBREROS,get_default_patterns

import pandas as pd


from pprint import pprint
import traceback


import pandas as pd

from . import utils

from database.manage import insert_socios












def evaluate_rows(df,patterns=get_default_patterns.get[SOCIOS],key):

    if key==SOCIOS: 
        from socios.excel import evaluate_row_pattern
    else: 
        from socios.excel import evaluate_row_pattern

        
    for row in  df.itertuples():

        try:
            

            yield evaluate_row_pattern(row=row,patterns=patterns) # here i should warn that there are some problems with some cells
            
        except TypeError:
            print(traceback.format_exc())
            break 



def read_file(path,key):
    
    df = pd.read_excel(path, header=None,na_filter=False) #reading excel file
    insert_socios(evaluate_rows(df,key))
        