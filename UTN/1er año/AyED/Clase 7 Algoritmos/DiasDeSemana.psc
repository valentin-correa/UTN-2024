Algoritmo DiasDeSemana
	Definir dia Como Caracter
	
	Escribir "Ingrese un día de la semana"
	Leer dia
	
	Segun dia Hacer
		"Lunes" o "lunes":
			Escribir "Martes, Miercoles, Jueves, Viernes, Sábado, Domingo"
		"Martes" o "martes":
			Escribir "Miercoles, Jueves, Viernes, Sábado, Domingo, Lunes"
		"Miercoles" o "miercoles":
			Escribir "Jueves, Viernes, Sábado, Domingo, Lunes, Martes"
		"Jueves" o "jueves":
			Escribir "Viernes, Sábado, Domingo, Lunes, Martes, Miercoles"
		"Viernes" o "viernes":
			Escribir "Sábado, Domingo, Lunes, Martes, Miercoles, Jueves"
		"Sábado" o "sábado":
			Escribir "Domingo, Lunes, Martes, Miercoles, Jueves, Viernes"
		"Domingo" o "domingo":
			Escribir "Lunes, Martes, Miercoles, Jueves, Viernes, Sábado"
	Fin Segun
FinAlgoritmo
