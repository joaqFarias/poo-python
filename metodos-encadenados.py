class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount: int) -> None:	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self

    # haz que este método disminuya el saldo del usuario en la cantidad especificada
    def make_withdrawal (self, amount: int) -> None:
        self.account_balance -= amount
        return self

    # haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
    def display_user_balance (self) -> None:
        print(f"Usuario: {self.name}, Saldo: {self.account_balance}")

    # BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la
    #               cantidad y agrega esa cantidad al saldo de otro other_user
    def transfer_money (self, other_user: str, amount: int) -> None:
        self.account_balance -= amount
        usuario3.account_balance += amount
        return self
            
            


# se crean 3 instancias de la clase
usuario1 = User("Joaquin Farias", "joaquin.farias@gmail.com")
usuario2 = User("Rebeca Munoz", "rebeca.munoz@gmail.com")
usuario3 = User("Belen Varas", "belen.varas@gmail.com")

# metodos encadenados
print("Deposito encadenado")
usuario1.make_deposit(1000).make_deposit(1000).make_deposit(1000)
usuario1.display_user_balance()