''' Crie uma lista vazia chamada tarefas.
Adicione três tarefas à lista usando o método .append().
Mostre todas as tarefas presentes na lista usando um loop for.
Peça ao usuário que remova uma das tarefas fornecendo o índice da tarefa a ser removida.
Remova a tarefa da lista usando o índice fornecido e mostre a lista atualizada de tarefas. '''

tarefas = list()
tarefas.append("Regar as plantas")
tarefas.append("Lavar os pratos")
tarefas.append("estudar python")

def remover_tarefa(indice):
    for tarefa in tarefas:
        print(tarefa)
    tarefas.remove(tarefas[indice])
    print(f'tarefa {indice} removida')
    for tarefa in tarefas:
        print(tarefa)

print('informe o índice da tarefa que deseja remover: ')
indice = int(input())

remover_tarefa(indice)

''' Crie um programa que armazena informações sobre três estudantes usando dicionários. Para cada estudante, armazene seu nome, idade e curso. Siga os passos abaixo:
    
Crie três dicionários, um para cada estudante, contendo as seguintes chaves: "nome", "idade", "curso".
Armazene todos os dicionários em uma lista chamada estudantes.
Utilize um loop for para exibir as informações de cada estudante no seguinte formato:
Nome: <nome>
Idade: <idade>
Curso: <curso>
Adicione um quarto estudante solicitando os dados ao usuário (input()) e, em seguida, inclua-o na lista estudantes.
Exiba a lista completa de estudantes atualizada. '''

estudante1 = {'nome': 'jaum', 'idade': 21, 'curso': 'computação'}
estudante2 = {'nome': 'sheila', 'idade': 23, 'curso': 'gastronomia'}
estudante3 = {'nome': 'ricardo', 'idade': 21, 'curso': 'engenharia'}
estudantes = [estudante1, estudante2, estudante3]

def add_estudante(lista):
    print('nome: ')
    nome_estudante = input()
    print('idade: ')
    idade_estudante = input()
    print('curso: ')
    curso_estudante = input()
    novo_estudante = dict(nome = nome_estudante, idade = idade_estudante, curso = curso_estudante)
    estudantes.append(novo_estudante)
    for estudante in estudantes:
        print(f''' 
            nome: {estudante['nome']}
            idade: {estudante['idade']} 
            curso: {estudante['curso']}''')

add_estudante(estudantes)

''' Escreva um programa que lê uma lista de números inteiros e, para cada número, verifica se ele é positivo, negativo ou zero. Siga os passos abaixo:
    
Crie uma lista de 10 números inteiros variados, incluindo positivos, negativos e zeros.
Utilize um loop for para iterar sobre os números da lista.
Para cada número, use uma estrutura condicional (if, elif, else) para verificar se o número é positivo, negativo ou zero.
Exiba uma mensagem para cada número no formato:
<número> é positivo
<número> é negativo
<número> é zero
Ao final, exiba a quantidade de números positivos, negativos e zeros presentes na lista.'''

numeros = [2,34, 656, -234, -7, 0, 28, 0, -1, 0]

def verifica_numeros(lista):
    positivos = 0
    negativos = 0
    zeros = 0
    for numero in numeros:
        if numero < 0:
            print(f'{numero} é negativo')
            negativos+=1
        elif numero == 0:
            print(f'{numero} é zero')
            zeros+=1
        else:
            print(f'{numero} é positivo')
            positivos+=1
    print(f'Há {positivos} números positivos, {negativos} números negativos e {zeros} zeros na lista')

verifica_numeros(numeros)