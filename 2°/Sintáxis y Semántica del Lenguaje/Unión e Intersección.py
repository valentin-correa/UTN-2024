def customSplit(cadena, caracterSeparador):
    nuevaCadena = []
    elemento = ""
    for caracter in cadena:
        if caracter != caracterSeparador:
            elemento += caracter
        else:
            nuevaCadena.append(elemento)
            elemento = ""
    nuevaCadena.append(elemento)
    return nuevaCadena

    # Consideración: Se podría agregar como strip() para no generar confusiones en el input de elementos del conjunto.


def union(conjuntoA, conjuntoB):
    # Analizamos si al menos los conjuntos empiezan y terminan con llaves. Característica fundamental de conjuntos.
    if (conjuntoA[0] == conjuntoB[0] == "{") and (conjuntoA[-1] == conjuntoB[-1] == "}"):
        # Convertimos las cadenas en listas para poder trabajar con cada elemento por separado. Además, identificamos los elementos separados por comas con split(",").
        conjuntoA = customSplit(conjuntoA[1:-1], ",")
        conjuntoB = customSplit(conjuntoB[1:-1], ",")
        for elemento in conjuntoA:
            if elemento not in conjuntoB:
                # Anexamos cada elemento que no esté en el conjunto B del conjunto A. Esto con el fin de evitar repetidos (inexistente en Teoría de Conjuntos).
                conjuntoB.append(elemento)
        return conjuntoB
    else:
        return ("Los conjuntos no han sido ingresados con el formato correspondiente.")


def interseccion(conjuntoA, conjuntoB):
    conjuntoFinal = []
    # Analizamos si al menos los conjuntos empiezan y terminan con llaves. Característica fundamental de conjuntos.
    if (conjuntoA[0] == conjuntoB[0] == "{") and (conjuntoA[-1] == conjuntoB[-1] == "}"):
        # Convertimos las cadenas en listas para poder trabajar con cada elemento por separado. Además, identificamos los elementos separados por comas con split(",").
        conjuntoA = customSplit(conjuntoA[1:-1], ",")
        conjuntoB = customSplit(conjuntoB[1:-1], ",")
        for elemento in conjuntoA:
            if elemento in conjuntoB:
                # Anexamos cada elemento del conjunto A que esté en el conjunto B a un nuevo conjunto. Esto debido a que no tiene sentido anexar o quitar elementos de un conjunto.
                conjuntoFinal.append(elemento)
        if conjuntoFinal:
            # Con este condicional, analizamos si la lista "conjuntoFinal" tiene elementos o está vacía.
            return conjuntoFinal
        else:
            return "No hay elementos en común entre los conjuntos."
    else:
        return ("Los conjuntos no han sido ingresados con el formato correspondiente.")
