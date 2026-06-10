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

def existeCategoria(valor: str,ref_lista: list,padrao=None)->bool:
    '''
    padrao == none: apenas verificamos se existe
    padrao == true: verificamos o campo default
    '''
    if padrao == None:
        for item in ref_lista:
            if item['nome'] == valor:
                return True
        
    elif padrao == True:
        for item in ref_lista:
            if item['nome'] == valor and item['default'] == padrao:
                return True
            elif item['nome'] == valor and item['default'] == (not padrao):
                return False
                