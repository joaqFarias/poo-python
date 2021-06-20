class product:
    def __init__(self, name: str, price: int, category:str) -> None:
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change: float, is_increased: bool) -> object:
        if is_increased == True:
            self.price = self.price + (percent_change * self.price)
        else:
            self.price = self.price - (percent_change * self.price)
        print(f"el nuevo precio del producto {self.name} es {self.price}")
        return self

    def print_info(self) -> object:
        print(f"Nombre producto: {self.name} | Categoria: {self.category} | Precio: {self.price}")
        return self