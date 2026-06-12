import subprocess
import sys
import time
'''funções auxiliares reutilizaveis gerais'''

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

def ValidaCriar(ref_modulo: str,ref_lista: list)->bool:
    for item in ref_lista:
        if item['nome'] == ref_modulo:
            return True
    return False
                
def encontraIdIndex(ref_id,ref_lista):
    #if len(ref_lista) > 10: # se houver pelo menos uma categoria cadastrada ele entra
    for index,item in enumerate(ref_lista): 
         if item['id'] == ref_id:
            return True, index
    # mesmo que o user informe um valor absurdo (ex:30) ele vai rodar,
    # pode até ocorrer de id após o 10 ser 30, mas outros 19 foram removidos
    # mas mesmo assim ele compara os id's e retorna caso esse id exista          
    return False, 1000 #1000 é para manter a consistência da tupla
    ''' 
    Usar enumarate em um fatiamento de listas [i:f]
    funciona de forma que a contagem do index do enumerate comece em 0, não na posição de inicio do corte
    '''

def calculaId(lista):
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1
    


