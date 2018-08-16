import re



def get_ids(row,patterns): 
    return is_id(row[patterns[ID]])

def get_date(file_name,key):
    return get_date_from_filename(file_name,key)
   
def get_id(var):
    return is_id(var)

def get_mov(var):
    return is_mov(var)
    






def is_id(var):
    is_ok = True

    try:
        _id = str(var).strip()

        if _id=='': return {VAR:None,IS_OK: not is_ok}
        pattern = re.compile(r'[0-9]+')
        match = pattern.findall(_id)
        if len(match)>0: return {VAR:match[0],IS_OK:is_ok}
    except:
        return {VAR:var,IS_OK: not is_ok}

def get_date_from_filename(file_name,key):

    if key==EMPLEADOS and re.search(get_filename_handfuls(OBREROS),file_name,re.IGNORECASE):
        return get_filename_handfuls(OBREROS)


    matches = re.search(r'0*([0-9]{1,2})-0*([0-9]{1,2})-[0-9]+',file_name).groups() if key==EMPLEADOS else re.search(r'0*([0-9]{1,2})20?[0-9]{2}',file_name)
    matches = matches.groups()
    if matches and len(matches)==2 or len(matches)==1:
        return matches
    
    return None

def is_mov(var):
    var = str(var)

    match = re.search(r'^([0-9]*)([.,]*)([0-9]{0,2})',var).groups()

    if len(match)==3:
        return match
    elif var.isdigit():
        return (var[1:len(var)-2],'.',var[:-2])
    else:
        return None


        