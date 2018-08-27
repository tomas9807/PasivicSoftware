import os
from metadata import setup  as metadata_setup
from data_manager.out import to_database,to_format60
from data_manager.into import from_excel,from_database
from data_manager import data_utils
from datetime import date
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_list_of_files(pardir):

    return (
    os.path.join(pardir,file)
    for file in os.listdir(pardir))



def remove_database():
    if os.path.isfile('database/db.sqlite3'):
        os.remove('database/db.sqlite3')

def make_60_format_files(meta,cur,identifier_str,key_str):
    todays_date = date.today().strftime('%d%m%y')
    pardir = os.path.abspath('files/format_60')
    os.makedirs(pardir,exist_ok=True)
    sub_dir =  f'/{identifier_str}_{key_str}'
    dir_towrite = os.path.join(pardir,sub_dir)
    os.makedirs(dir_towrite,exist_ok=True,mode=0o777)
    n_socios  = from_database.get_total_num_socios(cur)
    dates_str = (date for date in data_utils.get_date_fields(meta,key_str).split(','))
    for date_str in dates_str:
        to_format60.make_file(meta,cur,identifier_str,key_str,dir_towrite,todays_date,date_str,n_socios)

if __name__=='__main__':
    #remove_database()
    conn = data_utils.connect() #connect to the database 
    with conn:
        META_KEYS = metadata_setup.Keys() #setup a object that has keys for easy dict manipulation and for differentiation of files or content
        cur = conn.cursor()   
        data_utils.check_data_base(META_KEYS,cur)  #check if the database exists if not create one

        make_60_format_files(meta=META_KEYS,cur=cur,identifier_str='aportes',key_str='obreros')
        
        

        # from_excel.setup_database(
        #     meta=META_KEYS,
        #     cur=cur,
        #     key=META_KEYS.SOCIOS,
        #     patterns = META_KEYS.get_default_patterns(META_KEYS.SOCIOS),
        #     file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS 2017 NUEVO.xls'),  #add socios to the database
        # )

        # from_excel.setup_database(
        #     meta=META_KEYS,
        #     cur=cur,
        #     key=META_KEYS.EMPLEADOS,
        #     patterns = META_KEYS.get_default_patterns(META_KEYS.EMPLEADOS),
        #     file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS EMPLEADOS.xlsx'),  #add socios to the database
        # )

        # from_excel.setup_database(
        #     meta=META_KEYS,
        #     cur=cur,
        #     key=META_KEYS.OBREROS,
        #     patterns = META_KEYS.get_default_patterns(META_KEYS.OBREROS),
        #     file = os.path.join(BASE_DIR,'files/PASIVIC 2016/SOCIOS OBREROS.xlsx'),  #add socios to the database
        # )
          

        # from_excel.insert_movs(
        # meta= META_KEYS,
        # cur=cur,
        # key = META_KEYS.OBREROS,
        # indentifier = META_KEYS.APORTE,
        # list_of_files = get_list_of_files('files/PASIVIC 2016/OBREROS 2016 OK/APORTES OK/')
        # )
        # from_excel.insert_movs(
        # meta= META_KEYS,
        # cur=cur,
        # key = META_KEYS.OBREROS,
        # indentifier = META_KEYS.DEDUC,
        # list_of_files = get_list_of_files('files/PASIVIC 2016/OBREROS 2016 OK/DEDUCCIONES OK/')
        # )
        # from_excel.insert_movs(
        # meta= META_KEYS,
        # cur=cur,
        # key = META_KEYS.EMPLEADOS,
        # indentifier = META_KEYS.APORTE,
        # list_of_files = get_list_of_files('files/PASIVIC 2016/EMPLEADOS 2016 OK/APORTES 2016')
        # )
        # from_excel.insert_movs(
        # meta= META_KEYS,
        # cur=cur,
        # key = META_KEYS.EMPLEADOS,
        # indentifier = META_KEYS.DEDUC,
        # list_of_files = get_list_of_files('files/PASIVIC 2016/EMPLEADOS 2016 OK/DEDUCCIONES 2016')
        # )
        
        
        
        
   