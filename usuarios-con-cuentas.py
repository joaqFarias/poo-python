class BankAccount:
    # ¡No olvides agregar valores predeterminados para estos parámetros!
    def __init__(self, name_account: str, int_rate: float=1, balance: int=0):
        '''
        El interes se ingresa como porcentaje y el balance es el saldo inicial de la cuenta
        '''
        # su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
        # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
        self.name_account = name_account
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

class User:		# aqui está lo que tenemos hasta ahora
    
    def __init__(self, name: str, email: str, accounts: dict={}) -> None:
        self.name = name
        self.email = email
        self.accounts = accounts
        account1 = BankAccount("account1", int_rate=0.02, balance=0)	# agregó esta línea
        self.accounts["account1"] = account1

    def add_account(self, name_account: str, int_rate: float=1, balance: int=0) -> None:
        account_create = BankAccount(name_account=name_account, int_rate=int_rate, balance=balance)
        self.accounts[name_account] = account_create
        return self

    # agrega el método deposit 
    def make_deposit(self, amount: int, name_account: str="account1") -> None:	# toma un argumento que es el monto del depósito
        self.accounts[name_account].deposit(amount)	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self

    # haz que este método disminuya el saldo del usuario en la cantidad especificada
    def make_withdrawal (self, amount: int, name_account: str="account1") -> None:
        self.accounts[name_account].withdraw(amount)
        return self

    # haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
    def display_user_balance (self, name_account: str="account1") -> None:
        print(f"Usuario: {self.name}")
        print(f"Cuenta: {name_account}")
        self.accounts[name_account].display_account_info()

    # BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la
    #               cantidad y agrega esa cantidad al saldo de otro other_user
    def transfer_money (self, other_user: str, amount: int, name_account: str="cuenta1", account_transfer: str="cuenta1") -> None:
        self.accounts[name_account].withdraw(amount)
        other_user.accounts[account_transfer].deposit(amount)
        return self

# prueba de deposito
usuario1 = User("Joaquin Farias", "jfarias@gmail.com")
usuario1.make_deposit(1000, "account1").display_user_balance("account1")
print("")
# prueba nueva cuenta y giro
usuario1.add_account("cuenta 2").make_deposit(3000, "cuenta 2").make_withdrawal(1000, "cuenta 2").display_user_balance("cuenta 2")



