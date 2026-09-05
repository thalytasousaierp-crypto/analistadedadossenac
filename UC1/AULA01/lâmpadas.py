largura = 5
comprimento = 10
potencia_lampada = 10
area = 5 * 10
potencia_necessaria = area * 3
quantidade_bocais = area / 3

quantidade_lampadas =potencia_necessaria / potencia_lampada

resto = potencia_necessaria % potencia_lampada

if resto != 0:
    quantidade_lampadas +=1

print ("area:" , area)
print("potencia necessaria:", potencia_necessaria)
print("quantidade de bocais:" , quantidade_bocais)
print("quantidade de lampadas:", quantidade_lampadas)
