import time
import entradas as ent
import despesas as des
import categorias as cat
import relatorios as rel
import estatisticas as est
import visualizacoes as views
import analises as anl
import metas as met
import utils as u

def main_menu():
    while True:
        u.limpar_tela()
        u.line()
        print('--- CARTEIRA DE GABRIEL ---')
        u.line()
        print('1 - ENTRADAS')
        print('2 - DESPESAS')
        print('3 - CATEGORIAS')
        print('4 - RELATÓRIOS')
        print('5 - ESTATÍSTICAS')
        print('6 - VISUALIZAÇÕES')#graficos
        print('7 - ANÁLISES AUTOMÁTICAS')
        print('8 - METAS FINANCEIRAS')
        print('0 - SALVAR E SAIR')
        u.line()
        opcao = input('Digite a opção desejada: ')
        u.line()
        if opcao == '1':
            ent.menu_entradas()
        elif opcao == '2':
            des.menu_despesa()
        elif opcao == '3':
            cat.menu_categorias()
        elif opcao == '4':
            rel.menu_relatorio()
        elif opcao == '5':
            est.menu_estatisticas()
        elif opcao == '6':
            views.menu_visualizacoes()
        elif opcao == '7':
            anl.menu_analises()
        elif opcao == '8':
            met.menu_metas()
        elif opcao == '0':
            print('Salvando...')
            u.pause()
            break

if __name__ == '__main__':

    print('Iniciando...')
    time.sleep(1)
    print('Carregando Arquivos e Dados...')
    time.sleep(1)
    print('Pronto')
    main_menu()