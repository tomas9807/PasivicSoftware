import re 
import traceback
 # quick comparisons
from ..meta import VAR,IS_OK


   
def is_name(var):
    is_ok = True
    try:            
        if len(str(var))<2: return {VAR:None,IS_OK: not is_ok}

        pattern_wrong = re.compile(r'([^A-Za-z\.,Ññ ]+)')
    
        match_wrong = pattern_wrong.findall(str(var))
        #MATCH_WRONG AND MATCH_OK RETURNS ONLY ONE GROUP ('ALAMO A.LORENZO A.')

        if len(match_wrong)>0: 
            return {VAR:var,IS_OK: not is_ok}
        else:
            return {VAR:var,IS_OK:is_ok}
    except IndexError:
        print(traceback.format_exc())

        return {VAR:var,IS_OK: not is_ok}





    
def is_id(var):
    is_ok = True
    
    try:
        tmp = str(var)
        if tmp=='':
            return {VAR:None,IS_OK: not is_ok}

        if tmp.isalnum(): 
            return {VAR:var,IS_OK: not is_ok}
        else:
            split = re.split(r'[-]?',tmp)
            
            if not len(split)==2: return (var,not is_ok)
            else:
                split_one = str(split[0]).upper().strip()
                split_two = str(split[1]).strip()
                if not split_one=='E' and not split_one=='V': 
                    return {VAR:var,IS_OK: not is_ok}
                elif  not split_two.isdigit(): 
                    return {VAR:var,IS_OK: not is_ok}
                else:
                    return {VAR:(split_one,split_two),IS_OK: is_ok}

    except: 
        return {VAR:var,IS_OK: not is_ok}



def is_account(var): 
    is_ok = True 
    try:
        if var=='': return {VAR:None,IS_OK: not is_ok}  

        tmp = str(var) 
        pattern_wrong = re.compile(r'([^0-9-]+)')
        matches_wrong = pattern_wrong .findall(tmp)
        if len(matches_wrong)>0: 
            return {VAR:var,IS_OK: is_ok}
        
        pattern_ok = re.compile(r'^([0-9]{4})-([0-9]{4})')
        matches_ok = pattern_ok.findall(tmp)

        #REMEMBER ADDING OPTION TO SWITCH BETWEEN ONE AND TWO COLUMNS
        #EXAMPLE [('0114', '0162')]
        if len(matches_ok[0])==2:   #it means the account is longer thats supposed 
                                #so most likely that complete account is enterily in one cell
            return {VAR:var,IS_OK: is_ok}
        else:  #error ocurred
            return {VAR:var,IS_OK: not is_ok}
    except IndexError:

        return {VAR:var,IS_OK: not is_ok}   

def is_account2(var):
    is_ok = True  
    try:
        if var=='':
            return {VAR:None,IS_OK: not is_ok}
        pattern = re.compile(r'([0-9]+)')
        tmp = int(var) if isinstance(var,float) else var
        matches = pattern.findall(str(tmp))
        if len(matches)==1: 
            return {VAR:var,IS_OK: is_ok}
        else:  #error ocurred
            return {VAR:var,IS_OK: not is_ok}
    except:

        return {VAR:var,IS_OK: not is_ok}






        







