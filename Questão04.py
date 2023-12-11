
# mostra uma mensagem inicial para usuário
print("Descubra de onde é seu DDD\n")
# Solicita que o usuário digite o número de telefone brasileiro
numero = int(input(f"Digite seu número de telefone (brasileiro)\nObs: Não utilize espaços ou sinais: "))
# verificar os dois primeiros dígitos do número, que representam o DDD
ddd = int(str(numero)[:2])
# Verifica a qual região pertence o DDD
if ddd == 61:
    print("Brasília")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("São Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitória")
elif ddd == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")