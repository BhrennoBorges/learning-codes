numeros = input("Digite os números separados por espaço: ").split()
contador = 0
while True:
    if contador >= len(numeros):
        break
    print(numeros[contador])
    contador += 1
soma = 0
for numero in numeros:
    soma += int(numero)
print("A soma dos números é:", soma)
