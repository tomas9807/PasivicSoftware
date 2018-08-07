
from pprint import pprint
import traceback


import pandas as pd

from . import utils

from database.manage import insert_socios










def evaluate_row_pattern(row,patterns):  #returns the patternsition of names,id numbers,accounts numbers,etc
   
        #extract values from the sheet
    
    name = utils.is_name(row[patterns[utils.NAME]]) 
    _id = utils.is_id(row[patterns[utils.ID]])
    acc = (utils.is_account(row[patterns[utils.ACC][0]]),utils.is_account2(row[patterns[utils.ACC][1]]))
        #start validationss
    return {utils.NAME:name,utils.ID:_id,utils.ACC:acc}

def evaluate_rows(df,patterns={utils.NAME:1,utils.ID:3,utils.ACC:(5,6)}):
    for row in  df.itertuples():
            try:
              yield evaluate_row_pattern(row=row,patterns=patterns) # here i should warn that there are some problems with some cells
            
            except TypeError:
                print(traceback.format_exc())
                break 



def read_file(path):
    
    df = pd.read_excel(path, header=None,na_filter=False) #reading excel file
    insert_socios(evaluate_rows(df))
        



    
    


    

          
            
