## Programa que verifique si un número es par o impar

numero = int(input("Digite un número para verificar si es par o impar:\n "))
if numero % 2 == 0:
  print(f"El número {numero} es par")
else:
  print(f"El número {numero} es impar")