'''
- terminar editar e remover entradas
- fazer busca por campos
- reler e melhorar
'''
import utils as u
from categorias import listar_categorias
from estruturasDados import lista_entradas, lista_categorias

def adicionar_entradas():
    valorEntrada = input('Digite o valor em R$ da entrada: ')
    valorEntrada = u.converte_moeda(valorEntrada)

    if type(valorEntrada) == str:
        return valorEntrada
    
    else: 
        # descrição será uma lista, assim podemos procurar por plavras chaves
        descricaoEntrada = input('Insira uma descrição para a entrada: ').strip().title().split(' ')

        while True:
            data = u.converte_data()

            if data[0] == 'E':
                u.line()
                print(data)
                u.line()
                continue # se voltar erro, pede data novamente

            else:
                break # senão, valor válido e insere data
        u.line()
        listar_categorias()
        u.line()
        categoriaIndex = int(input('Digite o ID da categoria desta entrada: '))

        lista_entradas.append({"id":u.calcula_id(lista_entradas),
                            "valor":valorEntrada,
                            "descricao":descricaoEntrada,
                            "categoria":lista_categorias[categoriaIndex-1]["nome"],
                            "data":data})
            
        u.line()    
        return('Entrada cadastrada!')

    
def editar_entradas():

    listar_entradas()
    u.line()

    if lista_entradas:
        id_entrada = input('Digite o ID da entrada que deseja alterar: ').strip()

        if not id_entrada.isnumeric() or id_entrada == '':
            return('Escolha uma opção (numérica) válida!')
        
        elif id_entrada.isnumeric():

            achou_posicao = u.encontra_id_index(id_entrada, lista_entradas)
            if not achou_posicao:
                return 'Entrada não encontrada ou cadastrada!'
            
            else:
                campo = input('Qual campo dessa entrada você deseja editar?: ').lower().strip()

                match campo:
                    case 'id': 
                        return('Não é permitido alterar o campo ID')
                    
                    case 'valor':
                        novoValor = input('Digite o novo valor em R$ da entrada: ')
                        novoValor = u.converte_moeda(novoValor)
                        if type(novoValor) == str:
                            return novoValor
                        else:
                            lista_entradas[achou_posicao[1]]["valor"] = novoValor
                            return f'{campo} alterado com sucesso!'
                            
                    case 'descricao':
                        pass
                    case 'categoria':
                        listar_categorias()
                        novaCategoria = int(input('Digite o Id da categoria desta entrada: '))
                    case 'data':
                        pass
                    case _: # _ é como se fosse um 'ELSE'. usar | (barra reta) é como um OR
                        return('Insira um campo válido ou remova os acentos (~,ç,etc)')
                    
                    
            
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para editar')
        
    
def remover_entradas():
    
    listar_entradas()

    return 'INCOMPLETO'


def listar_entradas():

    if len(lista_entradas) == 0:
        return 'Registro de entradas vazio. Nenhuma entrada para listar!'
    
    else:
        print(f'{"ID":<5}{"VALOR":<10}{"DESCRIÇÃO":<20}{"CATEGORIA":<15}{"DATA":<10}')

        for item in lista_entradas:
           print(
            f'{item["id"]:<5}'
            f'{item["valor"]:<10.2f}'#.2f = duas casas decimais
            f'{' '.join(item["descricao"]):<20}'
            f'{item["categoria"]:<15}'
            f'{item["data"]:<10}'#Alinha para ESQUERDA e reserva 20 espaços
            )
        u.line()  
        return 'Lista retornada com sucesso!'

def buscar_por_descricao():
    u.read_key()
    pass

def buscar_por_categoria():
    u.read_key()
    pass

def buscar_por_periodo():
    u.read_key()
    pass

def menu_entradas():
    while True:
        u.limpar_tela()
        u.line()
        print('ENTRADAS'.center(30,' '))
        u.line()
        print('1 - LISTAR ENTRADAS')
        print('2 - EDITAR ENTRADA')
        print('3 - REMOVER ENTRADA')
        print('4 - ADICIONAR ENTRADA')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        u.line()
        opcao = input('Digite a opção desejada: ')
        u.line()

        if opcao == '1':
            u.limpar_tela()
            msg = listar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '2':
            u.limpar_tela()
            msg = editar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '3':
            u.limpar_tela()
            msg = remover_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '4':
            u.limpar_tela()
            msg = adicionar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == '5':
            u.limpar_tela()
            buscar_por_descricao()
            u.line()
            u.read_key()

        elif opcao == '6':
            u.limpar_tela()
            buscar_por_categoria()
            u.line()
            u.read_key()

        elif opcao == '7':
            u.limpar_tela()
            buscar_por_periodo()
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
    menu_entradas()
