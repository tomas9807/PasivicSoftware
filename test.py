from loader.socios import excel

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


if __name__=='__main__':
    # excel.read_file(os.path.join(BASE_DIR,'test1.xlsx'))
    excel.read_file(r'C:\Users\PC\Desktop\PASIVIC 2016\SOCIOS 2017 NUEVO.xls')