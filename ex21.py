def adicionar(a, b):
    print(f"Adicionar {a} + {b}")
    return a + b

def subtrair(a, b):
    print(f"Subtração: {a} - {b}")
    return a - b

def multiplicar(a, b):
    print(f"Multiplicar {a} * {b}")
    return a * b

def dividir (a, b):
    print(f"Divisão {a} / {b}")
    return a / b

print("Vamos fazer alguns cálculos usando funções!")

idade = adicionar(30, 3)
altura = subtrair(78, 4)
peso = multiplicar(40,2)
qi = dividir(200,2)

print(f"Idade: {idade}, Altura: {altura}, Peso: {peso}, Qi: {qi}")
