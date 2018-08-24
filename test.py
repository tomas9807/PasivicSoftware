import re

tmp = {'value': 'V-4056366 ', 'bool': False}
def get_split():
    value = str(tmp['value']).strip()
    if value=='':
        return None
    if value.isalnum(): 
        return None
    return re.split(r'[-]+',value)

print(get_split())