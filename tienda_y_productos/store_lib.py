from typing import Union

class store:
    def __init__(self, name: str, list_products: dict = {}) -> None:
        self.name = name
        self.list_products = list_products

    def add_product (self, new_product: object) -> object:
        for num_id in range(len(self.list_products.keys())+1):
            if not str(num_id) in self.list_products.keys():
                self.list_products[str(num_id)] = new_product
                break
        return self

    def remove_product (self, id_product: int) -> object:
        if str(id_product) in self.list_products.keys():
            del self.list_products[str(id_product)]
        else:
            print("ingrese ID valida")
        return self

    def inflation(self, percent_increase: float) -> object:
        for id_product in self.list_products.keys():
            self.list_products[id_product].update_price(percent_increase, True)
        return self

    def set_clearance (self, category_or_idproduct: Union[str, int], percent_discount: float) -> object:
        if type(category_or_idproduct) == str:
            for id_product in self.list_products.keys():
                if self.list_products[id_product].category == category_or_idproduct:
                    self.list_products[id_product].update_price(percent_discount, False)
        elif type(category_or_idproduct) == int:
            self.list_products[str(category_or_idproduct)].update_price(percent_discount, False)
        return self