print(__name__)

if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")
else:
    print("El archivo esta siendo ejecutado porque este esta siendo importado por otro archivo.\nEl archivo se llama: ", __name__)