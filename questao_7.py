
# QUESTÃO 7

# 7. Faça um programa que leia 5 números e informe o maior número.

maior = None

for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))

    if maior == None:
        maior = numero

    if numero > maior:
        maior = numero

print(f"O maior número é {maior}!")