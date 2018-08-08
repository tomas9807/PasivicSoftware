from ..meta import IS_OK,VAR
import re

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


    

