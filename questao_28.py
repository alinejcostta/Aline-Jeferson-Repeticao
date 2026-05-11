
# QUESTÃO 28

# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.


soma = 0
qtd_cds = int(input("Digite a quantidade de CDs que você possui: "))

for i in range(1, qtd_cds+1):
    valor_cds = float(input(f"Digite o valor do CD {i}: "))
    soma += valor_cds

media = soma/qtd_cds

print(f"Você possui {qtd_cds} CDs com um valor total investido de R${soma:.2f} e valor médio gasto de R$ {media:.2f}")