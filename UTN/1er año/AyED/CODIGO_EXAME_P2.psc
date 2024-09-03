Algoritmo sin_titulo
	silo1=10000
	silo2=8000
	silo3=5000
	silo1capres=silo1
	silo2capres=silo2
	silo3capres=silo3
	
	camionMax=patente
	cargaMax=carga
	
	Mientras ultimocamion<>1
		Escribir "¿Es el ultimo camion? true/false"
		leer finalizar
		si finalizar="true"
			ultimocamion=1
		FinSi
		
		Escribir "¿Cual es tu patente?"
		Leer patente
		
		Escribir "¿Cual es tu carga?"
		Leer carga
		
		Si carga>cargaMax
			camionMax=patente
		FinSi
		
		Si carga<silo1capres
			silo1capres=silo1capres-carga
		sino carga=carga-silo1capres
			silo1capres=0
		FinSi
		
		Si carga<silo2capres
			silo2capres=silo2capres-carga
		sino carga=carga-silo2capres
			silo2capres=0
		FinSi
		
		Si carga<silo3capres
			silo3capres=silo3capres-carga
		sino carga=carga-silo3capres
			silo3capres=0
		FinSi
		
		Escribir "El silo 1 tiene ", silo1capres," de capacidad restante"
		Escribir "El silo 2 tiene ", silo2capres," de capacidad restante"
		Escribir "El silo 3 tiene ", silo3capres," de capacidad restante"
	FinMientras
	
	silo1=silo1-silo1capres
	silo2=silo2-silo2capres
	silo3=silo3-silo3capres
	
	Escribir "El camion que más descargo fue ", camionMax
	Escribir "El silo 1 quedo con ", silo1, "Kg"
	Escribir "El silo 2 quedo con ", silo2, "Kg"
	Escribir "El silo 3 quedo con ", silo3, "Kg"
FinAlgoritmo
