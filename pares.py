soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break
    if numero % 2 == 0:
        soma += numero
        contador += 1
    

media = soma / contador

print(f"A média aritmética dos números pares é:{media:.2f}")