import math
a = int(input("Informe o A da equação:"))
b = int(input("Informe o B da equação:"))
c = int(input("Informe o C da equação:"))

print("Calculando o delta da Equação:")
delta = (b**2)-(4*a*c)
print("Delta igual à: {} " .format(delta))

if delta > 0:
    delta1 = math.sqrt(delta)
    print("Raiz quadrada de delta: ", delta1)
    x1 = (-b + delta1) / (2 * a)
    x2 = (-b - delta1) / (2 * a)
    print("X1 = ", x1, "X2 = ", x2)
elif delta == 0:
    delta2 = math.sqrt(delta)
    print("Raiz quadrada de delta: ", delta2)
    x = -b / (2 * a)
    print("Valor de x = ", x)

elif delta < 0:
    print("Essa raiz é menor do que zero")
