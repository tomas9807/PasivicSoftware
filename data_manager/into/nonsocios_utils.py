import re



def get_ids(meta,row,patterns): 
    return is_id(row[patterns[meta.ID]],meta)

def get_date(meta,file_name,key):
    return get_date_from_filename(file_name,key,meta)
   
def get_id(meta,var):
    return is_id(var,meta)

def get_mov(var):
    return is_mov(var)
    






def is_id(var,meta):
    is_ok = True

    try:
        _id = str(var).strip()

        if _id=='': return {meta.VAR:None,meta.IS_OK: not is_ok}
        pattern = re.compile(r'[0-9]+')
        match = pattern.findall(_id)
        if len(match)>0: return {meta.VAR:match[0],meta.IS_OK:is_ok}
    except:
        return {meta.VAR:var,meta.IS_OK: not is_ok}

def get_date_from_filename(file_name,key,meta):
    if key==meta.EMPLEADOS:
        matches = re.search(r'0*([0-9]{1,2})-0*([0-9]{1,2})-[0-9]+',file_name).groups()
        if matches and len(matches)==2:
            day = matches[0]
            month = matches[1]
            offset = -1 if day==15 else 0
            quin = (month * 2) + offset
            return quin
    elif key==meta.OBREROS:
        matches = re.search(r'0*([0-9]+)20',file_name).groups()
        if matches and len(matches)==1:
            date = matches[0]
            return date
    return None




    matches = re.search(r'0*([0-9]{1,2})-0*([0-9]{1,2})-[0-9]+',file_name).groups() if key==meta.EMPLEADOS else re.search(r'0*([0-9]+)20',file_name)
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


        