from datetime import datetime, date
import os
os.system('cls')

while True:

    inicio = int(input('\n1 - Adicionar gasto \n2 - Consultar gastos \n3 - Excluir gasto \n4 - Encerrar \n\nDigite o número correspondente à ação desejada: '))

    if inicio == 1:

        while True:
            d = int(input('\n1 - Utilizar data de hoje \n2 - Digitar data \n3 - Voltar \n\nOpção: '))

            if d == 1:
                data = date.today()
                data_usuario = data.strftime('%d/%m/%Y')
                
            elif d == 2:
                data_usuario = str(input('Digite a data (DD/MM/YYYY): '))
                data_obj = datetime.strptime(data_usuario, '%d/%m/%Y')
                data = data_obj.strftime('%Y-%m-%d')

            elif d == 3:
                break

            else:
                print('\nAção inválida.')
                continue

            descricao = str(input('\nDescrição: '))
            valor = float(input('\nValor: R$'))
            forma = str(input('\n1 - Pix \n2 - Crédito \n\nForma de pagamento: '))

            if forma == '1':
                forma = 'Pix'
            
            elif forma == '2':
                forma = 'Crédito'

            confirmacao = int(input(f'\n{data_usuario}, {descricao}, R${valor}, {forma} \n\n1 - Sim \n2 - Não \n\nOs dados estão corretos? '))

            if confirmacao == 1:
                linha = (f'{data},{descricao},{valor},{forma}\n')

                with open('data/gastos.csv', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(linha)
                
                print('\n\n\033[1;32mGasto salvo com sucesso!\033[m')
                
                pergunta = int(input('\n\nDeseja adicionar outro gasto? \n\n1 - Sim \n2 - Não \n\nOpção: '))

                if pergunta == 1:
                    continue
                
                else:
                    break

            else:
                continue
    
    elif inicio == 2:
        
        while True:
            m = int(input('\n1 - Janeiro \n2 - Fevereiro \n3 - Março \n4 - Abril \n5 - Maio \n6 - Junho \n7 - Julho \n8 - Agosto \n9 - Setembro \n10 - Outubro \n11 - Novembro \n12 - Dezembro \n13 - Voltar \n\nConsultar gastos de que mês? '))
            print()

            if m >= 1 and m <=12:  
                with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

                total = 0

                for linha in linhas:
                    partes = linha.split(',')
                    valor = float(partes[2])
                    data_str = partes[0]
                    data = datetime.strptime(data_str, '%Y-%m-%d')
                    
                    if data.month == m:
                        print(linha)

                        total = total + valor

                print(f'\nTotal gasto no mês: R${total}')
                
                pergunta = int(input('\n\nDeseja consultar outro gasto? \n\n1 - Sim \n2 - Não \n\nOpção: '))

                if pergunta == 1:
                    continue
                
                else:
                    break

            elif m == 13:
                break

            else:
                print('Opção inválida.')
                continue
    
    elif inicio == 3:
        with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            print(f'{i + 1} - {linha}')
        
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
