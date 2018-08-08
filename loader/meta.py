SOCIOS = 1
EMPLEADOS = 2
OBREROS = 3
NAME = 4
ACC = 5
ID = 6
IS_OK = 7
VAR = 8

PATTERNS_DEFAULT = {
    
    SOCIOS:{NAME:2,ID:4,ACC:(6,7)},
    EMPLEADOS:{ID:3},
    OBREROS:{ID:1},
}

def get_default_patterns(key):
    return PATTERNS_DEFAULT.get(key)
