#Em Python, um método abstrato é um método definido 
# numa classe abstrata que tem uma assinatura (nome 
# e parâmetros), mas não possui implementação.

#Para criar um método abstrato, usa-se o decorador
#  @abstractmethod do módulo abc. 

from abc import ABC, abstractmethod
class Veiculo (ABC):
   @abstractmethod
   def ligar(self):
        pass
class Carro (Veiculo):
    def _init_(self, modelo, cor):
        self.modelo = modelo 
        self.cor = cor
class Caminhao (Veiculo):
    def _init_(self, modelo, cor, carga):
        self.modelo = modelo 
        self.cor = cor
        self.carga = carga
    
    def ligar(self):
        print("O carro está ligado.")

carro = Carro("Fusca", "Branco")
Carro.ligar
caminhao = Caminhao("Iveco", "Azul", 1000)
caminhao.ligar
