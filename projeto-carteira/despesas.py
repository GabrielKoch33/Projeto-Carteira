import utils as u

def adicionar_despesa():
    u.read_key()
    pass
def editar_despesa():
    u.read_key()
    pass
def remover_despesa():
    u.read_key()
    pass
def listar_despesa():
    u.read_key()
    pass
def buscar_por_descricao():
    u.read_key()
    pass
def buscar_por_categoria():
    u.read_key()
    pass
def buscar_por_periodo():
    u.read_key()
    pass


def menu_despesa():
    while True:
        u.limpar_tela()
        u.line()
        print('DESPESAS'.center(30,' '))
        u.line()
        print('1 - ADICIONAR DESPESA')
        print('2 - EDITAR DESPESA')
        print('3 - REMOVER DESPESA')
        print('4 - LISTAR DESPESAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao(7)
        u.line()
        
        if opcao == 1:
            u.limpar_tela()
            adicionar_despesa()

        elif opcao == 2:
            u.limpar_tela()
            editar_despesa()

        elif opcao == 3:
            u.limpar_tela()
            remover_despesa()

        elif opcao == 4:
            u.limpar_tela()
            listar_despesa()

        elif opcao == 5:
            u.limpar_tela()
            buscar_por_descricao()

        elif opcao == 6:
            u.limpar_tela()
            buscar_por_categoria()

        elif opcao == 7:
            u.limpar_tela()
            buscar_por_periodo()

        elif opcao == 0:
            u.limpar_tela()
            break

if __name__ == '__main__':
    menu_despesa()
'''
{
    "id": 1,
    "descricao": "Mercado",
    "valor": 250.00,
    "categoria": "Alimentação",
    "data": "2026-06-10"
}
'''