# Pede usuario digitar o seu salário
salario = float(input("Digite seu salário: "))
# Se o salário for menor que 400, aumenta em 15%
if salario < 400.00:
    print(f"Novo salário: {salario + (salario * 0.15):.2f}")
    print(f"Reajuste ganho: {salario * 0.15:.2f}")
    print("Em percentual: 15 %")
# Se o salário estiver entre 400.01 e 800, aumenta em 12%
elif 400.01 < salario < 800.00:
    print(f"Novo salário: {salario + (salario * 0.12):.2f}")
    print(f"Reajuste ganho: {salario * 0.12:.2f}")
    print("Em percentual: 12 %")
# Se o salário estiver entre 800.01 e 1200, aumenta em 10%
elif 800.01 < salario < 1200.00:   
    print(f"Novo salário: {salario + (salario * 0.10):.2f}")
    print(f"Reajuste ganho: {salario * 0.10:.2f}")
    print("Em percentual: 10 %")
# Se o salário estiver entre 1200.01 e 2000, aumenta em 7%
elif 1200.01 < salario < 2000.00:
    print(f"Novo salário: {salario + (salario * 0.07):.2f}")
    print(f"Reajuste ganho: {salario * 0.07:.2f}")
    print("Em percentual: 7 %")
# Se o salário for maior que 2000.01, aumenta em 4%
elif salario > 2000.01:
    print(f"Novo salário: {salario + (salario * 0.04):.2f}")
    print(f"Reajuste ganho: {salario * 0.04:.2f}")
    print("Em percentual: 4 %")
