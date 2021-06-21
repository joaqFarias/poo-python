import unittest
import numpy as np

def fibonacci(numero: int) -> int: 
    if numero <= 0: 
        return "NA"
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

class fibonacciTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(fibonacci(5), 3, msg="se calcula mal la secuencia de fibonacci")

    def testTwo(self):
        self.assertEqual(fibonacci(0), "NA", msg="No admite 0")

    def testThree(self):
        self.assertEqual(fibonacci(1), 0, msg="no admite 1")

    def testFour(self):
        self.assertEqual(fibonacci(-1), "NA", msg="no admite negativos")

    def testFive(self):
        self.assertEqual(fibonacci(10), 34, msg="se calcula mal la secuencia de fibonacci")

    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp
    def setUp(self):
        # agrega las tareas setUp
        print("Se incian las pruebas")
            
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown
        print("Finalizan las pruebas")


if __name__ == '__main__':
    unittest.main()  # esto ejecuta nuestras pruebas