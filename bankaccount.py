class BankAccount:
    # ¡No olvides agregar valores predeterminados para estos parámetros!
    def __init__(self, int_rate: float=1, balance: int=0):
        '''
        El interes se ingresa como porcentaje y el balance es el saldo inicial de la cuenta
        '''
        # su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
        # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
        self.int_rate = int_rate
        self.amount = balance

    def deposit(self, amount: int) -> None:
        # tu código aqui
        self.amount += amount
        return self

    def withdraw(self, amount: int) -> None:
        # tu código aqui
        self.amount -= amount
        return self

    def display_account_info(self) -> None:
        # tu código aqui
        print(f"Saldo: $ {self.amount}")
        return self

    def yield_interest(self) -> None:
        # tu código aqui
        interest = self.amount * (self.int_rate / 100)
        if self.amount > 0:
            self.amount = self.amount + interest
        return self

# Crear dos cuentas
cuenta1 = BankAccount(2, 1000)
cuenta2 = BankAccount(2.5, 2500)

# En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y 
# muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

# En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre 
# la información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta2.deposit(100).deposit(200).withdraw(50).withdraw(50).withdraw(100).withdraw(50).display_account_info()