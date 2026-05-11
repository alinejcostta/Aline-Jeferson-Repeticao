
# QUESTÃO 33

# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.


qtd_temperaturas = int(input("Digite quantas temperaturas serão informadas: "))

soma_temperaturas = 0
maior_temperatura = None
menor_temperatura = None
historico = ""

for i in range(qtd_temperaturas):
    temperatura = float(input("Digite a temperatura: "))

    historico += f"{i+1}. {temperatura}°C\n"
    soma_temperaturas += temperatura

    if maior_temperatura == None:
        maior_temperatura = temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura
    if menor_temperatura == None:
        menor_temperatura = temperatura
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

media_temperatura = soma_temperaturas/qtd_temperaturas

print(f"""
--- Dados do Dia ---
    Menor temperatura: {menor_temperatura}°C
    Maior temperatura: {maior_temperatura}°C
    Média diária: {media_temperatura}°C
""")