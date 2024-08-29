import datetime as dt
                    
def transfer(daily_trs, account_amt, transfer_op):
    if daily_trs == 10:
        print('limite diário de transações atingido')
    else:
        transfer_value = float(input("Digite o valor do depósito: "))
        if transfer_value <= 0:
            print("valor insuficiente. O valor precisa ser maior que 0")
        else:
            account_amt+=transfer_value
            transfer_value = str(f'{transfer_value:,.2f}')
            transfer_dt = dt.datetime.now()
            transfer_dt = transfer_dt.strftime("%H:%M %d/%m/%Y")
            transfer_value = "Valor de: " + transfer_value + " depositado as " + transfer_dt
            
            #Todos os depósitos devem ser armazenados em uma variável 
            transfer_op.append(transfer_value)
            print(transfer_value + "\n" + f"Novo saldo: R${account_amt:,.2f}")
            daily_trs+=1
            print (daily_trs)

def withdrawal(daily_trs, account_amt,withdrawal_op):
    if daily_trs == 10:
        print('limite diário de transações atingido')
    else: 
        withdrawal_value = float(input("Digite o valor do saque: "))
        if withdrawal_value <= 0:
            print("valor insuficiente. O valor precisa ser maior que 0")
        #Valor do saque deve ser de no máximo 500 reais por saque
        elif withdrawal_value > 500:
            print("valor ultrapassa o limite de saque. Favor informar um valor entre 1 e 500")
        #Caso o usuário não tenha saldo, sistema deve exibir mensagem informando a falta de saldo
        elif withdrawal_value > account_amt:
            print("Não foi possível efetuar o saque pois o valor informado é maior que o saldo em conta")

        #O sistema deve permitir apenas 3 saques diários
        elif withdrawal_value <= 500 and account_amt >= withdrawal_value:
            account_amt -=withdrawal_value
            withdrawal_value = str(f'{withdrawal_value:,.2f}')
            withdrawal_dt = dt.datetime.now()
            withdrawal_dt = withdrawal_dt.strftime("%H:%M %d/%m/%Y ")
            withdrawal_value = "Valor de: " + withdrawal_value + " sacado as " + withdrawal_dt

            withdrawal_op.append(withdrawal_value)
            print(withdrawal_value + "\n" + f"Novo saldo: R${account_amt:,.2f}")
            daily_trs+=1
            print(daily_trs)

def extract(transfer_op, withdrawal_op, account_amt):
    print(f"Extrato:\n")
    # O if verifica se há extrato de depósitos na conta, pois ela inicia zerada
    # e não é possível fazer outra operação sem ter feito algum depósito. 
    if len(transfer_op) > 0:
        print("Depósitos efetuados: ")
        for transfer in transfer_op:
            print(transfer)
        print("Saques efetuados: ")
        for withdrawal in withdrawal_op:
            print(withdrawal)
        print(f"Saldo atual: R$ {account_amt:,.2f}")
    else:
        #Se não houver movimentações sistema deve exibir mensagem
        print(f"Não foram realizadas movimentações.\n Saldo atual: R$ {account_amt:,.2f}")

while True:
    daily_trs = 0
    account_amt = 0.0
    transfer_op = []
    withdrawal_op = []
    option = input(f'''O que deseja fazer? 
                [d] - Depósito
                [s] - Saque
                [e] - verificar Extrato 
                [q] - Sair \n ''')
    
    if option == "d":
        transfer(daily_trs, account_amt, transfer_op)
    elif option == "s":
        withdrawal(daily_trs, account_amt, withdrawal_op)
    elif option == "e":
        extract(transfer_op, withdrawal_op, account_amt)
    elif option == "q":
        break
    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada")