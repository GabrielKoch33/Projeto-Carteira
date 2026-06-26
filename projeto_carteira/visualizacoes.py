import utils as u

def grafico_pizza_por_categoria():
    u.read_key()
    pass
def grafico_barras_categoria(): 
    u.read_key()
    pass
def evolucao_saldo(): 
    u.read_key()
    pass
def grafico_linha_despesas():
    u.read_key()
    pass


def menu_visualizacoes():
    while True:
        u.limpar_tela()
        u.double_line()
        print('VISUALIZAÇÕES & GRÁFICOS'.center(u.size,' '))
        u.double_line()
        print('1 - PIZZA POR CATEGORIA')
        print('2 - BARRAS POR CATEGORIA')
        print('3 - EVOLUÇÃO SALDO')
        print('4 - LINHA DE DESPESAS')
        print('0 - VOLTAR')
        u.double_line()
        opcao = u.ler_opcao_menu(4)
        u.double_line()
        if opcao == 1:
            u.limpar_tela()
            grafico_pizza_por_categoria()

        elif opcao == 2:
            u.limpar_tela()
            grafico_barras_categoria()

        elif opcao == 3:
            u.limpar_tela()
            evolucao_saldo()

        elif opcao == 4:
            u.limpar_tela()
            grafico_linha_despesas()

        elif opcao == 0:
            u.limpar_tela()
            break
        

if __name__ == '__main__':
    menu_visualizacoes()
