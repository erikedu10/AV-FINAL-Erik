# pedir o usuario para digita o seu salario.
salario = float(input(" insira o valor do seu salario: "))

# Garante que o salário inserido seja não negativo antes de prosseguir.
while salario < 0:
    print("\nPor favor, insira um salário valido.")
    salario = float(input("Digite novamente o valor do seu salário: "))

# Determina a faixa de salário do usuário e calcula o imposto.
# Se o salário for menor ou igual ha 2000 não há imposto
if salario <= 2000:
    print("Você esta isento de impostos.") 
# Salário entre 2000 e 3000, aplica-se 8% de imposto. 
elif 2000 < salario <= 3000:
    print(f"Seu imposto é de R$ {salario * 0.08:.2f}.")  
# Salário entre 3000 e 4500, aplica-se 18% de imposto.
elif 3000 < salario <= 4500:
    print(f"Seu imposto é de R$ {salario * 0.18:.2f}.")  
 # Para salários acima de 4500, aplica-se 28% de imposto.
else:
    print(f"Seu imposto é de R$ {salario * 0.28:.2f}.") 
    