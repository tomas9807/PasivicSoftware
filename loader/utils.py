
ID = 0
ACC = 1   #quick comparions
NAME = 2
INDEX = 3
IS_OK = 4
from .profile import profile



def get_socios_asdict(name,_id,acc):
    dict = {NAME:name,ID:_id,ACC:acc}
    print(dict)
    # is_ok = name[1] and _id[1] and acc[0][1] and acc[1][1]
    # name = name[0]
    # _id = ''.join(_id[0])
    # new_acc = []
    # new_acc.append(acc[0][0])
    # new_acc.append(acc[1][0])
    # dict = {NAME:name,ID:_id,ACC:new_acc,IS_OK:is_ok}
    return dict

   