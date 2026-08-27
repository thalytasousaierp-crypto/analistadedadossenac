num1 = float(input("digite seu primeiro numero"))
num2 = float(input("digite seu segundo nuero"))

operador=input("informe a operação desejada entre: 1. adição; 2. subtração; 3. multiplicação; 4 divisão;")
               
match operador:
 case "1":
   print(f"resultado da soma:(num1 + num2). ") 

 case "2":
     print(f"resultado da subtração:(num1 - num2). ") 
 
 case "3":
    print(f"resultado da multiplicação:(num1 * num2). ") 

 case "4":
    if num2!= 0:
        print("resultado da divisão: (num1 / num2). ")
    else:
        print (f"dividiu por zero. errou feio, errou rude!")
case_ :
print(f"informe um número de operador válido.")
    
return = resultado

    
 
calculinho = calculadora_v1(333, 555,operador = "1")

print (calculinho)

