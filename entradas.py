import utils as u
from categorias import listar_categorias
import estruturas_dados as est
'''
-> output lista: total de registros, categoria mais usada
'''
def adicionar_entradas():

    valor_entrada = input('Digite o valor em R$ da entrada: ')
    valor_entrada = u.converte_moeda(valor_entrada)

    # isinstance(varivael que vamos verificar, tipo esperado que ela seja)
    # retorna True se valor_entrada for str / caso o tipo for tupla e o valor um elemento q esta na tupla, ent True
    if isinstance(valor_entrada,str):
        return valor_entrada
    
    else: 
        # descrição será uma lista, assim podemos procurar por plavras chaves
        while True:
            descricao_entrada = input('Insira uma descrição para a entrada: ').strip().lower()
            if not descricao_entrada:
                print('Tente novamente!')
            else:
                descricao_entrada = descricao_entrada.split()
                break


        while True:
            data = u.converte_data()

            if not data:
                u.double_line()
                print("Erro: Digite exatamente 8 números.")
                u.double_line()
                continue # se voltar erro, pede data novamente

            else:
                break # senão, valor válido e insere data

        listar_categorias()
        u.double_line()

        while True:
            # Parte responsável por permitir entrada válida de ID de categoria
            id_entrada = u.ler_valida_id()
            achou, indice = u.encontra_campo_e_indice(id_entrada, est.lista_categorias,'id')

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
                                    "categoria":est.lista_categorias[indice]["nome"],
                                    "data":data})
                break

            else: 
                print('Tente Novamente!')
                continue

        return('Entrada cadastrada!')

def listar_entradas():

    if not est.lista_entradas:
        return 'Registro de entradas vazio. Nenhuma entrada para listar!'
    
    else:
        
        u.imprime_colunas('ENTRADAS')

        num_registros = 0
        for item in est.lista_entradas:
           descricao = ' '.join(item['descricao'])
           num_registros += 1
           print(
                f'{item["id"]:<5}'
                f'R${item["valor"]:<13.2f}'#.2f = duas casas decimais
                f"{descricao:<30}"
                f'{item["categoria"]:<20}'
                f'{item["data"]:<12}'
            )
        u.double_line()
        print(f'Total de registros: {num_registros}') 
        return 'Lista retornada com sucesso!'
    
def editar_entradas():

    if est.lista_entradas: #se conter logs de entrada, da inicio ao processo
        listar_entradas()
        u.double_line()

        id_entrada = u.ler_valida_id() #while true e try/except para ler id informado
        achou, indice = u.encontra_campo_e_indice(id_entrada,est.lista_entradas,'id')
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou:
            return 'Entrada não cadastrada!'
                
        else:
            print('Qual campo dessa entrada você deseja editar? ')
            u.double_line()

            while True:
                campo = input(f'[1] - VALOR\n[2] - DESCRIÇÃO\n[3] - CATEGORIA\n[4] - DATA\nR: ').strip()

                if campo not in {'1','2','3','4'}:
                    continue
                else:
                    break

            match campo:

                case '1':
                    u.double_line()
                    novo_valor = input('Digite o novo valor em R$ da entrada: ')
                    novo_valor = u.converte_moeda(novo_valor)

                    if isinstance(novo_valor,str):
                        return novo_valor
                    else:
                        est.lista_entradas[indice]["valor"] = novo_valor
                        return 'Campo "VALOR" alterado com sucesso!'
                                    
                case '2':
                    u.double_line()
                    nova_descricao = input('Digite a nova descrição: ').strip().lower().split()
                    # antiga = oi meu amor id = 1 // nova = eae mano
                    if nova_descricao == est.lista_entradas[indice]['descricao']:
                        return 'Campo "DESCRIÇÃO" alterado com sucesso!'
                    else:
                        # loop para remover os indices antigos ligados a palavra
                        for item in est.lista_entradas[indice]['descricao']:
                            est.palavras_desc_entradas[item].discard(id_entrada)
                            if not est.palavras_desc_entradas[item]:
                                del est.palavras_desc_entradas[item] 
                        
                        # loop para criar a hash das palavras da nova descrição
                        for item in nova_descricao:
                            if item not in est.palavras_desc_entradas:
                                est.palavras_desc_entradas[item] = set()
                                est.palavras_desc_entradas[item].add(id_entrada)
                            
                    est.lista_entradas[indice]['descricao'] = nova_descricao                        
                    return 'Campo "DESCRIÇÃO" alterado com sucesso!'

                case '3':
                    u.double_line()
                    listar_categorias()
                    while True:
                        id_nova_categoria = u.ler_valida_id()                           
                        encontrou_id, indice_categoria = u.encontra_campo_e_indice(id_nova_categoria, est.lista_categorias,'id')

                        if encontrou_id:
                            est.lista_entradas[indice]['categoria'] = est.lista_categorias[indice_categoria]['nome']
                            return 'Campo "CATEGORIA" alterado com sucesso!'
                        else:
                            print('Tente novamente!')
                            continue

                case '4':
                    u.double_line()
                    while True:
                        data = u.converte_data()

                        if not data:
                            u.double_line()
                            print("Erro: Digite exatamente 8 números.")
                            u.double_line()
                            continue # se voltar erro, pede data novamente
                        else:                               
                            break # senão, valor é válido e insere data
                    est.lista_entradas[indice]['data'] = data
                    return 'Campo "DATA" alterado com sucesso!'

                case _: # _ é como se fosse um 'ELSE'. usar | (barra reta) é como um OR
                    u.double_line()
                    return('Insira um campo válido!')      
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para editar')
           
def remover_entradas():
    
    if est.lista_entradas: #se conter logs de entrada, da inicio ao processo
        listar_entradas()
        u.double_line()

        id_entrada = u.ler_valida_id()
        achou, indice = u.encontra_campo_e_indice(id_entrada, est.lista_entradas,'id')
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou:
            return 'Entrada não cadastrada!'
                
        else:
            id_removido = est.lista_entradas[indice]['id']
            # ex: ID 15 pode estar no indice [4]

            for item in est.lista_entradas[indice]['descricao']:
                est.palavras_desc_entradas[item].discard(id_removido)
                if not est.palavras_desc_entradas[item]: # se o set ficou vazio (a palavra (key) so aparecia nesse log) então exclui a key
                    del est.palavras_desc_entradas[item]

            est.lista_entradas.pop(indice)
            return (f'Entrada de ID: {id_removido} foi removida!')
            
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para remover!')
    

def buscar_por_descricao():

    if est.lista_entradas:

        while True:
            palavra_chave_busca = input('Insira uma palavra-chave para a busca: ').strip().lower()
            if not palavra_chave_busca:
                print('Tente novamente!')
            else:
                break

        if palavra_chave_busca not in est.palavras_desc_entradas:
            return ('Nenhuma descrição com essa palavra-chave foi encontrada!')
        else:
            ids_encontrados = est.palavras_desc_entradas[palavra_chave_busca] #recebe os id das entradas da respectiva palavra chave

            u.imprime_colunas('ENTRADAS')
            
            num_registros = 0
            for item in est.lista_entradas: #percorre a lista de entradas comparando [id] com os id relacionados a palavra-chave
                if item['id'] in ids_encontrados:
                    descricao = ' '.join(item['descricao'])
                    num_registros += 1
                    print(
                        f'{item["id"]:<5}'
                        f'R${item["valor"]:<13.2f}'
                        f'{descricao:<30}'
                        f'{item["categoria"]:<20}'
                        f'{item["data"]:<12}'
                    )
            u.double_line()
            print(f'Total de registros: {num_registros}')
            return ('Consulta por descrição retornada com sucesso!')
    else:
        return('Nenhuma entrada foi registrada ainda! Nada para consultar!')

def buscar_por_categoria():
    
    if est.lista_entradas: #verifica se a lista de entrada possui elementos

        u.listar_categorias()
        u.double_line()

        id_entrada = u.ler_valida_id()
        achou, indice = u.encontra_campo_e_indice(id_entrada, est.lista_categorias,'id')
                        # verifica se o id informado pelo user existe e se existir retorna sua posição
                        # indice será usado para sabermos onde o id informado está 
        if not achou: 
            return 'Não existe categoria com o ID informado!'
            #verifica se existem categoria com o ID informado
        else:
            u.limpar_tela()
            nome_categoria = est.lista_categorias[indice]['nome']

            if u.encontra_campo_e_indice(nome_categoria, est.lista_entradas,'categoria')[0]:
                
                u.imprime_colunas('ENTRADAS')

                num_registros = 0
                for item in est.lista_entradas:
                    if item['categoria'] == nome_categoria:
                        descricao = ' '.join(item['descricao'])
                        num_registros += 1
                        print(
                            f'{item["id"]:<5}'
                            f'R${item["valor"]:<13.2f}'
                            f'{descricao:<30}'
                            f'{item["categoria"]:<20}'
                            f'{item["data"]:<12}'
                        )
                u.double_line()
                print(f'Total de registros: {num_registros}')
                return 'Lista retornada com sucesso!'
            else:
                return('Não existem entradas com a categoria indicada!')

    else:
        return('Nenhuma entrada foi registrada ainda! Nada para consultar!')

def buscar_por_periodo():
    '''
    user informa:
    -> data inicio
    -> data fim
    -> exibir lista
    -> contador de registro por categoria
    '''
    u.read_key()
    pass

def menu_entradas():
    while True:
        u.limpar_tela()
        u.double_line()
        print('ENTRADAS'.center(u.size,' '))
        u.double_line()
        print('1 - ADICIONAR ENTRADA')
        print('2 - EDITAR ENTRADA')
        print('3 - REMOVER ENTRADA')
        print('4 - LISTAR ENTRADAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        u.double_line()
        opcao = u.ler_opcao_menu(7)
        u.double_line()

        if opcao == 1:
            u.limpar_tela()
            msg = adicionar_entradas()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 2:
            u.limpar_tela()
            msg = editar_entradas()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 3:
            u.limpar_tela()
            msg = remover_entradas()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 4:
            u.limpar_tela()
            msg = listar_entradas()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 5:
            u.limpar_tela()
            msg = buscar_por_descricao()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 6:
            u.limpar_tela()
            msg = buscar_por_categoria()
            print(msg)
            u.double_line()
            u.read_key()

        elif opcao == 7:
            u.limpar_tela()
            buscar_por_periodo()
            u.double_line()
            u.read_key()

        elif opcao == 0:
            u.limpar_tela()
            break
        
if __name__ == '__main__':
    menu_entradas()
