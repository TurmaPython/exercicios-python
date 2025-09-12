# Exercíco: Utilizar um método de laço com as classes
#vamos utilizar o Wile()

while True:
    class Carro:
        def __init__(self, cor, modelo, ano):
            self.cor = cor
            self.modelo = modelo
            self.ligado = False
            self.velocidade = 0

        def ligar(self):
            if not self.ligado:
                self.ligado = True
                print(f"O {self.modelo} de cor {self.cor} está ligado.")
            else:
                print(f"O {self.modelo} já está ligado.")

        def desligar(self):
            if self.ligado:
                self.ligado = False
                self.velocidade = 0
                print(f"O {self.modelo} está desligado.")
            else:
                print(f"O {self.modelo} já está desligado.")

        def acelerar(self, valor):
            if self.ligado:
                self.velocidade += valor
                print(f"Acelerando... Velocidade atual: {self.velocidade} km/h.")
            else:
                print(f"Não é possível acelerar. O {self.modelo} está desligado.")

        def ferar(self, valor):
            if self.velocidade -valor >= 0:
                self.velocidade -= valor
                print(f"Freando... Velocidade atual: {self.velocidade} km/h.")
            else:
                self.velocidade = 0
                print("Freando... O carro parou.")
    break

meu_carro = Carro("Preto", "Fusca")

print(f"Cor do meu carro: {meu_carro.cor}")
print(f"Modelo do meu carro: {meu_carro.modelo}")

meu_carro.ligar()
meu_carro.acelerar(50)
meu_carro.acelerar(30)
meu_carro.frear(60)
meu_carro.desligar()
meu_carro.ligar()