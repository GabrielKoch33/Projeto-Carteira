import utils as u
import main as m
import datetime 
from categorias import listarCategorias
from estruturasDados import lista_entradas, lista_categorias

def adicionarEntradas():
    valorEntrada = input('Digite o valor em R$ da entrada: ').replace(' ','') #125.5
    valorEntrada = u.converteMoeda(valorEntrada)
    if type(valorEntrada) == str:
        print('Só são aceitos valores numéricos e positivos!')
        u.readKey()
        menuEntradas()
    else: #Esse else ñ é necessário, afinal a função pode retornar ou str, ou float
        descricaoEntrada = input('Digite a fonte da entrada (salário, proventos, etc..): ').strip().title().split(' ')
        dataDMA = input('Digite a data da entrada DD/MM/YYYY')
        listarCategorias()
        categoriaIndex = int(input('Digite o Nº da categoria desta entrada: '))
        lista_entradas.append({"id":u.calculaId(lista_entradas),
                            "valor":valorEntrada,
                            "descricao":descricaoEntrada,
                            "categoria":lista_categorias[categoriaIndex-1]["nome"],
                            "data":dataDMA})
        
        print('Entrada cadastrada!')
        u.readKey()
        menuEntradas()

    
def editarEntradas():
    if listarEntradas():
        while True:
            idEntrada = input('Digite o Id da entrada que deseja alterar ([999] para SAIR): ').strip()
            if not idEntrada.isnumeric() or idEntrada == '':
                print('Escolha uma opção (numérica) válida!')
            elif idEntrada.isnumeric():
                break
        while True:
            campo = print('Qual campo você deseja editar?: ').lower()
            if campo == 'id':
                print(f'Não é permitido alterar o campo {campo}')
            elif campo not in ("valor","descricao","categoria","data"):
                print('Insira um campo válido ou remova os acentos (~,ç,etc)')
            else:
                break
        
    else:
        print('Nenhuma entrada foi registrada ainda! Nada para editar')
        
    
def removerEntradas():
    u.readKey()
    pass
def listarEntradas():
    if len(lista_entradas) == 0:
        return False
    else:
        print(f'{"ID":<5} {"VALOR":<10} {"DESCRIÇÃO":<20} {"CATEGORIA":<15} {"DATA":<12}')
        for item in lista_entradas:
           print(
            f'{item["id"]:<5} '
            f'{item["valor"]:<10.2f} '#.2f = duas casas decimais
            f'{item["descricao"]:<20} '
            f'{item["categoria"]:<15} '
            f'{item["data"]:<12}'#Alinha para ESQUERDA e reserva 12 espaços
            )
    return True

def buscarPorDescricao():
    u.readKey()
    pass
def buscarPorCategoria():
    u.readKey()
    pass
def buscarPorPeriodo():
    u.readKey()
    pass
'''
{
    "id": 1,
    "descricao": "Salário",
    "valor": 3500.00,
    "data": "2026-06-10"
}
'''
#Campos: Data, Descrição, Valor
def menuEntradas():
        u.limparTela()
        print('===============================')
        print('--- ENTRADAS ---')
        print('===============================')
        print('1 - ADICIONAR ENTRADA')
        print('2 - EDITAR ENTRADA')
        print('3 - REMOVER ENTRADA')
        print('4 - LISTAR ENTRADAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')
        if opcao == '1':
            u.limparTela()
            adicionarEntradas()
        elif opcao == '2':
            u.limparTela()
            editarEntradas()
        elif opcao == '3':
            u.limparTela()
            removerEntradas()

        elif opcao == '4':
            u.limparTela()
            if not listarEntradas():
                 print('Nenhuma entrada foi registrada ainda!')
            u.readKey()
            menuEntradas()

        elif opcao == '5':
            u.limparTela()
            buscarPorDescricao()
        elif opcao == '6':
            u.limparTela()
            buscarPorCategoria()
        elif opcao == '7':
            u.limparTela()
            buscarPorPeriodo()
        elif opcao == '0':
            m.mainMenu()
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()
            menuEntradas()

if __name__ == '__main__':
    menuEntradas()
