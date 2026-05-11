
# QUESTÃO 24

# 24. Faça um programa que calcule o mostre a média aritmética de N notas.


soma = 0
media = 0

qtd_notas = int(input("Digite quantas notas deseja adicionar: "))

for i in range(qtd_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma/qtd_notas

print(f"A média é {media:.1f}")