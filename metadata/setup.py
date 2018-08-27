import json
import os
from datetime import date




class Keys():
    
    __PATH_JSON = os.path.join(os.path.abspath(os.path.dirname(__file__)),'keys.json')
    
    @classmethod
    def get_json(cls):
        with open(cls.__PATH_JSON,'r') as f:
            return json.load(f)
    
    def __init__(self):

        keys_json = Keys.get_json()
        self.SOCIOS = keys_json['SOC']
        self.EMPLEADOS = keys_json['EMP']
        self.OBREROS = keys_json['OBR']
        self.NAME = keys_json['NAME']
        self.ACC = keys_json['ACC']
        self.ID = keys_json['ID']
        self.IS_OK = keys_json['IS_OK']
        self.VAR = keys_json['VAR']
        self.MOVIMIENTOS = keys_json['MOV']
        self.APORTE = keys_json['APOR']
        self.DEDUC = keys_json['DEDU']
        self.QUINCENAS = keys_json['QUIN']
        self.SEMANAS = keys_json['SEM']
        format_60 = keys_json["FORMAT_60"]
        self.LEN_SOCIOS = format_60["LEN_SOCIOS"]
        self.LEN_MONTO_TOTAL = format_60["LEN_MONTO_TOTAL"]
        self.HEAD_CONST = format_60["HEAD_CONST"]
        self.CONST = format_60["CONST"]
        self.FONDO = format_60["FONDO"]
        self.NUM_OFFICINA = format_60["NUM_OFFICINA"]
        self.LEN_HEAD = format_60["LEN_HEAD"]
        self.LEN_CEDULA  = format_60["LEN_CEDULA"]
        self.LEN_MOV_INDIV= format_60["LEN_MOV_INDIV"]
        
        self. ZEROS_CONTENT= format_60["ZEROS_CONTENT"]

        self.tipo_mov = format_60["TIPO_MOV"]

        self.__default_patterns = {

        self.SOCIOS:{self.NAME:2,self.ID:4,self.ACC:(6,7)},
        self.EMPLEADOS:{self.ID:3},
        self.OBREROS:{self.ID:1},
        self.MOVIMIENTOS:{self.ID:1,self.MOVIMIENTOS:3},

        }

    @classmethod
    def pretty_print(cls,dict):
        json = cls.get_json()
        for key_dict in dict:
            for key_json,value_json in json.items():
                if key_dict==value_json:
                    dict[key_json] = dict.pop(key_dict)
        return dict
        
    def get_default_patterns(self,key): 
        
        return self.__default_patterns.get(key)






        




