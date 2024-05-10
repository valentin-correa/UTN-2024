def custom_replace(input_string, target, replacement):
    output_string = ""
    i = 0
    while i < len(input_string):
        # Verificar si la subcadena objetivo comienza en la posición actual
        if input_string[i:i + len(target)] == target:
            # Si sí, reemplazar la subcadena objetivo con la subcadena de reemplazo
            output_string += replacement
            i += len(target)  # Saltar la longitud de la subcadena objetivo en la entrada
        else:
            # Si no, copiar el carácter actual de la entrada a la salida y avanzar
            output_string += input_string[i]
            i += 1
    return output_string

def espacios(cadena):
    cadena_good = ""
    for i in range(len(cadena)):
        if cadena[i] != " " or (cadena[i] == " " and cadena[i-1] != " "):
            cadena_good += cadena[i]
    return cadena_good

def quita_numeros(cadena):
    cad=""
    for i in range(len(cadena)):
        if cadena[i] not in {"0","1","2","3","4","5","6","7","8","9"}:
            cad+=cadena[i]
    return cad

def equipo_pos1(cadena):
    cad=""
    for i in range(len(cadena)):
        if cadena[i]==" " and cadena[i-1]==" ":
            return espacios(cad)
        cad+=cadena[i]
    
def equipo_pos2(cadena):
    return custom_replace(cadena, equipo_pos1(cadena)+" ", "")
    
print(quita_numeros("ameghino 50 union central 26"))
print(equipo_pos1(quita_numeros("ameghino 50 union central 26")))
print(equipo_pos2(quita_numeros("ameghino 50 union central 26")))
