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

def mainMenu():
    while True:
        u.limparTela()
        print('===============================')
        print('--- CARTEIRA DE GABRIEL ---')
        print('===============================')
        print('1 - ENTRADAS')
        print('2 - DESPESAS')
        print('3 - CATEGORIAS')
        print('4 - RELATÓRIOS')
        print('5 - ESTATÍSTICAS')
        print('6 - VISUALIZAÇÕES')#graficos
        print('7 - ANÁLISES AUTOMÁTICAS')
        print('8 - METAS FINANCEIRAS')
        print('0 - SALVAR E SAIR')
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == 1:
            ent.menuEntradas()
        elif opcao == 2:
            des.menuDespesa()
        elif opcao == 3:
            cat.menuCategorias()
        elif opcao == 4:
            rel.menuRelatorio()
        elif opcao == 5:
            est.menuEstatisticas()
        elif opcao == 6:
            views.menuVisualizacoes()
        elif opcao == 7:
            anl.menuAnalises()
        elif opcao == 8:
            met.menuMetas()
        elif opcao == 0:
            print('Salvando...')
            u.pause()
            break

if __name__ == '__main__':

    print('Iniciando...')
    time.sleep(1)
    print('Carregando Arquivos e Dados...')
    time.sleep(1)
    print('Pronto')
    mainMenu()