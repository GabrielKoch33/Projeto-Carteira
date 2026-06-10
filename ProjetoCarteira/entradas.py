import utils as u
import main as m

def adicionarEntradas():
    u.readKey()
    pass
def editarEntradas():
    u.readKey()
    pass
def removerEntradas():
    u.readKey()
    pass
def listarEntradas():
    u.readKey()
    pass
def buscarPorDescricao():
    u.readKey()
    pass
def buscarPorCategoria():
    u.readKey()
    pass
def buscarPorPeriodo():
    u.readKey()
    pass

#Campos: Data, Descrição, Valor
def menuEntradas():
    while True:
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
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            adicionarEntradas()
        elif opcao == 2:
            editarEntradas()
        elif opcao == 3:
            removerEntradas()
        elif opcao == 4:
            listarEntradas()
        elif opcao == 5:
            buscarPorDescricao()
        elif opcao == 6:
            buscarPorCategoria()
        elif opcao == 7:
            buscarPorPeriodo()
        elif opcao == 0:
            m.mainMenu()
        else:
            print('Opcão Inválida')
            u.readKey()
            menuEntradas()

if __name__ == '__main__':
    menuEntradas()
'''
{
    "id": 1,
    "descricao": "Salário",
    "valor": 3500.00,
    "data": "2026-06-10"
}
'''