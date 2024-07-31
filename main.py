from my_functions import basico
from my_functions import appfunctions
from time import sleep

def menu_inicial() -> None:
    """
    Exibe o menu inicial e captura a opção do usuário.
    """

    def functions_menu_inicial(modo: int) -> None:
        """
        Executa a função correspondente à opção escolhida no menu.
        
        Parameters:
        modo (int): O número da opção escolhida pelo usuário.
        """
        basico.clear()
        if modo == 1:
            appfunctions.leitura_dados()
        elif modo == 2:
            appfunctions.exibir_estatisticas()
        elif modo == 3:
            appfunctions.adicionar_aluno()

    def contornar_erro():
        basico.clear()  # Limpa a tela
        print('Valor inválido.\033[1;31m Digite apenas os números válidos.\033[m')
        sleep(1)
        menu_inicial()  # Reexibe o menu em caso de erro

    # Exibe as opções do menu inicial
    print('''
STUDANT DATA ANALYSER
          
[1] Leitura de dados
[2] Exibir estatísticas
[3] Adicionar Aluno

Obs: Resposta em\033[1;33m números\033[m
    ''')

    number_selections = [1, 2, 3]  # Lista com as opções válidas

    try:
        escolha_modo = int(input('--> '))  # Captura a escolha do usuário
    except (ValueError, TypeError):
        contornar_erro()
    else:
        if escolha_modo in number_selections:
            functions_menu_inicial(escolha_modo)  # Executa a função correspondente à escolha
        else:
            contornar_erro()
            
def main() -> None:
    """
    Função principal que inicia o programa.
    """
    menu_inicial()

if __name__ == '__main__':
    # Executa a função principal se o script for executado diretamente
    main()
