class SList:
    def __init__(self):
        self.head = None
        self.next = None

    def add_to_front(self, val):
        new_node = SLNode(val)	     # crea una instancia de la clase Node usando el valor dado
        current_head = self.head	 # salva la cabecera actual en una variable
        new_node.next = current_head # Coloca el proximo nodo en la lista de la cabecera actual
        self.head = new_node     	 # Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        return self	                 # return self para permitir las cadenas
    
    def add_to_back(self, val):
        if self.head == None:	     # si la lista está vaciacopy
            self.add_to_front(val)	 # ejecuta el método add_to_fron
            return self	             # asegurémonos de que el resto de esta función no suceda si agregamos al frente
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	     # Incrementa el corredor al siguiente nodo de la lista.
        return self                  # retorna self para permitir el encadenamiento

    def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
                runner = runner.next 	# Establecer el corredor a su vecino
            return self                 # Una vez que el bucle está terminado, regrese a sí mismo para permitir el encadenamiento

    # ejercicios
    # eliminar el primer nodo y devolver su valor
    def remove_from_front(self): 
        print(f"El valor eliminado fue: {self.head.value}")
        self.next = self.head.next.next
        self.head = self.head.next
        return self
    # eliminar el último nodo y devolver su valor
    def remove_from_back(self):
        runner = self.head
        while runner.next != None:
            before_runner = runner
            runner = runner.next
        print(f"El valor eliminado fue: {runner.value}")
        before_runner.next = None
        return self
    # eliminar el primer nodo con el valor dado
    def remove_val(self, val):
        print(f"El valor eliminado fue: {val}")
        runner = self.head
        if runner.value == val:
            self.remove_from_front()
            return self
        before_runner = runner
        while runner.next != None:
            after_runner = runner.next
            if runner.value == val:
                before_runner.next = after_runner 
                return self
            before_runner = runner
            runner = runner.next
        self.remove_from_back()
        return self
    # insertar un nodo con valor val como el n º nodo en la lista
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        runner = self.head
        for n_node in range(1, n+1):
            if runner.next == None:
                self.add_to_back(val)
                return self
            if n_node == n:
                new_node = SLNode(val)
                new_node.next = runner.next
                runner.next = new_node
                return self
            runner = runner.next
        

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()	# crear una nueva instancia de una lista
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values() # encadenamiento, yeah!
# la saalida deberia ser:
# Linked list
# are
# fun!
print("\n")
my_list.remove_from_front().print_values().add_to_front("Linked list")
print("\n")
my_list.remove_from_back().print_values().add_to_back("fun!")
print("\n")
my_list.remove_val("are").print_values()
print('\n')
my_list.insert_at("insert", 1).print_values() # sirve con 0, 1, 2, etc.