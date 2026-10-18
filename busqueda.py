# 2. Buscar un producto por su codigo
def buscar_producto(codigo, codigos):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i

    return -1