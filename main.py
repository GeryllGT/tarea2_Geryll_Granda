from Clase5.clase5 import (
    lista_cuadrados,
    enumerar_elementos,
    funcion_doble,
    cambiar,
    mostrar_global,
    generador_simple,
    compuesto1,
    suma
)

def main():
    print("1. Comprehensions:", lista_cuadrados())
    print("2. Enumerate:", enumerar_elementos(["a", "b", "c"]))
    print("3. Lambda:", funcion_doble([1, 2, 3]))
    print("4. Ámbito Local:", cambiar())
    print("4. Ámbito Global:", mostrar_global())
    print("5. Generador:", list(generador_simple()))
    print("6. Composición:", compuesto1(3))  # (3+1)*2 = 8
    print("7. Función tipada (suma):", suma(4, 5))

if __name__ == "__main__":
    main()