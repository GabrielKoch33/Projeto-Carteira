import utils as u
import main as m

def mediaGastos():
    u.readKey()
    pass
def maiorMenorDespesa():
    u.readKey()
    pass
def maiorMenorEntrada():
    u.readKey()
    pass
def desvioPadrao():
    u.readKey()
    pass
def percentualCategoria():
    u.readKey()
    pass


def menuEstatisticas():
    while True:  
        u.limparTela()
        print('===============================')
        print('--- ESTATÍSTICAS ---')
        print('===============================')
        print('1 - MÉDIA DE GASTOS')
        print('2 - MAIOR E MENOR DESPESA')
        print('3 - MAIOR E MENOR ENTRADA')
        print('4 - DESVIO PADRÃO')
        print('5 - PERCENTUAL POR CATEGORIA')
        print('0 - VOLTAR')
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            mediaGastos()
        elif opcao == 2:
            maiorMenorDespesa()
        elif opcao == 3:
            maiorMenorEntrada()
        elif opcao == 4:
            desvioPadrao()
        elif opcao == 5:
            percentualCategoria()
        elif opcao == 0:
            m.mainMenu()
        else:
            print('Opcão Inválida')
            u.readKey()
            menuEstatisticas()

if __name__ == '__main__':
    menuEstatisticas()

