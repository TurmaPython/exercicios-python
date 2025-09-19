import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(2, 3), 5)
        self.assertEqual(calc.somar(-1, 1), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# ou pode ser por esse método:

'''
import unittest

class Calculadora:
	def somar(self, a, b):
    	return a + b

class TestCalculadora(unittest.TestCase):
	def test_somar(self):
    	calc = Calculadora()
    	with open('testes.txt', 'r') as arquivo:
        	conteudo = arquivo.readlines()
        	for linha in conteudo:
            	valores = linha.split(";")
            	self.assertEqual(calc.somar(float(valores[0]), float(valores[1])), float(valores[2])
   	 
if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)

'''