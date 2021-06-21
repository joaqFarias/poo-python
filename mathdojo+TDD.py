import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
        self.ds = 0

    def add(self, num, *args):
        # tu código aquí
        self.result += num
        if len(args) > 0:
            for i in range(len(args)):
                self.result += args[i]
        return self

    def subtract(self, num, *args):
        # tu código aquí
        self.result -= num
        if len(args) > 0:
            for i in range(len(args)):
                self.result -= args[i]
        return self

    def desviacion_standar(self, *args):
        if len(args) <= 0:
            return 0
        else:
            ds = 0
            media = sum(args) / len(args)
            for i in range(len(args)):
                ds = abs(args[i] - media)
            self.ds = ds / len(args)
            return  self

class mathDojoTests(unittest.TestCase):

    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp
    def setUp(self):
        # agrega las tareas setUp
        print("\nSe crea objeto")
        self.md = MathDojo()

    def testOne(self):
        self.assertEqual(self.md.add(1, 2, 3).add(5).result, 11, msg="error en suma")

    def testTwo(self):
        self.assertEqual(self.md.subtract(10).subtract(1).result, -11, msg="error en sustraccion")

    def testThree(self):
        self.assertEqual(self.md.add(10, 10).subtract(5).result, 15, msg="error en suma y sustraccion en conjunto")
    
    def testFour(self):
        self.assertEqual(self.md.desviacion_standar(1, 3, 4, 5, 6).ds, 0.44000000000000006, msg = "error en desviacion estandar")

    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown
        print("Finaliza la prueba")


if __name__ == '__main__':
    unittest.main()  # esto ejecuta nuestras pruebas
