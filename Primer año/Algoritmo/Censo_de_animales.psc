Algoritmo Censo_de_animales
	
	Definir animal Como Caracter
	Definir contador,vacacon, vacaenfcon, cabracon, cabraenfcon, cerdoenfcon Como Entero

	Mientras contador<350
		Escribir "¿Que es?"
		Escribir "Escriba lo que ve especie y estado de salud"
		
		//Vista previa de contadores
		Escribir vacacon
		Escribir vacaenfcon
		Escribir cerdocon
		Escribir cerdoenfcon
		Escribir cabracon
		Escribir cabraenfcon
		
		//Variable animal
		leer animal
		
		//Comprobacion de especie y estado de salud
		si animal="vaca"
			vacacon=vacacon+1
		FinSi
		si animal="cerdo"
			cerdocon=credocon+1
		FinSi
		si animal="cabra"
			cabracon=cabracon+1
		FinSi
		si animal="vaca enferma"
			vacaenfcon=vacaenfcon+1
		FinSi
		si animal="cerdo enferma"
			cerdoenfcon=cerdoenfcon+1
		FinSi
		si animal="cabra enferma"
			cabraenfcon=cabraenfcon+1
		FinSi
		contador=contador+1
	FinMientras
	
	//Escritura de resultados
	Escribir "La cantidad de vacas es " vacacon
	Escribir "La cantidad de vacas enfermas es " vacaenfcon
	Escribir "La cantidad de credos es " cerdocon
	Escribir "La cantidad de cerdos enfermos es " cerdoenfcon
	Escribir "La cantidad de cabra es " cabracon
	Escribir "La cantidad de cabras enfermas es " cabraenfcon
FinAlgoritmo
