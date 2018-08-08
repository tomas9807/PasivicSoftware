SOCIOS = 1
EMPLEADOS = 2
OBREROS = 3
NAME = 4
ACC = 5
ID = 6





def get_default_patterns():
    PATTERNS_DEFAULT = {
    
    SOCIOS:{NAME:2,ID:4,ACC:(6,7)},
    EMPLEADOS:{NAME:2,ID:4,ACC:(6,7)},
    OBREROS:{NAME:2,ID:4,ACC:(6,7)},
}
    yield from PATTERNS_DEFAULT
