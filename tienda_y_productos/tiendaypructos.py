import product_lib as pl
import  store_lib as sl


if __name__ == '__main__':
    # creacion de instancias
    producto1 = pl.product("manzana", 100, "frutas")
    producto2 = pl.product("pera", 200, "frutas")
    producto3 = pl.product("centella", 250, "helados")
    producto4 = pl.product("trululu", 350, "helado")
    tienda1 = sl.store("El semanforo")

    # prueba de metodos
    #se agregan 4 productos
    print("Se agregan 4 producto de dos categorias")
    tienda1.add_product(producto1)
    tienda1.add_product(producto2)
    tienda1.add_product(producto3)
    tienda1.add_product(producto4)
    # mostrar todos los prductos
    for producto in tienda1.list_products.values():
        producto.print_info()

    # se elimina el trululu
    print("\nSe elimina trululu y se vuelve a agregar")
    tienda1.remove_product(3)
    # mostrar todos los prductos
    for producto in tienda1.list_products.values():
        producto.print_info()
    print("Se agrega")
    tienda1.add_product(producto4)
    # mostrar todos los prductos
    for producto in tienda1.list_products.values():
        producto.print_info()

    # se agregar inflacion al precio de los productos
    print("\nse agregar inflacion al precio de los productos")
    tienda1.inflation(0.1)

    # se reduce el precio de categoria frutas
    print("\nse reduce el precio de categoria")
    tienda1.set_clearance("frutas", 0.2)

    # se reduce el precio del centella
    print("\nse reduce el precio del centella")
    tienda1.set_clearance(3, 0.2)