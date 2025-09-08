#TAREFA DE CASA: IMPLEMENTAR PARA FAZER COM QUE O CARRO NÃO DESLIGUE QUANDO ESTIVER EM VELOCIDADE!
# Definindo a classe Carro
class Carro:
    # O método construtor __init__ inicializa os atributos do objeto.
    # self.cor e self.modelo são os atributos da classe.
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False # Atributo para verificar o estado do carro
        self.velocidade = 0 # Atributo para controlar a velocidade

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} de cor {self.cor} está ligado.")
        else:
            print(f"O {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0 # A velocidade zera ao desligar
            print(f"O {self.modelo} está desligado.")
        else:
            print(f"O {self.modelo} já está desligado.")

    # Método para acelerar o carro
    def acelerar(self, valor):
        if self.ligado:
            self.velocidade += valor
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h.")
        else:
            print(f"Não é possível acelerar. O {self.modelo} está desligado.")
    
    # Método para frear o carro
    def frear(self, valor):
        if self.velocidade - valor >= 0:
            self.velocidade -= valor
            print(f"Freando... Velocidade atual: {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print("Freando... O carro parou.")

# ======================================================================
# Criando objetos e interagindo com eles
# ======================================================================

# Criando um objeto (instância) da classe Carro
meu_carro = Carro("Preto", "Fusca")

# Acessando os atributos do objeto
print(f"Cor do meu carro: {meu_carro.cor}")
print(f"Modelo do meu carro: {meu_carro.modelo}")

# Chamando os métodos do objeto para interação
meu_carro.ligar()
meu_carro.acelerar(50)
meu_carro.acelerar(30)
meu_carro.frear(60)
meu_carro.desligar()
meu_carro.ligar()