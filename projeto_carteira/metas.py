import utils as u

def criar_meta():
    u.read_key()
    pass
def editar_meta():
    u.read_key()
    pass
def excluir_meta():
    u.read_key()
    pass
def listar_metas_and_porcent():
    u.read_key()
    pass

#Campos: nome, valor alvo, prazo
#Indicadores: percentual concluído e valor restante
#Dar uma sugestão de X por Mês para atingir a Meta
def menu_metas():
    while True:
        u.limpar_tela()
        u.line()
        print('METAS'.center(30,' '))
        u.line()
        print('1 - CRIAR META')
        print('2 - EDITAR META')
        print('3 - EXCLUIR META')
        print('4 - LISTAR METAS E PORCENTAGEM')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao_menu(4)
        u.line()
        
        if opcao == 1:
            u.limpar_tela()
            criar_meta()

        elif opcao == 2:
            u.limpar_tela()
            editar_meta()

        elif opcao == 3:
            u.limpar_tela()
            excluir_meta()

        elif opcao == 4:
            u.limpar_tela()
            listar_metas_and_porcent()

        elif opcao == 0:
            u.limpar_tela()
            break



if __name__ == '__main__':
    menu_metas()

