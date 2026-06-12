import subprocess
import sys
import time
'''funções auxiliares reutilizaveis'''

def limparTela():
    # Usa o módulo subprocess, recomendado pelas diretrizes atuais do Python
    if sys.platform.startswith("win"):
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def pause():
    time.sleep(1.5)
        
def readKey():
    input("Pressione ENTER para voltar ao menu...")

def ValidaCriarCategoria(ref_categoria: str,ref_lista: list,padrao=None)->bool:
    '''
    padrao == none: apenas verificamos se existe
    padrao == true: verificamos o campo default
    '''
    if padrao == None:
        return [ True for item in ref_categoria if item['nome'] == ref_categoria]
        
    elif padrao == True:
        for item in ref_lista:
            if item['nome'] == ref_categoria and item['default'] == padrao:
                return True
            elif item['nome'] == ref_categoria and item['default'] == (not padrao):
                return False
                
def converteMoeda(valor):
    '''
    Aprender Try/Except e revisar essa função
    '''
    if valor == '':
        return 'Valores vazios não são permitidos'
    
    try:
        valor = valor.replace('.', '')
        valor = valor.replace(',', '.')
        valor = float(valor)

    except (ValueError,AttributeError):
        return 'Formato inválido'
    
    if valor <= 0:
        return 'Valores negativos ou nulos não são permitidos'
    
    return valor
    
def calculaId(lista):
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1
    
def verificaId(ref_id,ref_lista):
    for item in ref_lista:
        if item['id'] == ref_id:
            return True
