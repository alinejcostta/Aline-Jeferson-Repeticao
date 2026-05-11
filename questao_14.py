
# QUESTÃO 14

# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


pares = 0
impares = 0

for i in range(1,11):
    num = int(input(f"Digite o número {i}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print (f"""
Quantidade de números pares: {pares}
Quantidade de números ímpares: {impares}
""")
