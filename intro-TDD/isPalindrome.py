import unittest

def isPalindrome(palabra: str) -> bool:
    palabra_reverse = palabra[::-1]
    if palabra.lower() == palabra_reverse.lower():
        return True
    else:
        return False

class isPalindromeTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(isPalindrome("ana"), True, msg="La palabra no es palindrome")

    def testTwo(self):
        self.assertEqual(isPalindrome("juana"), False, msg="La palabra no es palindrome")

    def testThree(self):
        self.assertTrue(isPalindrome("Rodador"), msg="La palabra no es palindrome")

    def testFour(self):
        self.assertFalse(isPalindrome("CaRaCol1"), msg="La palabra no es palindrome")

    def testFive(self):
        self.assertEqual(isPalindrome("Sometemos"), True, msg="La palabra no es palindrome")

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