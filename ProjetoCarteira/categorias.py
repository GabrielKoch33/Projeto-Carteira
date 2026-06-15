import main as m
import utils as u
from estruturasDados import lista_categorias

def listarCategorias():
    print(f'{'ID':<5}{'CATEGORIA':<10}')
    
    for categoria in lista_categorias:
        print(f'{categoria["id"]:<5}{categoria["nome"]:<10}')

   
def criarCatPersonalizada():
    nomeCategoria = input('Digite o nome da nova categoria: ').strip().title()

    if u.ValidaCriar(nomeCategoria,lista_categorias):
        return 'Essa categoria já existe, duplicadas não são permitidas'
    
    else:
        lista_categorias.append({"id":u.calculaId(lista_categorias),
                                 "nome":nomeCategoria,"default":False})
        
        return 'Categoria adicionada!'

def editarCatPersonalizada():
    if len(lista_categorias) == 10:
        return 'Não foram cadastradas Categorias personalizadas'
    
    else:
        listarCategorias()
        idCategoria = int(input('Digite o id da categoria que deseja editar: '))

        if idCategoria <= 10:
            return 'Categorias padrões do sistema não são editáveis'
        
        else:
            result = u.encontraIdIndex(idCategoria,lista_categorias)
            if result[0] == True:
                novoValor = input('Qual será o novo nome?: ').title()
                lista_categorias[result[1]]["nome"] = novoValor
                return 'Campo alterado com sucesso!'

            elif result[0] == False:
                return 'Não foi possível encontrar esse item!'


def excluirCatPersonalizada():

    if len(lista_categorias) == 10:
        return 'Não foram cadastradas Categorias personalizadas'
    
    else:
        listarCategorias()
        idCategoria = int(input('Digite o id da categoria que deseja remover: '))
        
        if idCategoria <= 10:
            return 'Categorias padrões do sistema não são deletáveis'

        else:
            result = u.encontraIdIndex(idCategoria,lista_categorias)

            if result[0] == True:
                lista_categorias.pop(result[1])
                return 'Campo removido com sucesso!'
            
            elif result[0] == False:
                return 'Não foi possível encontrar esse item ou não foram cadastradas categorias customizadas'



def menuCategorias():
    u.limparTela()
    print('===============================')
    print('--- CATEGORIAS ---')
    print('===============================')
    print('1 - LISTAR CATEGORIAS')
    print('2 - CRIAR CATEGORIA PERSONALIZADA')
    print('3 - EDITAR CATEGORIA PERSONALIZADA')
    print('4 - EXCLUIR CATEGORIA PERSONALIZADA')
    print('0 - VOLTAR')
    print('===============================')
    opcao = input('Digite a opção desejada: ')
    print('===============================')

    if opcao == '1':
        u.limparTela()
        listarCategorias()
        u.readKey()
        menuCategorias()

    elif opcao == '2':
        u.limparTela()
        msg =criarCatPersonalizada()
        print(msg)
        u.readKey()
        menuCategorias()
        
    elif opcao == '3':
        u.limparTela()
        msg = editarCatPersonalizada()
        print(msg)
        u.readKey()
        menuCategorias()

    elif opcao == '4':
        u.limparTela()
        msg = excluirCatPersonalizada()
        print(msg)
        u.readKey()
        menuCategorias()

    elif opcao == '0':
        u.limparTela()
        m.mainMenu()

    else:
        u.limparTela()
        print('Opcão Inválida')
        u.readKey()
        menuCategorias()

if __name__ == '__main__':
    menuCategorias()