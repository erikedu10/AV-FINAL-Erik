#mostra há mensagem para usuario
print("Descubra a média de valores positivos.")
#lista dos "numeros" e da variavel "positivo"
numeros = []
positivo=0
#repete os 5 numeros
for i in range(0,5):
#pede um valor para ser colocado na variavel "numero"
    numero = float(input(f'Digite o {i+1}° número: '))
# se o numero for maior que 0 adicionar '"1" variavel positivo, e coloca na lista de "numeros
    if numero>0:
        positivo = positivo+1
        numeros.append(numero)
#soma os numeros da lista "numeros"      
soma = sum(numeros)
#mostra quantidade de valores positivos
print(f"{positivo} valores positivos")
#mostra há media da lista "numero"
print(f"{soma/5}")