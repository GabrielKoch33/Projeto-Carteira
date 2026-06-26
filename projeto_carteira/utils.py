import subprocess
import sys
import time
from categorias import *

size = 82

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

def double_line():
    print('='*size)
    
def line():
    print('-'*size)
''''''
def calcula_saldo():
    pass

def ler_opcao_menu(num_max_opcao):
    '''
    ler opção dos menus
    '''
    while True:
        try:
            op = int(input('Digite a opção que deseja acessar: '))

        except Exception as erro:
            print(f'Erro: {erro}')
            continue

        else:
            if op < 0 or op > num_max_opcao:
                print('Escolha uma opção dentre as apresentadas!')
                continue
            else:
                return op
            
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

def valida_existencia_campo_nome(ref_nome_categoria_user: str,ref_lista: list)->bool:
    '''
    percorre a lista para encontrar se existe ou não o campo nome
    usado em: categoria, metas
    '''
    for item in ref_lista:
        if item['nome'] == ref_nome_categoria_user:
            return True
    return False
                
def gera_id(lista):
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

def valida_editar_ou_excluir_categoria(lista):
    '''
    requer: ser chamada para validar o ID que da entrada que o user informar
    '''
    if len(lista) == 10:
        return 'Categorias padrões não são editáveis/removíveis'
    
    else:
        listar_categorias()
        while True:
            try:
                id_informado = int(input('Digite o ID da categoria que deseja alterar ou excluir: '))

            except:
                print('Escolha uma opção (numérica) válida!')
                continue # roda esse try até que uma entrada válida seja informada

            if id_informado <= 10:
                return 'Categorias padrões do sistema não são editáveis/removíveis'
            else:
                return id_informado #quando a entrada for validada e não der erro, retorna o id da categoria que o user quer usar

def encontra_id_e_retorna_index(ref_id,ref_lista):
    '''
    # mesmo que o user informe um valor absurdo (ex:30) ele vai rodar,
    # pode até ocorrer de id após o 10 ser 30, mas outros 19 foram removidos
    # mas mesmo assim ele compara os id's e retorna caso esse id exista
    Usar enumarate em um fatiamento de listas [i:f]
    funciona de forma que a contagem do index do enumerate comece em 0, não na posição de inicio do corte
    '''
    for index,item in enumerate(ref_lista): 
         if item['id'] == ref_id:
            return True, index
          
    return False, 1000 # não encontrou o id
   
def ler_valida_id ():
    ''' faz a validação de id'''
    while True: # valida entrada valida de valores
        try:
            id_entrada = int(input('Digite o ID: '))

        except:
            print('Escolha uma opção (numérica) válida!')
            continue # roda esse try até que uma entrada válida seja informada

        else:
            return id_entrada