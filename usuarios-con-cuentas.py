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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# agregó esta línea

    def example_method(self):
        self.account.deposit(100)		# podemos llamar los métodos de la instancia BankAccount 
        print(self.account.balance)		# o acceder a sus atributos




