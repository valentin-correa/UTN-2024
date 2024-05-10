Algoritmo ejercicio_4_3
	Leer hora_de_ingreso
	Leer hora_de_egreso
	Leer dia
	Leer turno
	
	hora=hora_de_egreso - hora_de_ingreso

	Si turno="diurno"
			tarifa=hora*5
		finsi
	Si turno="nocturno"
			tarifa=hora*8
		finsi
	Si dia=domingo y turno="diurno"
		tarifa=hora*7
	FinSi
	
	Si dia=domingo y turno="nocturno"
				tarifa=hora*11
				
			FinSi
	
escribir tarifa

FinAlgoritmo
