import subprocess
import sys
import time

'''funções auxiliares reutilizaveis gerais'''

def limpar_tela():
    # Usa o módulo subprocess, recomendado pelas diretrizes atuais do Python
    if sys.platform.startswith("win"):
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def pause():
    time.sleep(1.5)
        
def read_key():
    input("Pressione ENTER para voltar ao menu...")

def line():
    print('==================================================')
    
def converte_moeda(valor):
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

def valida_criar(ref_modulo: str,ref_lista: list)->bool:
    '''
    percorre a lista para encontrar se existe ou não o campo nome
    '''
    for item in ref_lista:
        if item['nome'] == ref_modulo:
            return True
    return False
                
def encontra_id_index(ref_id,ref_lista):
    '''
    # mesmo que o user informe um valor absurdo (ex:30) ele vai rodar,
    # pode até ocorrer de id após o 10 ser 30, mas outros 19 foram removidos
    # mas mesmo assim ele compara os id's e retorna caso esse id exista
    '''
    for index,item in enumerate(ref_lista): 
         if item['id'] == ref_id:
            return True, index
          
    return False, 1000 # não encontrou o id
    ''' 
    Usar enumarate em um fatiamento de listas [i:f]
    funciona de forma que a contagem do index do enumerate comece em 0, não na posição de inicio do corte
    '''

def calcula_id(lista):
    '''
    acessa uma lista, se for vazia retorna id 1 para o 1º elemento, senão encontra o maior nº id e + 1
    '''
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1
    
def converte_data():
    entrada = input("Digite a data (apenas números, ex: 25122026): ").strip()

    if len(entrada) == 8 and entrada.isdigit():
        data_formatada = f"{entrada[:2]}/{entrada[2:4]}/{entrada[4:]}"
        return data_formatada

    else:
        return "Erro: Digite exatamente 8 números."

