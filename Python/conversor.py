pesos_chilenos = input ("¿Cuantos pesos chilenos tienes?:  ")
pesos_chilenos = float (pesos_chilenos)
valor_dolar = 788
dolares = pesos_chilenos / valor_dolar
dolares = round (dolares, 2)
dolares = str (dolares)
print("Tienes $" + dolares + " dólares")
