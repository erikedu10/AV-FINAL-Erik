# mostra mensagem para o usuário
print("Contagem de números pares")
# Inicia uma variável para contar os números pares
contagem_pares = 0
# pedir os 5 numeros para usuario
for i in range(0, 5): 
# pedir que o usuário digitar o número
    numero = int(input(f"Digite o {i+1}° número: "))
# Verifica se o número inserido é par
    if numero % 2 == 0:
# Se for par, incrementa a contagem
        contagem_pares = contagem_pares + 1
# mostrar o resultado da contagem de números pares
print(f"Você digitou {contagem_pares} números pares.")