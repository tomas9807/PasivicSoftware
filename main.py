import os
from metadata import setup  as metadata_setup
from data_manager.out import to_database
from data_manager.into import from_excel

BASE_DIR = os.path.abspath(os.path.dirname(__file__))



def remove_database():
    import subprocess
    subprocess.run('sudo rm -f ../../database/db.sqlite3',check=True)




if __name__=='__main__':
    remove_database()
    conn = to_database.connect() #connect to the database 
    with conn:
        META_KEYS = metadata_setup.Keys() #setup a object that has keys for easy dict manipulation and for differentiation of files or content
        cur = conn.cursor()   
        to_database.check_data_base(META_KEYS,cur)  #check if the database exists if not create one
        

        from_excel.setup_database(
            meta=META_KEYS,
            cur=cur,
            key=META_KEYS.SOCIOS,
            patterns = META_KEYS.get_default_patterns(META_KEYS.SOCIOS),
            file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS 2017 NUEVO.xls'),  #add socios to the database
        )

        from_excel.setup_database(
            meta=META_KEYS,
            cur=cur,
            key=META_KEYS.EMPLEADOS,
            patterns = META_KEYS.get_default_patterns(META_KEYS.EMPLEADOS),
            file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS EMPLEADOS.xlsx'),  #add socios to the database
        )

        from_excel.setup_database(
            meta=META_KEYS,
            cur=cur,
            key=META_KEYS.OBREROS,
            patterns = META_KEYS.get_default_patterns(META_KEYS.OBREROS),
            file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS OBREROS.xlsx'),  #add socios to the database
        )
          
          


        from_excel.insert_movs(
        meta= META_KEYS,
        cur=cur,
        key = META_KEYS.OBREROS,
        indentifier = META_KEYS.APORTE,
        list_of_files = (
            os.path.join(BASE_DIR,'files/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 022016.xls'),
            os.path.join(BASE_DIR,'files/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 042016.xls'),
         ))
        
        from_excel.insert_movs(
        meta= META_KEYS,
        cur=cur,
        key = META_KEYS.EMPLEADOS,
        indentifier = META_KEYS.APORTE,
        list_of_files = (
            os.path.join(BASE_DIR,'files/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 022016.xls'),
            os.path.join(BASE_DIR,'files/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/APORTES PASIVIC SEMANA 042016.xls'),
         ))

   