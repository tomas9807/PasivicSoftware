import pandas as pd
import os,traceback
from . import socios_utils
from . import nonsocios_utils
from ..out import to_database




def read_excel(path):
    return pd.read_excel(path, header=None, na_filter=False)


def get_data_excel(meta,df, patterns, key, func):
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

        date = nonsocios_utils.get_date(meta=meta,file_name=os.path.basename(file), key=key)

        if date is None:
            return None
        elif isinstance(date, dict):
            return None
        else:
 
            df = read_excel(file)

            for row in df.itertuples():

                _id = nonsocios_utils.get_id(meta,row[ meta.get_default_patterns(meta.MOVIMIENTOS)[meta.ID] ])

                if _id[meta.IS_OK]:

                    mov = nonsocios_utils.get_mov(row[ meta.get_default_patterns(meta.MOVIMIENTOS)[meta.MOVIMIENTOS] ]  )

                    if mov is not None:

                        data = cur.execute(""" 
                        SELECT id FROM socios WHERE cedula=? LIMIT 1
                        """, (_id[meta.VAR],))
                        socio_id = data.fetchone()

                        if socio_id:
                            to_database.insert_mov(meta,cur, key, indentifier,
                                       date[0], socio_id, ''.join(mov))



def setup_database(meta,cur, key,patterns,file):

    df = read_excel(file)

    if key == meta.SOCIOS:

        func = socios_utils.format_data_socios
    else:

        func = nonsocios_utils.get_ids

    for data in get_data_excel(meta=meta,df=df, patterns=patterns, key=key, func=func):
        to_database.setup_socios(meta=meta,socio=data, key=key, cur=cur)
