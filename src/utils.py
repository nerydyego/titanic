import pandas as pd

def transformar_sexo(valor):
    if valor == 'female':
        return 1
    else:
        return 0
        