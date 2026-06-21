import utils as u
from estruturasDados import lista_categorias

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

    if u.valida_existencia(nome_categoria,lista_categorias):
        return 'Essa categoria já existe, duplicadas não são permitidas'
    
    else:
        lista_categorias.append({"id":u.calcula_id(lista_categorias),
                                 "nome":nome_categoria,"default":False})
        
        return 'Categoria adicionada!'


def editar_cat_personalizada():
    id_categoria = u.valida_editar_ou_excluir_categoria(lista_categorias)

    if type(id_categoria) == int:

        achaPosicao = u.encontra_id_index(id_categoria,lista_categorias)
        if achaPosicao[0] == True:
            novoValor = input('Qual será o novo nome?: ').title()
            lista_categorias[achaPosicao[1]]["nome"] = novoValor
            return 'Campo alterado com sucesso!'

        elif achaPosicao[0] == False:
           return 'Não foi possível encontrar esse item!'
        
    else:
        return id_categoria

def excluir_cat_personalizada():
    id_categoria = u.valida_editar_ou_excluir_categoria(lista_categorias)

    if type(id_categoria) == int:
        achaPosicao = u.encontra_id_index(id_categoria,lista_categorias)
            # busca um linha que contenha o id indicado, retorna o index dessa linha para remover/alterar
        if achaPosicao[0] == True:
            lista_categorias.pop(achaPosicao[1])
            return 'Campo removido com sucesso!'
            
        else:
            return 'Não foi possível encontrar esse item!'

    else:
        return id_categoria


def menu_categorias():
    while True:
        u.limpar_tela()
        u.line()
        print('CATEGORIAS'.center(30,' '))
        u.line()
        print('1 - LISTAR CATEGORIAS')
        print('2 - CRIAR CATEGORIA PERSONALIZADA')
        print('3 - EDITAR CATEGORIA PERSONALIZADA')
        print('4 - EXCLUIR CATEGORIA PERSONALIZADA')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao(4)
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