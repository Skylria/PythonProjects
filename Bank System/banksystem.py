import datetime as dt
account_amt = 0.0
receipt_list = [] 

# def create_user():


def transfer(account_amt, receipt_list, transfer_value):
    if len(receipt_list) == 10:
        print('limite diário de transações atingido')
    elif transfer_value <= 0:
        print("valor insuficiente. O valor precisa ser maior que 0")
    else:
        account_amt+=transfer_value
        transfer_value = str(f'{transfer_value:,.2f}')
        transfer_dt = dt.datetime.now()
        transfer_dt = transfer_dt.strftime("%H:%M %d/%m/%Y")
        transfer_value = "Valor de: " + transfer_value + " depositado as " + transfer_dt
        print(transfer_value + "\n" + f"Novo saldo: R${account_amt:,.2f}")
    return account_amt, transfer_value

def withdrawal(account_amt,receipt_list, withdrawal_value):
    if len(receipt_list) == 10:
        print('limite diário de transações atingido')
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
        print(withdrawal_value + "\n" + f"Novo saldo: R${account_amt:,.2f}")
    return account_amt, withdrawal_value

def extract(account_amt, /, *, receipts):
    print(f"Extrato:\n")
    if len(receipts) > 0:
        for receipt in receipts:
            print(receipt)
        print(f"Saldo atual: R$ {account_amt:,.2f}")
    else:
        print(f"Não foram realizadas movimentações.\n Saldo atual: R$ {account_amt:,.2f}")

while True:

    option = input(f'''O que deseja fazer? 
                [d] - Depósito
                [s] - Saque
                [e] - verificar Extrato 
                [q] - Sair \n ''')
    
    if option == "d":
        transfer_value = float(input("Digite o valor do depósito: "))
        result = transfer(account_amt, receipt_list, transfer_value)
        account_amt = result[0]
        receipt_list.append(result[1])
    elif option == "s":
        withdrawal_value = float(input("Digite o valor do saque: "))
        result_w = withdrawal(account_amt, receipt_list, withdrawal_value)
        account_amt = result_w[0]
        receipt_list.append(result_w[1])
    elif option == "e":
        extract(account_amt, receipts = receipt_list)
    elif option == "q":
        break
    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada")