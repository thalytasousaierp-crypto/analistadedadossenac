nota1 = 4
nota2 = 5
nota_optativa = 8

if  nota_optativa != -1:
 if nota1 < nota2:
else:
 nota2 = nota_optativa
 
 media = (nota1 + nota2) / 2
print ("média:", media)

if media >= 6:
 print("aprovado")
elif media < 3:
 print("reprovado")
else:
 print("recuperacao")
