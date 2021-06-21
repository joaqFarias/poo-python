import unittest
import numpy as np

def monedas(monedas: int) -> list: # devuelve un array con la cantidad de monedas de [25, 10, 5, 1]
    lista_monedas = [] 
    # monedas de 25
    monedas25 = np.floor(monedas / 25)
    if monedas25 > 0:
        lista_monedas.append(int(monedas25))
        monedas -= monedas25 * 25
    else:
        lista_monedas.append(0)
    # monedas de 10
    monedas10 = np.floor(monedas / 10)
    if monedas10 > 0:
        lista_monedas.append(int(monedas10))
        monedas -= monedas10 * 10
    else:
        lista_monedas.append(0)
    # monedas de 5
    monedas5 = np.floor(monedas / 5)
    if monedas5 > 0:
        lista_monedas.append(int(monedas5))
        monedas -= monedas5 * 5
    else:
        lista_monedas.append(0)
    # monedas de 1
    monedas1 = np.floor(monedas / 1)
    if monedas1 > 0:
        lista_monedas.append(int(monedas1))
    else:
        lista_monedas.append(0)
    return lista_monedas

class monedasTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(monedas(87), [3, 1, 0, 2], msg="No se minimiza el numero de monedas")

    def testTwo(self):
        self.assertEqual(monedas(15), [0, 1, 1, 0], msg="No se minimiza el numero de monedas")

    def testThree(self):
        self.assertEqual(monedas(41), [1, 1, 1, 1], msg="No se minimiza el numero de monedas")

    def testFour(self):
        self.assertEqual(monedas(6), [0, 0, 1, 1], msg="No se minimiza el numero de monedas")

    def testFive(self):
        self.assertEqual(monedas(1531), [61, 0, 1, 1], msg="No se minimiza el numero de monedas")

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