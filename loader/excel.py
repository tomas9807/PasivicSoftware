
from pprint import pprint



import pandas as pd
from .utils import get_socios_asdict,ID,NAME,INDEX,ACC,IS_OK
from . import comp

from database.manage import insert_socios
from .profile import profile









def evaluate_row_pattern(row,patterns,list_socios):  #returns the patternsition of names,id numbers,accounts numbers,etc
   
        #extract values from the sheet
    
    name = comp.is_name(row[patterns[NAME]]) 
    _id = comp.is_id(row[patterns[ID]])
    acc = (comp.is_account(row[patterns[ACC][0]]),comp.is_account2(row[patterns[ACC][1]]))
  
        #start validationss
    list_socios.append(get_socios_asdict(name,_id,acc)) 


def read_file(path,patterns={NAME:1,ID:3,ACC:(5,6)}):
    
    df = pd.read_excel(path, header=None,na_filter=False) #reading excel file
    
    list_socios =[]
    for row in  df.itertuples():
        # try:
        #     evaluate_row_pattern(row=row,patterns=patterns,list_socios=list_socios) # here i should warn that there are some problems with some cells
        # except TypeError as e:
        #     print(e)
        #     break 
        evaluate_row_pattern(row=row,patterns=patterns,list_socios=list_socios)
    # insert_socios(list_socios)
        



    
    


    

          
            
