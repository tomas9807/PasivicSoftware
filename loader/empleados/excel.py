
from ..meta import ID,VAR,IS_OK

from . import utils
import pandas as pd





def get_ids(row,patterns): 
    return utils.is_id(row[patterns[ID]])

def get_date(file_name,key):
    return utils.get_date_from_filename(file_name,key)
   





    
    


    

          
            
