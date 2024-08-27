account_amount = 0.0
transfer_amount = []
withdrawal_amount = []
daily_withdrawal = 0
while True:

    option = input('''O que deseja fazer? 
                [d] - Depósito
                [s] - Saque
                [e] - verificar Extrato 
                [q] - Sair \n''')
                        
    if option == 'd':
        transfer_value = float(input("Digite o valor do depósito: "))

        #Deve ser possível depositar valores positivos na conta
        if transfer_value <= 0:
            print("valor insuficiente. O valor precisa ser maior que 0")
        else:
            account_amount+=transfer_value
            #Todos os depósitos devem ser armazenados em uma variável 
            transfer_amount.append(transfer_value)
    elif option == 's':
        if daily_withdrawal == 3:
            print('limite diário de saques atingido')
        withdrawal_value = float(input("Digite o valor do saque: "))

        if withdrawal_value <= 0:
            print("valor insuficiente. O valor precisa ser maior que 0")

        #Valor do saque deve ser de no máximo 500 reais por saque
        elif withdrawal_value > 500:
            print("valor ultrapassa o limite de saque. Favor informar um valor entre 1 e 500")

        #Caso o usuário não tenha saldo, sistema deve exibir mensagem informando a falta de saldo
        elif withdrawal_value > account_amount:
            print("Não foi possível efetuar o saque pois o valor informado é maior que o saldo em conta")

        #O sistema deve permitir apenas 3 saques diários
        elif withdrawal_value <= 500 and account_amount >= withdrawal_value:
            account_amount -=withdrawal_value
            daily_withdrawal+=1
            withdrawal_amount.append(withdrawal_value)
        
    #Valores devem ser printados no extrato da conta            
    elif option == "e":
        print(f"Extrato:\n")
        if len(transfer_amount) > 0:

            print("Depósitos efetuados: ")
            for transfer in transfer_amount:
                print(f"{transfer:,.2f}")
            
            print("Saques efetuados: ")
            for withdrawal in withdrawal_amount:
                print(f"{withdrawal:,.2f}")
            
            print(f"Saldo atual: R$ {account_amount:,.2f}")

        else:
            #Se não houver movimentações sistema deve exibir mensagem
            print(f"Não foram realizadas movimentações.\n Saldo atual: R$ {account_amount:,.2f}")
            
    elif option == "q":
        break

    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada")

