import unittest

def factorial(numero: int) -> int: 
    if numero < 0: 
        return "NA"
    elif numero <= 1:
        return 1
    else:
        return numero * factorial(numero - 1)

class factorialTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(factorial(5), 120, msg="se calcula mal el factorial")

    def testTwo(self):
        self.assertEqual(factorial(0), 1, msg="No admite 0")

    def testThree(self):
        self.assertEqual(factorial(1), 1, msg="no admite 1")

    def testFour(self):
        self.assertEqual(factorial(-1), "NA", msg="no admite negativos")

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