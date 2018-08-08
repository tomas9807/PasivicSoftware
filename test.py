from loader import excel
from loader.meta import get_default_patterns,SOCIOS,EMPLEADOS,OBREROS
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


if __name__=='__main__':
    pass
    # if os.path.isfile('db.sqlite3'): os.remove('db.sqlite3')
    # excel.read_file(
    #     path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS 2017 NUEVO.xls'),
    #     patterns=get_default_patterns(SOCIOS),
    #     key = SOCIOS
    # )

    

    # excel.read_file(
    #     path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS EMPLEADOS.xlsx'),
    #     patterns=get_default_patterns(EMPLEADOS),
    #     key = EMPLEADOS
    # )

    # excel.read_file(
    #     path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS OBREROS.xlsx'),
    #     patterns=get_default_patterns(OBREROS),
    #     key = OBREROS
    # )
    