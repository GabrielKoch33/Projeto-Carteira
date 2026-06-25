'''
- terminar editar e remover entradas
- fazer busca por campos
- reler e melhorar
'''
import utils as u
from categorias import listar_categorias
import estruturas_dados as est

def adicionar_entradas():
    valor_entrada = input('Digite o valor em R$ da entrada: ')
    valor_entrada = u.converte_moeda(valor_entrada)

    if type(valor_entrada) == str:
        return valor_entrada
    
    else: 
        # descrição será uma lista, assim podemos procurar por plavras chaves
        descricao_entrada = input('Insira uma descrição para a entrada: ').strip().lower().split(' ')

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
        while True:
            # Parte responsável por permitir entrada válida de ID de categoria
            categoria_index = u.ler_valida_id()
            achou, indice_categoria = u.encontra_id_e_retorna_index(categoria_index, est.lista_categorias)

            if achou:
                id = u.gera_id(est.lista_entradas)# depois que tudo dá certo é gerado um ID

                for palavra in descricao_entrada: # como descrição é uma lista, cada palavra vai ser uma chave em um dicionario
                    if palavra not in est.palavras_desc_entradas:
                        est.palavras_desc_entradas[palavra] = set()
                        est.palavras_desc_entradas[palavra].add(id)
                    else: # cada palavra vai conter um set onde guarda os ID das entradas
                        est.palavras_desc_entradas[palavra].add(id)
                        

                est.lista_entradas.append({"id":id,
                                    "valor":valor_entrada,
                                    "descricao":descricao_entrada,
                                    "categoria":est.lista_categorias[indice_categoria]["nome"],
                                    "data":data})
                break

            else: 
                print('Tente Novamente!')
                continue

        return('Entrada cadastrada!')

def listar_entradas():

    if len(est.lista_entradas) == 0:
        return 'Registro de entradas vazio. Nenhuma entrada para listar!'
    
    else:
        print(f'{"ID":<5}{"VALOR":<10}{"DESCRIÇÃO":<20}{"CATEGORIA":<15}{"DATA":<10}')
        print("-" * 60)
        for item in est.lista_entradas:
           print(
            f'{item["id"]:<5}'
            f'{item["valor"]:<10.2f}'#.2f = duas casas decimais
            f'{' '.join(item["descricao"]):<20}'
            f'{item["categoria"]:<15}'
            f'{item["data"]:<10}'#Alinha para ESQUERDA e reserva 20 espaços
            )
        u.line()  
        return 'Lista retornada com sucesso!'
    
def editar_entradas():

    if est.lista_entradas: #se conter logs de entrada, da inicio ao processo
        listar_entradas()

        id_entrada = u.ler_valida_id() #while true e try/except para ler id informado

        achou, indice_log_editar = u.encontra_id_e_retorna_index(id_entrada, est.lista_entradas)
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou:
            return 'Entrada não encontrada ou cadastrada!'
                
        else:
            print('Qual campo dessa entrada você deseja editar? ')
            u.line()

            while True:
                campo = input(f'[1] - VALOR\n[2] - DESCRIÇÃO\n[3] - CATEGORIA\n[4] - DATA\nR: ').strip()

                if campo not in {'1','2','3','4'}:
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
                        est.lista_entradas[indice_log_editar]["valor"] = novo_valor
                        return 'Campo "VALOR" alterado com sucesso!'
                                    
                case '2':
                    u.line()
                    nova_descricao = input('Digite a nova descrição: ').strip().title().split(' ')
                    est.lista_entradas[indice_log_editar]['descricao'] = nova_descricao                        
                    return 'Campo "DESCRIÇÃO" alterado com sucesso!'

                case '3':
                    u.line()
                    listar_categorias()
                    while True:
                        id_nova_categoria = u.ler_valida_id()                           
                        encontrou_id, indice_categoria = u.encontra_id_e_retorna_index(id_nova_categoria, est.lista_categorias)

                        if encontrou_id:
                            est.lista_entradas[indice_log_editar]['categoria'] = est.lista_categorias[indice_categoria]['nome']
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
                        else:                               
                            break # senão, valor é válido e insere data
                    est.lista_entradas[indice_log_editar]['data'] = data
                    return 'Campo "DATA" alterado com sucesso!'

                case _: # _ é como se fosse um 'ELSE'. usar | (barra reta) é como um OR
                    u.line()
                    return('Insira um campo válido!')      
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para editar')
           
def remover_entradas():

    if est.lista_entradas: #se conter logs de entrada, da inicio ao processo
        listar_entradas()

        id_entrada = u.ler_valida_id() #while true e try/except para ler id informado

        achou, indice_log_remover = u.encontra_id_e_retorna_index(id_entrada, est.lista_entradas)
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou:
            return 'Entrada não encontrada ou cadastrada!'
                
        else:
            id_removido = est.lista_entradas[indice_log_remover]['id']
            # ex: ID 15 pode estar no indice [4]

            for item in est.lista_entradas[indice_log_remover]['descricao']:
                est.palavras_desc_entradas[item].discard(id_removido)
                # discard

                if not est.palavras_desc_entradas[item]: # se o set ficou vazio (a palavra (key) so aparecia nesse log) então exclui a key
                    del est.palavras_desc_entradas[item]

            est.lista_entradas.pop(indice_log_remover)
            return (f'Entrada de ID: {id_removido} foi removida!')
            
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para remover!')

def buscar_por_descricao():

    palavra_chave = input('Insira uma palavra-chave para a busca: ').strip().lower()

    if palavra_chave not in est.palavras_desc_entradas:
        return ('Nenhuma descrição com essa palavra-chave foi encontrada!')
    else:
        ids_encontrados = est.palavras_desc_entradas[palavra_chave] #recebe os id das entradas da respectiva palavra chave

        print(f'{"ID":<5}{"VALOR":<10}{"DESCRIÇÃO":<20}{"CATEGORIA":<15}{"DATA":<10}')
        print("-" * 60)

        for item in est.lista_entradas: #percorre a lista de entradas comparando [id] com os id relacionados a palavra-chave
            if item['id'] in ids_encontrados:
                print(
                    f'{item["id"]:<5}'
                    f'{item["valor"]:<10.2f}'
                    f'{" ".join(item["descricao"]):<20}'
                    f'{item["categoria"]:<15}'
                    f'{item["data"]:<10}'
                )

        u.line()
        return ('Consulta por descrição retornada com sucesso!')


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
        print('ENTRADAS'.center(60,' '))
        u.line()
        print('1 - ADICIONAR ENTRADA')
        print('2 - EDITAR ENTRADA')
        print('3 - REMOVER ENTRADA')
        print('4 - LISTAR ENTRADAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        u.line()
        opcao = u.ler_opcao_menu(7)
        u.line()

        if opcao == 1:
            u.limpar_tela()
            msg = adicionar_entradas()
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
            msg = listar_entradas()
            print(msg)
            u.line()
            u.read_key()

        elif opcao == 5:
            u.limpar_tela()
            msg = buscar_por_descricao()
            print(msg)
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
