
# QUESTÃO 46

# 46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Melhor salto: 6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
# Resultado final:
# Rodrigo Curvêllo: 5.9 m


saltos = []
maior_salto = 0
menor_salto = 0

nome = input("Digite o nome do atleta: ")

for i in range(5):
    salto = float(input(f"Salto {i+1}: "))
    saltos.append(salto)

print("""
Resultado final:
--- Dados de Saltos ---
""")
for i in range(len(saltos)):
    print(f"Salto {i+1}: {saltos[i]:.1f} m")

maior_salto = max(saltos)
menor_salto = min(saltos)

saltos.remove(maior_salto)
saltos.remove(menor_salto)

media = sum(saltos)/len(saltos)

print(f"""
Atleta: {nome}
Melhor nota: {maior_salto:.1f} m
Pior nota: {menor_salto:.1f} m
Média: {media:.1f} m
""")
