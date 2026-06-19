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
        u.line()
        print('VISUALIZAÇÕES & GRÁFICOS'.center(30,' '))
        u.line()
        print('1 - PIZZA POR CATEGORIA')
        print('2 - BARRAS POR CATEGORIA')
        print('3 - EVOLUÇÃO SALDO')
        print('4 - LINHA DE DESPESAS')
        print('5 - VOLTAR')
        u.line()
        opcao = input('Digite a opção desejada: ')
        u.line()
        if opcao == '1':
            u.limpar_tela()
            grafico_pizza_por_categoria()
        elif opcao == '2':
            u.limpar_tela()
            grafico_barras_categoria()
        elif opcao == '3':
            u.limpar_tela()
            evolucao_saldo()
        elif opcao == '4':
            u.limpar_tela()
            grafico_linha_despesas()
        elif opcao == '5':
            u.limpar_tela()
            break
        else:
            u.limpar_tela()
            print('Opcão Inválida')
            u.read_key()

if __name__ == '__main__':
    menu_visualizacoes()
