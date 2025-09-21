# Dicionário com velocidades máximas
carros_velocidade = {
    "mobi": 160,
    "onix": 167,
    "hb20": 170,
    "gol": 180,
    "golf": 220,
    "kwid": 156,
    "ferrari f80": 350
}

# Definição da classe Carro
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0
        self.velocidade_maxima = carros_velocidade.get(modelo.lower(), 180)

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} de cor {self.cor} está ligado.")
        else:
            print(f"O {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            if self.velocidade == 0:
                self.ligado = False
                print(f"O {self.modelo} está desligado.")
            else:
                print(f"Não pode desligar em movimento. Velocidade atual: {self.velocidade} km/h.")
        else:
            print(f"{self.modelo} já está desligado.")

    def acelerar(self, valor):
        if self.ligado:
            if self.velocidade + valor > self.velocidade_maxima:
                self.velocidade = self.velocidade_maxima
                print(f"{self.modelo} atingiu a velocidade máxima de {self.velocidade_maxima} km/h!")
            else:
                self.velocidade += valor
                print(f"{self.modelo} acelerou para {self.velocidade} km/h.")
        else:
            print(f"Não é possível acelerar. O {self.modelo} está desligado.")

    def frear(self, valor):
        if self.velocidade - valor >= 0:
            self.velocidade -= valor
            print(f"{self.modelo} freou para {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print(f"{self.modelo} parou.")



def comparar_carros(meu_carro, ferrari):
    if not meu_carro.ligado or not ferrari.ligado:
        print("Ambos os carros precisam estar ligados para começar a comparação.")
        return

    while meu_carro.velocidade < meu_carro.velocidade_maxima or ferrari.velocidade < ferrari.velocidade_maxima:
        if meu_carro.velocidade < meu_carro.velocidade_maxima:
            meu_carro.acelerar(5)
        if ferrari.velocidade < ferrari.velocidade_maxima:
            ferrari.acelerar(10)

        if meu_carro.velocidade == meu_carro.velocidade_maxima and ferrari.velocidade == ferrari.velocidade_maxima:
            break

    print("\n--- Resultado da corrida ---")
    print(f"{meu_carro.modelo} terminou a {meu_carro.velocidade} km/h.")
    print(f"{ferrari.modelo} terminou a {ferrari.velocidade} km/h.")
    if ferrari.velocidade > meu_carro.velocidade:
        print("A Ferrari venceu!")
    elif ferrari.velocidade < meu_carro.velocidade:
        print("Você venceu!")
    else:
        print("Empate!")


# Interface
print("""fiat mobi
chevrolet onix
hyundai hb20
volkswagen gol
volkswagen golf
renault kwid""")

modelo = input("Escolha um modelo de cima: ")
cor = input("Informe a cor do carro: ")

meu_carro = Carro(cor, modelo)
ferrari = Carro("vermelha", "Ferrari F80")

while True:
    opcao = int(input("""
1 - Ligar Carro
2 - Frear Carro
3 - Desligar Carro
4 - Acelerar
5 - Começar a comparação com a Ferrari
6 - Sair
"""))

    if opcao == 1:
        meu_carro.ligar()
        ferrari.ligar()
    elif opcao == 2:
        meu_carro.frear(5)
    elif opcao == 3:
        meu_carro.desligar()
    elif opcao == 4:
        meu_carro.acelerar(5)
    elif opcao == 5:
        comparar_carros(meu_carro, ferrari)
    else:
        break
