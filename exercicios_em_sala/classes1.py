# self significa "meu mesmo" e é usado para referenciar atributos e métodos dentro da própria classe.
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor # Atributo de instância
        self.modelo = modelo # Atributo de instância
    def ligar(self): # Método de instância
        print(f"O {self.modelo} está ligado.")

# Criando instâncias da classe Carro
meu_carro = Carro("Branco", "Fusca")
print(f"Cor do meu carro: {meu_carro.cor}")
print(f"Modelo do meu carro: {meu_carro.modelo}")
meu_carro.ligar()

# Criando outra instância da classe Carro
meu_edu = Carro("Parata", "Uno")
print(f"Cor do carro do edu: {meu_edu.cor}")
print(f"Modelo do carro do edu: {meu_edu.modelo}")
meu_edu.ligar()