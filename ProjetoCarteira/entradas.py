'''
- terminar editar e remover entradas
- fazer busca por campos
- reler e melhorar
'''
import utils as u
import main as m
from categorias import listarCategorias
from estruturasDados import lista_entradas, lista_categorias

def adicionarEntradas():
    valorEntrada = input('Digite o valor em R$ da entrada: ').replace(' ','') #125.5
    valorEntrada = u.converteMoeda(valorEntrada)
    if type(valorEntrada) == str:
        return valorEntrada
    
    else: 
        # descrição será uma lista, assim podemos procurar por plavras chaves
        descricaoEntrada = input('Insira uma descrição para a entrada: ').strip().title().split(' ')
        dataDMA = input('Digite a data da entrada DD/MM/YYYY: ').strip()
        listarCategorias()
        categoriaIndex = int(input('Digite o Id da categoria desta entrada: '))

        lista_entradas.append({"id":u.calculaId(lista_entradas),
                            "valor":valorEntrada,
                            "descricao":descricaoEntrada,
                            "categoria":lista_categorias[categoriaIndex-1]["nome"],
                            "data":dataDMA})
        
        return('Entrada cadastrada!')

    
def editarEntradas():
    if lista_entradas:
        idEntrada = input('Digite o Id da entrada que deseja alterar: ').strip()

        if not idEntrada.isnumeric() or idEntrada == '':
            return('Escolha uma opção (numérica) válida!')
        
        elif idEntrada.isnumeric():
            campo = input('Qual campo você deseja editar?: ').lower()

            if campo == 'id':
                return(f'Não é permitido alterar o campo {campo}')
            
            elif campo not in ("valor","descricao","categoria","data"):
                return('Insira um campo válido ou remova os acentos (~,ç,etc)')
            
            else:
                return 'INCOMPLETO'
                
        
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para editar')
        
    
def removerEntradas():
    return 'INCOMPLETO'


def listarEntradas():

    if len(lista_entradas) == 0:
        return 'Registro de entradas vazio. Nenhuma entrada para listar!'
    
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
           
        return 'Lista retornada com sucesso!'

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
        print('1 - LISTAR ENTRADAS')
        print('2 - EDITAR ENTRADA')
        print('3 - REMOVER ENTRADA')
        print('4 - ADICIONAR ENTRADA')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')

        if opcao == '1':
            u.limparTela()
            msg = listarEntradas()
            print(msg)
            u.readKey()
            menuEntradas()

        elif opcao == '2':
            u.limparTela()
            msg = editarEntradas()
            print(msg)
            u.readKey()
            menuEntradas()

        elif opcao == '3':
            u.limparTela()
            msg = removerEntradas()
            print(msg)
            u.readKey()
            menuEntradas()

        elif opcao == '4':
            u.limparTela()
            adicionarEntradas()
            u.readKey()
            menuEntradas()

        elif opcao == '5':
            u.limparTela()
            buscarPorDescricao()
            u.readKey()
            menuEntradas()

        elif opcao == '6':
            u.limparTela()
            buscarPorCategoria()
            u.readKey()
            menuEntradas()

        elif opcao == '7':
            u.limparTela()
            buscarPorPeriodo()
            u.readKey()
            menuEntradas()

        elif opcao == '0':
            u.limparTela()
            m.mainMenu()

        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()
            menuEntradas()

if __name__ == '__main__':
    menuEntradas()
