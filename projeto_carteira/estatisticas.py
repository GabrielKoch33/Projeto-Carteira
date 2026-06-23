import utils as u

def media_gastos():
    u.read_key()
    pass
def maior_menor_despesa():
    u.read_key()
    pass
def maior_menor_entrada():
    u.read_key()
    pass
def desvio_padrao():
    u.read_key()
    pass
def percentual_categoria():
    u.read_key()
    pass


def menu_estatisticas():
    while True:
        u.limpar_tela()
        u.line()
        print('ESTATÍSTICAS'.center(30,' '))
        u.line()
        print('1 - MÉDIA DE GASTOS')
        print('2 - MAIOR E MENOR DESPESA')
        print('3 - MAIOR E MENOR ENTRADA')
        print('4 - DESVIO PADRÃO')
        print('5 - PERCENTUAL POR CATEGORIA')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao_menu(5)
        u.line()
        
        if opcao == 1:
            media_gastos()

        elif opcao == 2:
            maior_menor_despesa()

        elif opcao == 3:
            maior_menor_entrada()

        elif opcao == 4:
            desvio_padrao()

        elif opcao == 5:
            percentual_categoria()

        elif opcao == 0:
            u.limpar_tela()
            break


if __name__ == '__main__':
    menu_estatisticas()

