# mostra há mensagem para o usuario
print("cofre")
#armazenar o valor da senha.
senha = 2002
#pedir que o usuario digite a sua senha.
tentativa = int(input("digite a senha"))
#ver se o usuario botou a senha correta se não, bota senha novamente
while tentativa != senha:
    print("senha incorreta")
# se há senha tiver correta, finalizar o codigo
    tentativa = int(input("digite a senha"))
print("acesso valido")