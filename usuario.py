class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount: int) -> None:	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

    # haz que este método disminuya el saldo del usuario en la cantidad especificada
    def make_withdrawal (self, amount: int) -> None:
        self.account_balance -= amount

    # haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
    def display_user_balance (self) -> None:
        print(f"Usuario: {self.name}, Saldo: {self.account_balance}")

    # BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la
    #               cantidad y agrega esa cantidad al saldo de otro other_user
    def transfer_money (self, other_user: str, amount: int) -> None:
        self.account_balance -= amount
        other_user.account_balance += amount
            
            


# se crean 3 instancias de la clase
usuario1 = User("Joaquin Farias", "joaquin.farias@gmail.com")
usuario2 = User("Rebeca Munoz", "rebeca.munoz@gmail.com")
usuario3 = User("Belen Varas", "belen.varas@gmail.com")

# Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
print("Ejercicio 1")
usuario1.make_deposit(1000)
usuario1.make_deposit(1000)
usuario1.make_deposit(1000)
usuario1.make_withdrawal(1000)
usuario1.display_user_balance()

# Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
print("\nEjercicio 2")
usuario2.make_deposit(1000)
usuario2.make_deposit(1000)
usuario2.make_withdrawal(500)
usuario2.make_withdrawal(500)
usuario2.display_user_balance()

# Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
print("\nEjercicio 3")
usuario3.make_deposit(9000)
usuario3.make_withdrawal(1000)
usuario3.make_withdrawal(1000)
usuario3.make_withdrawal(1000)
usuario3.display_user_balance()

# BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera 
# dinero al tercer usuario y luego imprima los saldos de ambos usuarios
print("\nBonus")
usuario1.transfer_money(usuario3, 500)
usuario1.display_user_balance()
usuario3.display_user_balance()