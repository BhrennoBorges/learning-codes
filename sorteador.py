import random

nomes = []
while True:
    nome = input("Digite um nome para o sorteio (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

for numero in range(inicio, fim + 1):
    print(numero)

numero_sorteado = random.randint(inicio, fim)
print(f"Número sorteado: {numero_sorteado}")

if nomes:
    nome_sorteado = random.choice(nomes)
    print(f"Nome sorteado: {nome_sorteado}")
else:
    print("Nenhum nome foi inserido para o sorteio.")
