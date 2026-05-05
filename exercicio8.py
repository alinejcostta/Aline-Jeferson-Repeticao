
# QUESTÃO 8

# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))
    soma += numero

media = soma/5

print(f"A soma é {soma} e a média é {media}!")