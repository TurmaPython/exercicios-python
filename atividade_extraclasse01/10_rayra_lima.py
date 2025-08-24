dividendo = int(input("Digite o valor do dividendo: "))
divisor = int(input("Digite o valor do divisor: "))
resto = dividendo % divisor
if divisor == 0:
    print("Divisão por zero não é permitida.")
else:
    if dividendo % divisor == 0:
        print(f"{dividendo} é divisível por {divisor}.")
    else:
        print(f"{dividendo} não é divisível por {divisor}.")
        print(f"O resto da divisão é: {resto}")
