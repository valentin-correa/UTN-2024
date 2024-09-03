Algoritmo Jornal
	Definir tarifa_total, turno_diurno, turno_nocturno Como Real
	Definir dia Como Caracter
	
	Escribir "Ingresar día de trabajo"
	Leer dia
	Escribir "Cuántas horas trabajó el empleado entre las 6:00am y 20:00pm?"
	Leer turno_diurno
	Escribir "Cuántas horas trabajó el empleado entre las 20:00pm y las 6:00am?"
	Leer turno_nocturno
	
	si dia<>"domingo" o dia<>"Domingo"
		turno_diurno=turno_diurno*5
		turno_nocturno=turno_nocturno*8
	SiNo
		turno_diurno=turno_diurno*7
		turno_nocturno=turno_nocturno*11
	FinSi
	tarifa_total=turno_diurno+turno_nocturno
	Escribir "El jornal diario del empleado es de " tarifa_total " euros"
FinAlgoritmo
