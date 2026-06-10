import main as m
import utils as u
from estruturasDados import lista_categorias

def listarCategorias():
    u.limparTela()
    for indice,categoria in enumerate(lista_categorias):
        print(f'{indice+1}  -  {categoria["nome"]}')

    u.readKey()
    menuCategorias()

def criarCatPersonalizada():
    u.limparTela()
    nomeCategoria = input('Digite o nome da nova categoria: ').title().strip()

    if u.existeCategoria(nomeCategoria,lista_categorias):
        print(f'{nomeCategoria} já existe, duplicadas não são válidas')
        u.readKey()
        menuCategorias()

    else:
        lista_categorias.append({"nome":nomeCategoria,"default":False})
        print(f'{nomeCategoria} adicionada!')
        u.readKey()
        menuCategorias()
    

def editarCatPersonalizada():
    u.limparTela()
    nomeCategoria = input('Digite o nome da categoria que deseja editar: ').title().strip()

    if u.existeCategoria(nomeCategoria,lista_categorias):
        if u.existeCategoria(nomeCategoria,lista_categorias,True):
            print('Não é possível alterar categorias padrões do sistema')
            u.readKey()
            menuCategorias()
        else:
            novaCategoria = input('Digite o nome que você deseja alterar: ').title().strip()
            print(f'Alterada: "{nomeCategoria}" -> "{novaCategoria}"')
            for item in lista_categorias:
                if item["nome"] == nomeCategoria:
                    item['nome'] = novaCategoria
            u.readKey()
            menuCategorias()
            
    else:
        print('Não é possível editar categorias inexistêntes, verifique a ortografia ou crie a devida categoria')
        u.readKey()
        menuCategorias()
    

def excluirCatPersonalizada():
    u.limparTela()
    nomeCategoria = input('Digite o nome da categoria que deseja remover: ').title().strip()

    if u.existeCategoria(nomeCategoria,lista_categorias):
        if u.existeCategoria(nomeCategoria,lista_categorias,True):
            print('Não é possível alterar categorias padrões do sistema')
            u.readKey()
            menuCategorias()
        else:
            print(f'Removida: "{nomeCategoria}"')
            for item in lista_categorias:
                if item["nome"] == nomeCategoria:
                    lista_categorias.remove(item)
            u.readKey()
            menuCategorias()
            
    else:
        print('Não é possível remover categorias inexistêntes, verifique a ortografia ou crie a devida categoria')
        u.readKey()
        menuCategorias()

    u.limparTela() 
    u.readKey()
    menuCategorias()

lista_categorias = [ 
  {"nome":"Alimentação","default":True},
  {"nome":"Transporte","default":True},
  {"nome":"Moradia","default":True},
  {"nome":"Saúde","default":True},
  {"nome":"Educação","default":True},
  {"nome":"Lazer","default":True},
  {"nome":"Salário","default":True},
  {"nome":"Investimentos","default":True},
  {"nome":"Outros","default":True}
]

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
        listarCategorias()
    elif opcao == '2':
        criarCatPersonalizada()
    elif opcao == '3':
        editarCatPersonalizada()
    elif opcao == '4':
        excluirCatPersonalizada()
    elif opcao == '0':
        m.mainMenu()
    else:
        print('Opcão Inválida')
        u.readKey()
        menuCategorias()

if __name__ == '__main__':
    menuCategorias()