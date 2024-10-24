#media aritmética
''' Declare três variáveis num1, num2 e num3 e atribua a elas valores numéricos inteiros ou floats.
Calcule a média aritmética desses três números.
Use uma f-string para exibir o resultado no formato:
A média dos números X, Y e Z é igual a M. '''

num1 = 2
num2 = 4
num3 = 9

media = (num1+num2+num3)/3

print(f'A média dos números {num1}, {num2} e {num3} é igual a {media}.')

#conversor de unidades
''' Crie um programa que converte um período de tempo dado em dias, horas, minutos e segundos para o total de segundos. Siga os passos abaixo:
    
Declare quatro variáveis: dias, horas, minutos e segundos, atribuindo a elas valores inteiros.
Calcule o total de segundos considerando:
1 dia = 86.400 segundos
1 hora = 3.600 segundos
1 minuto = 60 segundos
Utilize a ordem correta das operações aritméticas para somar todos os segundos.
Use uma f-string para exibir o resultado no formato:
O total de segundos em X dias, Y horas, Z minutos e W segundos é igual a T segundos. '''

dias = 6
horas = 10
minutos = 30
segundos = 25

conversor = (86400*dias) + (3600*horas) + (60*minutos) + segundos

print(f'O total de segundos em {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos é igual a {conversor} segundos.')