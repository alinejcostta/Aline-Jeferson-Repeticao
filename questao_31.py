
# QUESTÃO 31

# 31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara

# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 8.00
# Dinheiro: R$ 20.00
# Troco: R$ 12.00


soma = 0
contador = 1
produtos = []

while True:
    preco_produto = float(input(f"Digite o preço do produto {contador}: "))
    if preco_produto == 0:
        break

    produtos.append(preco_produto)
    soma += preco_produto
    contador += 1

print(f"Total = R$ {soma:.2f}")
dinheiro = float(input("Dinheiro recebido: "))

troco = dinheiro - soma

print(f"------ Lojas Tabajara ------")

for i in range(len(produtos)):
    print(f"Produto {i+1}: R$ {produtos[i]:.2f}")

print(f"Total: R$ {soma:.2f}")
print(f"Dinheiro: R$ {dinheiro:.2f}")
print(f"Troco: {troco:.2f}")
print()
print("Agradecemos a preferência!")