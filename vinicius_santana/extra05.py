
from abc import ABC, abstractmethod

# Classe Abstrata: Representa a abstração de um funcionário genérico
class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        # Encapsulamento: Atributos privados
        self.__nome = nome
        self.__salario_base = salario_base

    def get_nome(self):
      return self.__nome

    
    def get_salario_base(self):#Precisa usar ele para evitar o erro
      return self.__salario_base   
    
    @abstractmethod
    def calcular_salario_bruto(self):
        pass
    
    
# Herança: Classe Gerente herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.__bonus = bonus

    def calcular_salario_bruto(self):
        # Polimorfismo: Implementação específica para Gerente
        return self.get_salario_base() + self.__bonus

# Herança: Classe Desenvolvedor herda de Funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario_base, horas_extras):
        super().__init__(nome, salario_base)
        self.__horas_extras = horas_extras
        self.__valor_hora = 50.0

    def get_horas_extras(self):
        return self.__horas_extras
   
    def get_valor_hora(self):
        return self.__valor_hora
    
    def calcular_salario_bruto(self):
        # Polimorfismo: Implementação específica para Desenvolvedor
        return self.get_salario_base() + (self.get_horas_extras() * self.get_valor_hora())

# Agregação: A Empresa "agrega" vários funcionários
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def processar_folha_pagamento(self):
        print(f"Processando folha de pagamento da {self.nome}:")
        for funcionario in self.lista_funcionarios:
            try:
                # Polimorfismo em ação: cada objeto chama seu próprio método
                salario = funcionario.calcular_salario_bruto()
                print(f"- {funcionario.get_nome()}: R${salario:.2f}")
            except Exception as e:
                # Tratamento de Exceções
                print(f"Erro ao processar salário de {funcionario.get_nome()}: {e}")
    def descontos(self):
       print(f"Processando folha de pagamento com descontos {self.nome}:")
       for funcionario in self.lista_funcionarios:
            
            try:
                bruto = funcionario.calcular_salario_bruto()
                imposto = bruto * 0.11 
                inss = bruto * 0.08
                sindicato = bruto * 0.05
                total = imposto + inss + sindicato
                salario_liquido =  bruto - total 
                print(f"- {funcionario.get_nome()}: R${salario_liquido:.2f}")
            except Exception as e:
                print(f"Erro ao processar salário de {funcionario.get_nome()}: {e}")
        



# Exemplo de uso
empresa = Empresa("Tech Solutions")
gerente = Gerente("Ana", 8000, 2000)
dev = Desenvolvedor("João", 5000, 10)


empresa.adicionar_funcionario(gerente)
empresa.adicionar_funcionario(dev)

empresa.processar_folha_pagamento()
empresa.descontos()