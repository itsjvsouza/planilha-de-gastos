from src.interface import MENU_PRINCIPAL, MENU_DATA, MENU_PAGAMENTO, MENU_CONFIRMACAO, MENU_REPETIR_GASTO, MENU_MES, MENU_REPETIR_CONSULTA, MENU_EXCLUIR
from datetime import datetime, date
import os
os.system('cls')

while True:

    inicio = int(input(MENU_PRINCIPAL))

    if inicio == 1:

        while True:
            escolha = int(input(MENU_DATA))

            if escolha == 1:
                data = date.today()
                data_usuario = data.strftime('%d/%m/%Y')
                
            elif escolha == 2:
                data_usuario = str(input('Digite a data (DD/MM/YYYY): '))
                data_obj = datetime.strptime(data_usuario, '%d/%m/%Y')
                data = data_obj.strftime('%Y-%m-%d')

            elif escolha == 3:
                break

            else:
                print('\nAção inválida.')
                continue

            descricao = str(input('\nDescrição: '))
            valor = float(input('\nValor: R$'))
            forma = str(input(MENU_PAGAMENTO))

            if forma == '1':
                forma = 'Pix'
            
            elif forma == '2':
                forma = 'Crédito'

            confirmacao = int(input(f"{data_usuario}, {descricao}, R${valor}, {forma}" + MENU_CONFIRMACAO))

            if confirmacao == 1:
                linha = (f'{data},{descricao},{valor},{forma}\n')

                with open('data/gastos.csv', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(linha)
                
                print('\n\n\033[1;32mGasto salvo com sucesso!\033[m')
                
                pergunta = int(input(MENU_REPETIR_GASTO))

                if pergunta == 1:
                    continue
                
                else:
                    break

            else:
                continue
    
    elif inicio == 2:
        
        while True:
            escolha = int(input(MENU_MES))
            print()

            if escolha >= 1 and escolha <=12:  
                with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

                total = 0

                for linha in linhas:
                    partes = linha.split(',')
                    valor = float(partes[2])
                    data_str = partes[0]
                    data = datetime.strptime(data_str, '%Y-%m-%d')
                    
                    if data.month == escolha:
                        print(linha)

                        total = total + valor

                print(f'\nTotal gasto no mês: R${total}')
                
                pergunta = int(input(MENU_REPETIR_CONSULTA))

                if pergunta == 1:
                    continue
                
                else:
                    break

            elif escolha == 13:
                break

            else:
                print('Opção inválida.')
                continue
    
    elif inicio == 3:
        
        escolha = int(input(MENU_EXCLUIR))

        if escolha >= 1 and escolha <= 12:
            with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()

            for i, linha in enumerate(linhas):
                partes = linha.split(',')
                data_str = partes[0]
                data = datetime.strptime(data_str, '%Y-%m-%d')
                
                if data.month == escolha:
                    print(f'\n{i + 1} - {linha}')
                
                else:
                    
            
            excluir = int(input('\nDigite o número do gasto que deseja excluir: '))

            if excluir >= 1 and excluir <= len(linhas):
                del linhas[excluir - 1]

                with open('data/gastos.csv', 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas)

                print('\n\033[1;32mGasto excluído com sucesso!\033[m')

            else:
                print('\nNúmero inválido.')

    elif inicio == 4:
        break

    else:
        print('\nAção inválida.')
