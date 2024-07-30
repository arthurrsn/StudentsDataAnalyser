def menuInicial():
    print('''
STUDANT DATA ANALYSER
          
[1] Leitura de dados
[2] Exibir estatísticas
[3] Adicionar Aluno

Obs: Resposta em\033[1;33m números\033[m
    ''')

    while True:
        try:
            escolha_modo = int(input('--> '))
        except (ValueError, TypeError):
            print('Valor inválido.\033[1;31m Digite apenas números.\033[m')
            continue
        else:
            break

