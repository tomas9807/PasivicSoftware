import os
import metadata 
from data_manager.out import to_database
from data_manager.into import excel

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KEYS = metadata.setup.Keys()

if __name__=='__main__':

    conn = to_database.connect()
    with conn:
        cur = conn.cursor()   
        to_database.check_data_base(cur)
        

        excel.setup_database(
        path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS 2017 NUEVO.xls'),
        patterns=get_default_patterns(SOCIOS),
        key = SOCIOS,
        cur=cur
        )

        

        excel.fill_database(
        path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS EMPLEADOS.xlsx'),
        patterns=get_default_patterns(EMPLEADOS),
        key = EMPLEADOS,
        cur=cur
        )

        excel.fill_database(
        path= os.path.join(BASE_DIR,'archivos/PASIVIC 2016/SOCIOS OBREROS.xlsx'),
        patterns=get_default_patterns(OBREROS),
        key = OBREROS,
        cur=cur
        )

        excel.fill_movs(
        cur=cur,
        key = OBREROS,
        indentifier = APORTE,
        list_of_files = (
            os.path.join(BASE_DIR,'archivos/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 022016.xls'),
            os.path.join(BASE_DIR,'archivos/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 042016.xls'),
         ))

   