Algoritmo Sueldo
	Escribir "Cuántas horas trabajó el empleado?"
	Leer horas_trabajadas
	Escribir "Cuánto es el importe por hora?"
	Leer importe
	
	si horas_trabajadas<40
		horas_trabajadas=horas_trabajadas*importe
	SiNo
		horas_trabajadas=horas_trabajadas*importe*1.5
	FinSi
	salario=horas_trabajadas
	
	Escribir "El sueldo del empleado es de " "$" salario
	
FinAlgoritmo

	