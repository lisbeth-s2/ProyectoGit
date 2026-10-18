from busqueda import buscar_producto

# 4. Ordenar el inventario por codigo
def ordenar_inventario(inventario_codigos, inventario_cantidades):
    for i in range(len(inventario_codigos) - 1):
        for j in range(len(inventario_codigos) - 1 - i):
            if inventario_codigos[j] > inventario_codigos[j + 1]:
                auxiliar = inventario_codigos[j]
                inventario_codigos[j] = inventario_codigos[j + 1]
                inventario_codigos[j + 1] = auxiliar

                auxiliar = inventario_cantidades[j]
                inventario_cantidades[j] = inventario_cantidades[j + 1]
                inventario_cantidades[j + 1] = auxiliar


# 5. Mostrar el resumen final
def mostrar_inventario(inventario_codigos, inventario_cantidades, codigos, nombres, colores, tallas):
    if len(inventario_codigos) == 0:
        print("\nNo se registraron productos.")
        return

    ordenar_inventario(inventario_codigos, inventario_cantidades)

    print("\n")
    print("=" * 75)
    print("                    INVENTARIO PEAK")
    print("=" * 75)
    print(f"{'CODIGO':<12}{'PRODUCTO':<25}{'COLOR':<15}{'TALLA':<8}{'CANTIDAD':>10}")
    print("-" * 75)

    total_unidades = 0

    for i in range(len(inventario_codigos)):
        codigo = inventario_codigos[i]
        posicion = buscar_producto(codigo, codigos)

        print(f"{codigo:<12}{nombres[posicion]:<25}{colores[posicion]:<15}{tallas[posicion]:<8}{inventario_cantidades[i]:>10}")
        total_unidades += inventario_cantidades[i]

    print("-" * 75)
    print("Productos diferentes:", len(inventario_codigos))
    print("Total de unidades:", total_unidades)
    print("=" * 75)