'''
Dado una expresionn regular ingresada por el usuario, devolver 3 cadenas que cumplan la condicion teniendo en cuenta que todos los términos deben estar entre paréntesis

Tener en cuenta los operadores (), U, * y sólo considerar expresiones regulares con como máximo 1 (una) unión y del alfabeto {a,b}

Ejemplos:

(a*)(b*) --> [aaaabbbbbb, bbbbbb, aaaaaa]
(a)(ba*)U(b) --> [ab, ababab, abababab]
(a*)U(b*) --> [a, b, bbb]
'''

import random

def generate_strings_from_regex(regex):
    # Función principal que genera tres cadenas a partir de la expresión regular
    if 'U' in regex:
        return generate_union(regex)
    return generate_from_concatenation(regex)

def generate_union(regex):
    # Manejo de la unión de dos partes, separadas por 'U'
    left, right = regex.split('U')
    left_strings = generate_from_concatenation(left)
    right_strings = generate_from_concatenation(right)
    return random.sample(left_strings + right_strings, 3)

def generate_from_concatenation(regex):
    # Genera cadenas basadas en concatenaciones y estrellas '*'
    parts = split_regex_parts(regex)
    strings = ['']
    for part in parts:
        new_strings = []
        if part.endswith('*'):
            base = part[:-1]
            # Genera varias versiones del string basado en la estrella '*'
            options = [''] + [base*random.randint(0,10) for i in range(1, 3)]
            for s in strings:
                for opt in options:
                    new_strings.append(s + opt)
        else:
            for s in strings:
                new_strings.append(s + part)
        strings = new_strings
    return strings

def split_regex_parts(regex):
    # Divide la expresión regular en partes para manejar las concatenaciones
    parts = []
    i = 0
    while i < len(regex):
        if regex[i] == '(':
            j = i
            while regex[j] != ')':
                j += 1
            parts.append(regex[i+1:j])
            i = j
        elif regex[i].isalpha():
            if i + 1 < len(regex) and regex[i+1] == '*':
                parts.append(regex[i:i+2])
                i += 1
            else:
                parts.append(regex[i])
        i += 1
    return parts

# Ejemplos de uso
regex1 = '(a*)(b*)'
regex2 = '(a)(ba*)U(b)'
regex3 = '(a*)U(b*)'

print("Ejemplo 1:", generate_strings_from_regex(regex1))
print("Ejemplo 2:", generate_strings_from_regex(regex2))
print("Ejemplo 3:", generate_strings_from_regex(regex3))