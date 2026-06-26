import utils as u

def saldo_atual():
    u.read_key()
    pass
def total_entradas():
    u.read_key()
    pass
def total_despesdas():
    u.read_key()
    pass
def gastos_por_categoria(): 
    u.read_key()
    pass
def entradas_por_categoria():
    u.read_key()
    pass
def relatorio_mensal():
    u.read_key()
    pass
def relatorio_anual():
    u.read_key()
    pass


def menu_relatorio():
    while True:
        u.limpar_tela()
        u.double_line()
        print('RELATÓRIOS'.center(u.size,' '))
        u.double_line()
        print('1 - SALDO ATUAL')
        print('2 - TOTAL DE ENTRADAS')
        print('3 - TOTAL DE DESPESAS')
        print('4 - GASTOS POR CATEGORIA')
        print('5 - ENTRADAS POR CATEGORIA')
        print('6 - RELATÓRIO MENSAL')
        print('7 - RELATÓRIO ANUAL')
        print('0 - VOLTAR')
        u.double_line()
        opcao = u.ler_opcao_menu(7)
        u.double_line()
        
        if opcao == 1:
            u.limpar_tela()
            saldo_atual()

        elif opcao == 2:
            u.limpar_tela()
            total_entradas()

        elif opcao == 3:
            u.limpar_tela()
            total_despesdas()

        elif opcao == 4:
            u.limpar_tela()
            gastos_por_categoria()

        elif opcao == 5:
            u.limpar_tela()
            entradas_por_categoria()

        elif opcao == 6:
            u.limpar_tela()
            relatorio_mensal()

        elif opcao == 7:
            u.limpar_tela()
            relatorio_anual()

        elif opcao == 0:
            u.limpar_tela()
            break

if __name__ == '__main__':
    menu_relatorio()



#Campos: Data, Descrição, Categoria, Valor