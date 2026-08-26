odometro_inicial = 10000
odometro_final = 10200
litros = 20
valor_recebido = 500

km_percorridos = odometro_final - odometro_inicial
media_consumo = km_percorridos / litros 
custo_combustivel = litros * 6.15
lucro = valor_recebido - custo_combustivel

print("km_percorrios:", km_percorridos)
print("media_consumo:", media_consumo, "KM/L")
print("custo_combustivel: R$, custo_combustivel")
print("lucro liquido: R$", lucro)


