Algoritmo DiasDeSemana
	Definir dia Como Caracter
	
	Escribir "Ingrese un d�a de la semana"
	Leer dia
	
	Segun dia Hacer
		"Lunes" o "lunes":
			Escribir "Martes, Miercoles, Jueves, Viernes, S�bado, Domingo"
		"Martes" o "martes":
			Escribir "Miercoles, Jueves, Viernes, S�bado, Domingo, Lunes"
		"Miercoles" o "miercoles":
			Escribir "Jueves, Viernes, S�bado, Domingo, Lunes, Martes"
		"Jueves" o "jueves":
			Escribir "Viernes, S�bado, Domingo, Lunes, Martes, Miercoles"
		"Viernes" o "viernes":
			Escribir "S�bado, Domingo, Lunes, Martes, Miercoles, Jueves"
		"S�bado" o "s�bado":
			Escribir "Domingo, Lunes, Martes, Miercoles, Jueves, Viernes"
		"Domingo" o "domingo":
			Escribir "Lunes, Martes, Miercoles, Jueves, Viernes, S�bado"
	Fin Segun
FinAlgoritmo
