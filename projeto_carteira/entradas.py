'''
- terminar editar e remover entradas
- fazer busca por campos
- reler e melhorar
'''
import utils as u
from categorias import listar_categorias
from estruturasDados import lista_entradas, lista_categorias

def adicionar_entradas():
    valor_entrada = input('Digite o valor em R$ da entrada: ')
    valor_entrada = u.converte_moeda(valor_entrada)

    if type(valor_entrada) == str:
        return valor_entrada
    
    else: 
        # descrição será uma lista, assim podemos procurar por plavras chaves
        descricao_entrada = input('Insira uma descrição para a entrada: ').strip().title().split(' ')

        while True:
            data = u.converte_data()

            if data[0] == 'E':
                u.line()
                print(data)
                u.line()
                continue # se voltar erro, pede data novamente

            else:
                break # senão, valor válido e insere data
        '''
        REVER ESSE BLOCO PARA EVITAR INSERIR UM ID INEXISTÊNTE
        '''
        u.line()
        listar_categorias()
        u.line()
        categoria_index = int(input('Digite o ID da categoria desta entrada: '))
    
        lista_entradas.append({"id":u.gera_id(lista_entradas),
                            "valor":valor_entrada,
                            "descricao":descricao_entrada,
                            "categoria":lista_categorias[categoria_index-1]["nome"],
                            "data":data})
            
        u.line()    
        return('Entrada cadastrada!')

    
def editar_entradas():

    if lista_entradas: #se conter logs de entrada, da inicio ao processo
        listar_entradas()

        id_entrada = u.ler_valida_id() #while true e try/except para ler id informado

        achou, indice = u.encontra_id_e_retorna_index(id_entrada, lista_entradas)
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou:
            return 'Entrada não encontrada ou cadastrada!'
                
        else:
            print('Qual campo dessa entrada você deseja editar? ')
            u.line()
            while True:
                campo = input(f'[1] - VALOR\n[2] - DESCRIÇÃO\n[3] - CATEGORIA\n[4] - DATA\nR: ').strip()
                if campo not in ('1234'):
                    continue
                else:
                    break
            match campo:
                case '1':
                    u.line()
                    novo_valor = input('Digite o novo valor em R$ da entrada: ')
                    novo_valor = u.converte_moeda(novo_valor)

                    if type(novo_valor) == str:
                        return novo_valor
                    else:
                        lista_entradas[indice]["valor"] = novo_valor
                        return 'Campo "VALOR" alterado com sucesso!'
                                    
                case '2':
                    u.line()
                    nova_descricao = input('Digite a nova descrição: ').strip().title().split(' ')
                    lista_entradas[indice]['descricao'] = nova_descricao                        
                    return 'Campo "DESCRIÇÃO" alterado com sucesso!'

                case '3':
                    u.line()
                    listar_categorias()
                    while True:
                        id_nova_categoria = u.ler_valida_id()                           
                        encontrou_id, indice_categoria = u.encontra_id_e_retorna_index(id_nova_categoria, lista_categorias)

                        if encontrou_id:
                            lista_entradas[indice]['categoria'] = lista_categorias[indice_categoria]['nome']
                            return 'Campo "CATEGORIA" alterado com sucesso!'
                        else:
                            print('Tente novamente!')
                            continue

                case '4':
                    u.line()
                    while True:
                        data = u.converte_data()

                        if data[0] == 'E':
                            u.line()
                            print(data)
                            u.line()
                            continue # se voltar erro, pede data novamente
                        else:                                break # senão, valor é válido e insere data
                    lista_entradas[indice]['data'] = data
                    return 'Campo "DATA" alterado com sucesso!'

                case _: # _ é como se fosse um 'ELSE'. usar | (barra reta) é como um OR
                    u.line()
                    return('Insira um campo válido!')      
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
        opcao = u.ler_opcao_menu(7)
        u.line()

        if opcao == 1:
            u.limpar_tela()
            msg = listar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 2:
            u.limpar_tela()
            msg = editar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 3:
            u.limpar_tela()
            msg = remover_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 4:
            u.limpar_tela()
            msg = adicionar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 5:
            u.limpar_tela()
            buscar_por_descricao()
            u.line()
            u.read_key()

        elif opcao == 6:
            u.limpar_tela()
            buscar_por_categoria()
            u.line()
            u.read_key()

        elif opcao == 7:
            u.limpar_tela()
            buscar_por_periodo()
            u.line()
            u.read_key()

        elif opcao == 0:
            u.limpar_tela()
            break
        
if __name__ == '__main__':
    menu_entradas()
