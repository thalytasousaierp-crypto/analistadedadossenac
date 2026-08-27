for candidato in range(1, 13):
    print("candidato", candidato)
    ano_nascimento = int(input(" digite o ano do nascimento: "))
    idade = 2026 - ano_nascimento
    
    if idade < 18:
        print("não pode participar")
    continue
telefone = input("2199999999: ")
email = input ("candidato@gmail.com: ")

print("idade", idade)
print ("telefone:" , telefone)
print ("e-mail:", email)
print ("candidatocadastrado com sucesso!")
