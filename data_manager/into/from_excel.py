import pandas as pd
import os,traceback
from . import socios_utils
from . import nonsocios_utils
from ..out import to_database



import sys
print(__name__)
print(sys.path)

def read_file(path):
    try:
        path = str(path)
        if path.endswith(('xlsx','xls')):
            return pd.read_excel(path, header=None, na_filter=False,encoding='utf-8')
        elif path.endswith(('csv',)):
            return pd.read_csv(path, header=None, na_filter=False,encoding="ISO-8859-1")
    except Exception as e :
        print(path,e)
        #print(traceback.format_exc())
        


def get_data_file(meta,df, patterns, key, func):

    for row in df.itertuples():

        try:

            # here i should warn that there are some problems with some cells
            yield func(meta=meta,row=row, patterns=patterns)

        except TypeError:
            print(traceback.format_exc())
            break


# identitifier means aporte or deduccion
def insert_movs(meta,cur, key, indentifier, list_of_files):

    for file in list_of_files:
        df = read_file(file)
        if df is not None:
            date = nonsocios_utils.get_date(meta=meta,file_name=os.path.basename(file), key=key)

            if date is None:
                return None
            elif isinstance(date, dict):
                return None
            else:
                cont = 1
                is_csv = file.endswith(('csv',))
                for row in df.itertuples():

                    if is_csv:
                        actual_row = str(row[1]).split(';')
                        _id = nonsocios_utils.get_id(meta,actual_row[meta.get_default_patterns(meta.MOVIMIENTOS)[meta.ID] -1 ])
                       
                        
                    else:
                        _id = nonsocios_utils.get_id(meta,row[meta.get_default_patterns(meta.MOVIMIENTOS)[meta.ID] ])

                    if _id[meta.IS_OK]:
                        try:
                            if is_csv:
                                mov = nonsocios_utils.get_mov(actual_row[meta.get_default_patterns(meta.MOVIMIENTOS)[meta.MOVIMIENTOS] - 1])
                            else:
                                mov = nonsocios_utils.get_mov(row[ meta.get_default_patterns(meta.MOVIMIENTOS)[meta.MOVIMIENTOS] ]  )
                        except IndexError as e:
                            print(file,e,f'row {cont}')
                            
                        else:
                            if mov is not None:

                                data = cur.execute(""" 
                                SELECT id FROM socios WHERE cedula=? LIMIT 1
                                """, (_id[meta.VAR],))
                                socio_id = data.fetchone()

                                if socio_id:
                                    
                                    to_database.insert_mov(meta,cur, key, indentifier,
                                            date, socio_id, ''.join(mov))
                    cont +=1



def setup_database(meta,cur, key,patterns,file):

    df = read_file(file)
    if df is not None:
        if key == meta.SOCIOS:

            func = socios_utils.format_data_socios
        else:

            func = nonsocios_utils.get_ids

        for data in get_data_file(meta=meta,df=df, patterns=patterns, key=key, func=func):
            to_database.setup_socios(meta=meta,socio=data, key=key, cur=cur)
