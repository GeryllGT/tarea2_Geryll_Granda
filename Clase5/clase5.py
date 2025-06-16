# 1. Comprehensions
# ----------------------------------
# Básico 1: lista de cuadrados
def lista_cuadrados(n=5):
    return[x**2 for x in range(n)]
# ----------------------------------

# ----------------------------------
# 2. enumerate
# ----------------------------------
# Básico 1: impresión con índices
def enumerar_elementos(lista):
    return list(enumerate(lista))

# ----------------------------------
# 3. Funciones lambda
# ----------------------------------
# Básico 1: función doble
def funcion_doble(lista):
    f=lambda x: x * 2
    return [f(i) for i in lista]

# 4. Ámbito local/global
# ----------------------------------
# Básico 1: local vs global
x = 5   #variable global
def cambiar():
    x = 10  # local
    return f"Local: {x}"

def mostrar_global():
    return f"Global: {x}"

# === Generadores (yield) ===
# 1. Básico: Secuencia de números

def generador_simple():
    for i in range(3):
        yield i

# === Composición de funciones ===
# 1. Básico

def doble(x):
    return 2 * x

def incrementar(x):
    return x + 1

def compuesto1(x):
    return doble(incrementar(x))

# === Funciones tipadas ===
# 1. Básico

def suma(a: int, b: int) -> int:
    return a + b