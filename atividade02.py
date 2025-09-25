list_nomes = ['samuel','pedro','André','João', 'Crisitiano']
#pesquisa
nomes = input('Digite o nome que deseja procurar: ').lower()
while True:
    if nomes in list_nomes:
        print(nomes)
    else:
        print('Nome não encontrado')
    while True:
        escolha = input('Deseja adicionar um novo nome?\nS - Sim\nN - Não: ').lower()
        if escolha == 's':
                nome2 = input('Digite o nome: ').lower()
                list_nomes.append(nome2)
        else:
                break
        print(list_nomes)
        remover = input('Deseja remover algum nome da lista?\nS - Sim\nN - Não: ')
        if remover == 's':
                nome3 = input('Digite o nome que vai ser excluido: ')
                if nome3 in list_nomes:
                    list_nomes.remove(nome3)
                else:
                    print('Esse nome nao está na lista!!')

    sair = input('Deseja continuar procurando nomes?\nS - Sim\nN - Não: ').lower()
    if sair !='s':
            break
print(f'Lista final de nomes: {list_nomes}')
#CRESCENTE
numeros = []

while True:
    try:

        entrada = input("Digite um número (ou 'sair' para terminar): ")

        if entrada.lower() == 'sair':
            break


        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido!")


numeros.sort()


print("\nLista de números em ordem crescente:")
for numero in numeros:
    print(numero)
#Média de notas
notas = []
quantidade = int(input("Quantas notas deseja inserir? "))
for i in range(quantidade):
    while True:
            try:
                nota = float(input(f"Digite a nota {i+1} (entre 0 e 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print(" A nota deve estar entre 0 e 10.")
            except ValueError:
                print(" Entrada inválida. Digite um número.")

    media = sum(notas) / len(notas)
    print(f"\nMédia do aluno: {media:.2f}")

    if media >= 7:
        print(" Aluno aprovado!")
    else:
        print(" Aluno reprovado.")


