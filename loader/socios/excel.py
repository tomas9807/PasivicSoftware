
from ..meta import NAME,ID,ACC


from . import utils
import pandas as pd




def evaluate_row_pattern(row,patterns):  #returns the patternsition of names,id numbers,accounts numbers,etc
   
        #extract values from the sheet
    
    name = utils.is_name(row[patterns[NAME]]) 
    _id = utils.is_id(row[patterns[ID]])
    acc = (utils.is_account(row[patterns[ACC][0]]),utils.is_account2(row[patterns[ACC][1]]))
        #start validationss
    return {NAME:name,ID:_id,ACC:acc}




    
    


    

          
            
