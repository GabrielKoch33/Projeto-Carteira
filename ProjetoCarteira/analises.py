import utils as u


def categoria_maior_consumo(): 
    u.read_key()
    pass
def mes_maior_gasto(): 
    u.read_key()
    pass
def mes_menor_gasto():
    u.read_key()
    pass
def taxa_media_economia():
    u.read_key()
    pass
def tendencia_saldo():
    u.read_key()
    pass


def menu_analises():
    while True:
        u.limpar_tela()
        u.line()
        print('--- ANÁLISES DO USUÁRIO ---')
        u.line()
        print('1 - CATEGORIA QUE MAIS CONSOME ')
        print('2 - MÊS COM MAIOR GASTO')
        print('3 - MÊS COM MENOR GASTO')
        print('4 - TAXA MÉDIA DE ECONOMIA')
        print('5 - TENDÊNCIA DO SALDO')
        print('0 - VOLTAR')
        u.line()
        opcao = input('Digite a opção desejada: ')
        u.line()
        if opcao == '1':
            u.limpar_tela()
            categoria_maior_consumo()
        elif opcao == '2':
            u.limpar_tela()
            mes_maior_gasto()
        elif opcao == '3':
            u.limpar_tela()
            mes_menor_gasto()
        elif opcao == '4':
            u.limpar_tela()
            taxa_media_economia()
        elif opcao == '5':
            u.limpar_tela()
            tendencia_saldo()
        elif opcao == '0':
            u.limpar_tela()
            break
        else:
            u.limpar_tela()
            print('Opcão Inválida')
            u.read_key()

            
if __name__ == '__main__':
    menu_analises()


