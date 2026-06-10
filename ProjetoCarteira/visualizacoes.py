import utils as u
import main as m

def pizzaCategoria():
    u.readKey()
    pass
def barrasCategoria(): 
    u.readKey()
    pass
def evolSaldo(): 
    u.readKey()
    pass
def linhaDespesas():
    u.readKey()
    pass


def menuVisualizacoes():
    while True:  
        u.limparTela()
        print('===============================')
        print('--- VISUALIZAÇÕES & GRÁFICOS ---')
        print('===============================')
        print('1 - PIZZA POR CATEGORIA')
        print('2 - BARRAS POR CATEGORIA')
        print('3 - EVOLUÇÃO SALDO')
        print('4 - LINHA DE DESPESAS')
        print('5 - VOLTAR')
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            pizzaCategoria()
        elif opcao == 2:
            barrasCategoria()
        elif opcao == 3:
            evolSaldo()
        elif opcao == 4:
            linhaDespesas()
        elif opcao == 5:
            m.mainMenu()
        else:
            print('Opcão Inválida')
            u.readKey()
            menuVisualizacoes()

if __name__ == '__main__':
    menuVisualizacoes()
