# 3. Registrar cantidades del inventario
from busqueda import buscar_producto

def registrar_inventario(codigos, nombres, colores, tallas):
    inventario_codigos = []
    inventario_cantidades = []
    continuar = "S"

    while continuar == "S":
        codigo = input("\nEscanea el codigo del producto: ")
        codigo = codigo.strip().upper()

        posicion = buscar_producto(codigo, codigos)

        if posicion != -1:
            print("\nProducto encontrado")
            print("Nombre:", nombres[posicion])
            print("Color:", colores[posicion])
            print("Talla:", tallas[posicion])

            while True:
                try:
                    cantidad = int(input("Cuantas unidades tienes?: "))

                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    else:
                        break

                except ValueError:
                    print("Ingresa una cantidad numerica.")

            posicion_inventario = buscar_producto(
                codigo, inventario_codigos
            )

            if posicion_inventario != -1:
                inventario_cantidades[posicion_inventario] += cantidad
            else:
                inventario_codigos.append(codigo)
                inventario_cantidades.append(cantidad)

            posicion_inventario = buscar_producto(
                codigo, inventario_codigos
            )

            print(
                "Cantidad acumulada:",
                inventario_cantidades[posicion_inventario]
            )

        else:
            print("\nCodigo no registrado en el catalogo.")

        continuar = input(
            "\nDeseas escanear otro codigo? (S/N): "
        ).strip().upper()

        while continuar != "S" and continuar != "N":
            continuar = input(
                "Escribe S para continuar o N para terminar: "
            ).strip().upper()

    return inventario_codigos, inventario_cantidades