import utils as u
import main as m
def adicionarDespesa():
    u.readKey()
    pass
def editarDespesa():
    u.readKey()
    pass
def removerDespesa():
    u.readKey()
    pass
def listarDespesa():
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

#Campos: id, Data, Descrição, Categoria, Valor
def menuDespesa():
    while True:
        u.limparTela()
        print('===============================')
        print('--- DESPESAS ---')
        print('===============================')
        print('1 - ADICIONAR DESPESA')
        print('2 - EDITAR DESPESA')
        print('3 - REMOVER DESPESA')
        print('4 - LISTAR DESPESAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            adicionarDespesa()
        elif opcao == 2:
            editarDespesa()
        elif opcao == 3:
            removerDespesa()
        elif opcao == 4:
            listarDespesa()
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
            menuDespesa()

if __name__ == '__main__':
    menuDespesa()
'''
{
    "id": 1,
    "descricao": "Mercado",
    "valor": 250.00,
    "categoria": "Alimentação",
    "data": "2026-06-10"
}
'''