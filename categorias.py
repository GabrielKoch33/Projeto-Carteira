import utils as u
from estruturasDados import lista_categorias

def listar_categorias():
    print(f'{'ID':<5}{'CATEGORIA':<10}')
    
    for categoria in lista_categorias:
        print(f'{categoria["id"]:<5}{categoria["nome"]:<10}')

   
def criar_cat_personalizada():
    nomeCategoria = input('Digite o nome da nova categoria: ').strip().title()

    if u.valida_criar(nomeCategoria,lista_categorias):
        return 'Essa categoria já existe, duplicadas não são permitidas'
    
    else:
        lista_categorias.append({"id":u.calcula_id(lista_categorias),
                                 "nome":nomeCategoria,"default":False})
        
        return 'Categoria adicionada!'

def editar_cat_personalizada():
    if len(lista_categorias) == 10:
        return 'Não existem categorias customizadas. Categorias padrões não são editáveis'
    
    else:
        listar_categorias()
        idCategoria = int(input('Digite o id da categoria que deseja editar: '))

        if idCategoria <= 10:
            return 'Categorias padrões do sistema não são editáveis'
        
        else:
            achaPosicao = u.encontra_id_index(idCategoria,lista_categorias)
            if achaPosicao[0] == True:
                novoValor = input('Qual será o novo nome?: ').title()
                lista_categorias[achaPosicao[1]]["nome"] = novoValor
                return 'Campo alterado com sucesso!'

            elif achaPosicao[0] == False:
                return 'Não foi possível encontrar esse item!'


def excluir_cat_personalizada():

    if len(lista_categorias) == 10:
        return 'Não existem categorias customizadas. Categorias padrões não são excluíveis'
    
    else:
        listar_categorias()
        idCategoria = int(input('Digite o id da categoria que deseja remover: '))
        
        if idCategoria <= 10:
            return 'Categorias padrões do sistema não são excluíveis'

        else:
            achaPosicao = u.encontra_id_index(idCategoria,lista_categorias)
            # busca um linha que contenha o id indicado, retorna o index dessa linha para remover/alterar
            if achaPosicao[0] == True:
                lista_categorias.pop(achaPosicao[1])
                return 'Campo removido com sucesso!'
            
            elif achaPosicao[0] == False:
                return 'Não foi possível encontrar esse item ou não foram cadastradas categorias customizadas'



def menu_categorias():
    while True:
        u.limpar_tela()
        u.line()
        print('--- CATEGORIAS ---')
        u.line()
        print('1 - LISTAR CATEGORIAS')
        print('2 - CRIAR CATEGORIA PERSONALIZADA')
        print('3 - EDITAR CATEGORIA PERSONALIZADA')
        print('4 - EXCLUIR CATEGORIA PERSONALIZADA')
        print('0 - VOLTAR')
        u.line()
        opcao = input('Digite a opção desejada: ')
        u.line()
        
        if opcao == '1':
            u.limpar_tela()
            listar_categorias()
            u.read_key()

        elif opcao == '2':
            u.limpar_tela()
            msg = criar_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '3':
            u.limpar_tela()
            msg = editar_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '4':
            u.limpar_tela()
            msg = excluir_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '0':
            u.limpar_tela()
            break

        else:
            u.limpar_tela()
            print('Opcão Inválida')
            u.read_key()


if __name__ == '__main__':
    menu_categorias()