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

# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
y = MathDojo()
y = md.add(20).add(1, 2, 3, -3).subtract(-3, -3, 1).result
print(y)

ds = MathDojo()
z = ds.desviacion_standar(1, 3, 4, 5, 6).ds
print(f"Desviacion estandar: {z}")
