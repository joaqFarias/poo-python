import unittest

def reverseList(lista: list) -> list:
    return lista[::-1]

class reverseListTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def testTwo(self):
        self.assertEqual(reverseList([-1, 0, 1, 4]), [4, 1, 0, -1])

    def testThree(self):
        self.assertEqual(reverseList(["hola", "chao", "como"]), ["como", "chao", "hola"])

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
