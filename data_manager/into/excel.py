import pandas as pd
import os,traceback
from . import socio_utils
from . import nonsocios_utils





def read_excel(path):
    return pd.read_excel(path, header=None, na_filter=False)


def get_data_excel(df, patterns, key, func):
    for row in df.itertuples():

        try:

            # here i should warn that there are some problems with some cells
            yield func(row=row, patterns=patterns)

        except TypeError:
            print(traceback.format_exc())
            break


# identitifier means aporte or deduccion
def insert_movs(cur, key, indentifier, list_of_files):

    for file in list_of_files:

        date = nonsocios_utils.get_date(file_name=os.path.basename(file), key=key)

        if date is None:
            return None
        elif isinstance(date, dict):
            return None
        else:
            print(date)
            df = read_excel(file)

            for row in df.itertuples():
                _id = get_id(row[get_default_patterns(MOVIMIENTOS)[ID]])

                if _id[IS_OK]:

                    mov = get_mov(
                        row[get_default_patterns(MOVIMIENTOS)[APORTE_DEDUC]])

                    if mov is not None:

                        data = cur.execute(""" 
                        SELECT id FROM socios WHERE cedula=? LIMIT 1
                        """, (_id[VAR],))
                        socio_id = data.fetchone()

                        if socio_id:
                            insert_mov(cur, key, indentifier,
                                       date[0], socio_id, ''.join(mov))


def setup_database(cur, path, patterns, key):

    df = read_excel(path)

    if key == SOCIOS:

        func = socios_utils.format_data_socios
    else:

        func = nonsocios_utils.get_ids

    for data in get_data_excel(df=df, patterns=patterns, key=key, func=func):
        insert_socios(socio=data, key=key, cur=cur)
