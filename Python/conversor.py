def conversor (tipo_pesos, valor_dolar):
    pesos = input ("¿Cuantos pesos "+ tipo_pesos +" tienes?:  ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenidos al conversor de monedas 💰-😉

1 - Pesos chilenos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input (menu)
if opcion == "1":
    conversor("chilenos", 788)
elif opcion == "2":
    conversor("argentinos", 78)
elif opcion == "3":
    conversor("mexicanos", 22)
else: 
    print("Ingresa una opción correcta por favor")