from catalogo import crear_catalogo
from registro import registrar_inventario
from resumen import mostrar_inventario
# 6. Menu principal
def menu_principal():
    codigos, nombres, colores, tallas = crear_catalogo()

    while True:
        print("\n================================")
        print("          SISTEMA PEAK")
        print("================================")
        print("1. Ventas (pendiente)")
        print("2. Consultar precio (pendiente)")
        print("3. Inventario")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            print("Modulo de ventas pendiente.")

        elif opcion == "2":
            print("Modulo de consulta de precios pendiente.")

        elif opcion == "3":
            inventario_codigos, inventario_cantidades = (
                registrar_inventario(
                    codigos, nombres, colores, tallas
                )
            )

            mostrar_inventario(
                inventario_codigos,
                inventario_cantidades,
                codigos,
                nombres,
                colores,
                tallas
            )

        elif opcion == "4":
            print("Gracias por utilizar el sistema PEAK.")
            break

        else:
            print("Opcion incorrecta. Intenta nuevamente.")


# Inicio del programa
menu_principal()
