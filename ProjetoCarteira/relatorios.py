import utils as u
import main as m

def saldoAtual():
    u.readKey()
    pass
def totalEntradas():
    u.readKey()
    pass
def totalDespesdas():
    u.readKey()
    pass
def gastosPorCategoria(): 
    u.readKey()
    pass
def entradasPorCategoria():
    u.readKey()
    pass
def relatorioMensal():
    u.readKey()
    pass
def relatorioAnual():
    u.readKey()
    pass


def menuRelatorio():
    while True:  
        u.limparTela()
        print('===============================')
        print('--- RELATÓRIOS ---')
        print('===============================')
        print('1 - SALDO ATUAL')
        print('2 - TOTAL DE ENTRADAS')
        print('3 - TOTAL DE DESPESAS')
        print('4 - GASTOS POR CATEGORIA')
        print('5 - ENTRADAS POR CATEGORIA')
        print('6 - RELATÓRIO MENSAL')
        print('7 - RELATÓRIO ANUAL')
        print('8 - VOLTAR')
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            saldoAtual()
        elif opcao == 2:
            totalEntradas()
        elif opcao == 3:
            totalDespesdas()
        elif opcao == 4:
            gastosPorCategoria()
        elif opcao == 5:
            entradasPorCategoria()
        elif opcao == 6:
            relatorioMensal()
        elif opcao == 7:
            relatorioAnual()
        elif opcao == 8:
            m.mainMenu()
        else:
            print('Opcão Inválida')
            u.readKey()
            menuRelatorio()

if __name__ == '__main__':
    menuRelatorio()



#Campos: Data, Descrição, Categoria, Valor