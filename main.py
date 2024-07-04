import funciones

lista_datos = []

while True:
    print("--- CleanWasser ---")
    opcion = funciones.menu()
    if opcion == 1:
        print("--- Registrar Pedido ---")
        funciones.registrar_pedido(lista_datos)
    elif opcion == 2:
        print(lista_datos)

    elif opcion == 3:
        funciones.imprimir_hoja(lista_datos)
    elif opcion == 4:
        pass
    elif opcion == 5: 
        break

