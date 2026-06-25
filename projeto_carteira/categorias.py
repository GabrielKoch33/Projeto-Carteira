import utils as u
from estruturas_dados import lista_categorias

'''
aprender isInstance()
'''

def listar_categorias():
    print(f'{'ID':<5}{'CATEGORIA':<10}')
    
    for categoria in lista_categorias:
        print(f'{categoria["id"]:<5}{categoria["nome"]:<10}')

   
def criar_cat_personalizada():
    '''
    Para o python, '' é visto como Falsy, enquanto '  ' é Truthy
    O que determina isso é a quantidade de caracteres, se == 0 -> false, se <> 0 -> true
    Se o user digitasse '   ' ele seria válido. Por isso usamos strip(), ele removerá todos os espaços em branco
    Se mesmo tirando os espaços em branco o tamanho for > 0 então temos uma entrada válida
    '''
    while True:
        nome_categoria = input('Digite o nome da nova categoria: ').strip()

        if nome_categoria: 
            nome_categoria = nome_categoria.title()
            break
        else:    
            print('Insira um nome válido (não vazio)!')
            continue       
    # verifica se o nome que o user inserir ja existe na lista de categorias
    if u.valida_existencia_campo_nome(nome_categoria,lista_categorias):
        return 'Essa categoria já existe, duplicadas não são permitidas'
    
    else:
        lista_categorias.append({"id":u.gera_id(lista_categorias),
                                 "nome":nome_categoria,"default":False})
        
        return 'Categoria adicionada!'


def editar_cat_personalizada():
                   # impede o user de por valores inexistentes, editar cat defaults ou valores inválidos
    id_categoria = u.valida_editar_ou_excluir_categoria(lista_categorias)
                   # retorna o id que o user inseriu 
    if type(id_categoria) == int:
                        # vai usar o valor de id informado para checar se existe essa categoria criada
        achou, indice = u.encontra_id_e_retorna_index(id_categoria,lista_categorias)
        if achou:       # ao encontrar, vai retornar a posição de alteração correta    
            novoValor = input('Qual será o novo nome?: ').title()
            lista_categorias[indice]["nome"] = novoValor
            return 'Campo alterado com sucesso!'

        else:
           return 'Não foi possível encontrar esse item!'
        
    else:
        return id_categoria

def excluir_cat_personalizada():
    id_categoria = u.valida_editar_ou_excluir_categoria(lista_categorias)

    if type(id_categoria) == int:

        achou, indice = u.encontra_id_e_retorna_index(id_categoria,lista_categorias)
        if achou:
            lista_categorias.pop(indice)
            return 'Campo removido com sucesso!'
            
        else:
            return 'Não foi possível encontrar esse item!'

    else:
        return id_categoria


def menu_categorias():
    while True:
        u.limpar_tela()
        u.line()
        print('CATEGORIAS'.center(60,' '))
        u.line()
        print('1 - LISTAR CATEGORIAS')
        print('2 - CRIAR CATEGORIA PERSONALIZADA')
        print('3 - EDITAR CATEGORIA PERSONALIZADA')
        print('4 - EXCLUIR CATEGORIA PERSONALIZADA')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao_menu(4)
        u.line()
        
        if opcao == 1:
            u.limpar_tela()
            listar_categorias()
            u.read_key()

        elif opcao == 2:
            u.limpar_tela()
            msg = criar_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 3:
            u.limpar_tela()
            msg = editar_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 4:
            u.limpar_tela()
            msg = excluir_cat_personalizada()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 0:
            u.limpar_tela()
            break



if __name__ == '__main__':
    menu_categorias()