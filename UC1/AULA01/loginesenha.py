usuario_correto = "alunopermanente@gmail.com"
senha_correta = "permanente123"

tentativas = 3

while tentativas > 0:
    usuario = input("digite seu usuario: ")
    senha = input ("digite sua senha: ")
    if usuario == usuario_correto and senha == senha_correta: 
     break
else:
    print ("login incorreto")
    tentativas -=1
    
    if tentativas == 2:
     print("Login bloqueado temporariamente")
     