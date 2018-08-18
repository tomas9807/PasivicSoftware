import re
import traceback



def format_data_socios(meta,row,patterns):
    name = is_name(row[patterns[meta.NAME]],meta) 
    _id = is_id(row[patterns[meta.ID]],meta)
    acc = (is_account(row[patterns[meta.ACC][0]],meta),is_account2(row[patterns[meta.ACC][1]],meta))
    return {meta.NAME:name,meta.ID:_id,meta.ACC:acc}



def is_name(var,meta):
    is_ok = True
    try:            
        if len(str(var))<2: return {meta.VAR:None,meta.IS_OK: not is_ok}

        pattern_wrong = re.compile(r'([^A-Za-z\.,Ññ ]+)')
    
        match_wrong = pattern_wrong.findall(str(var))
        #MATCH_WRONG AND MATCH_OK RETURNS ONLY ONE GROUP ('ALAMO A.LORENZO A.')

        if len(match_wrong)>0: 
            return {meta.VAR:var,meta.IS_OK: not is_ok}
        else:
            return {meta.VAR:var,meta.IS_OK:is_ok}
    except IndexError:
        print(traceback.format_exc())

        return {meta.VAR:var,meta.IS_OK: not is_ok}





    
def is_id(var,meta):
    is_ok = True
    
    try:
        tmp = str(var)
        if tmp=='':
            return {meta.VAR:None,meta.IS_OK: not is_ok}

        if tmp.isalnum(): 
            return {meta.VAR:var,meta.IS_OK: not is_ok}
        else:
            split = re.split(r'[-]?',tmp)
            
            if not len(split)==2: return (var,not is_ok)
            else:
                split_one = str(split[0]).upper().strip()
                split_two = str(split[1]).strip()
                if not split_one=='E' and not split_one=='V': 
                    return {meta.VAR:var,meta.IS_OK: not is_ok}
                elif  not split_two.isdigit(): 
                    return {meta.VAR:var,meta.IS_OK: not is_ok}
                else:
                    match = re.findall(r'[1-9]+[0-9]*',split_two)
                    return {meta.VAR:(split_one,match[0]),meta.IS_OK: is_ok}

    except: 
        return {meta.VAR:var,meta.IS_OK: not is_ok}


def is_account(var,meta): 
    is_ok = True 
    try:
        if var=='': return {meta.VAR:None,meta.IS_OK: not is_ok}  

        tmp = str(var) 
        pattern_wrong = re.compile(r'([^0-9-]+)')
        matches_wrong = pattern_wrong .findall(tmp)
        if len(matches_wrong)>0: 
            return {meta.VAR:var,meta.IS_OK: is_ok}
        
        pattern_ok = re.compile(r'^([0-9]{4})-([0-9]{4})')
        matches_ok = pattern_ok.findall(tmp)

        #REMEMBER ADDING OPTION TO SWITCH BETWEEN ONE AND TWO COLUMNS
        #EXAMPLE [('0114', '0162')]
        if len(matches_ok[0])==2:   #it means the account is longer thats supposed 
                                #so most likely that complete account is enterily in one cell
            return {meta.VAR:var,meta.IS_OK: is_ok}
        else:  #error ocurred
            return {meta.VAR:var,meta.IS_OK: not is_ok}
    except IndexError:

        return {meta.VAR:var,meta.IS_OK: not is_ok}   

def is_account2(var,meta):
    is_ok = True  
    try:
        if var=='':
            return {meta.VAR:None,meta.IS_OK: not is_ok}
        pattern = re.compile(r'([0-9]+)')
        tmp = int(var) if isinstance(var,float) else var
        matches = pattern.findall(str(tmp))
        if len(matches)==1: 
            return {meta.VAR:var,meta.IS_OK: is_ok}
        else:  #error ocurred
            return {meta.VAR:var,meta.IS_OK: not is_ok}
    except:

        return {meta.VAR:var,meta.IS_OK: not is_ok}