Algoritmo Problema_clase_Alg_Pseint
	Definir cad Como Caracter
	Definir ac Como Entero
	ac = 0
	Escribir "Ingrese una cadena: "
	Leer cad
	cad = Minusculas(cad)
	Para i = 1 hasta Longitud(cad)
		si (Subcadena(cad, i, i) = "a" o Subcadena(cad, i, i) = "e" o Subcadena(cad, i, i) = "i" o Subcadena(cad, i, i) = "o" o Subcadena(cad, i, i) = "u") y ((Subcadena(cad, i-1, i-1) = " " o i = 0))
			ac = ac + 1
		FinSi
	FinPara
	Escribir "La cantidad de palabras que comienzan con una vocal es: ", ac
FinAlgoritmo
