Algoritmo Censo_de_animales_C5_3
		
		Definir animal, final Como Caracter
		Definir vacacon, vacaenfcon, cabracon, cabraenfcon, cerdoenfcon Como Entero
		
		Mientras animal<>"listo"
			Escribir "¿Que es?"
			Escribir "Escriba lo que ve especie y estado de salud"
			Escribir "Si quiere finalizar el sistema escriba listo"
			
			//Variable animal
			leer animal
			
			//Comprobacion de especie y estado de salud
			si animal="vaca"
				vacacon=vacacon+1
				corralvaca=corralvaca+1
			FinSi
			si animal="cerdo"
				cerdocon=cerdocon+1
				corralcerdo=corralcerdo+1
			FinSi
			si animal="cabra"
				cabracon=cabracon+1
				corralcabra=corralcabra+1
			FinSi
			si animal="vaca enferma"
				vacaenfcon=vacaenfcon+1
				corralvaca=corralvaca+1
			FinSi
			si animal="cerdo enfermo"
				cerdoenfcon=cerdoenfcon+1
				corralcerdo=corralcredo+1
			FinSi
			si animal="cabra enferma"
				cabraenfcon=cabraenfcon+1
				corralcabra=corralcabra+1
			FinSi
			
			//Corrales contadores
			si corralvaca=19
				cantcorralvaca=cantcorralvaca+1
				corralvaca=0
			FinSi
			si corralcerdo=19
				cantcorralcerdo=cantcorralcerdo+1
				corralcerdo=0
			FinSi
			si corralcabra=19
				cantcorralcabra=cantcorralcabra+1
				corralcabra=0
			FinSi
		FinMientras
		
		//Cantidad de animales por especie sin corral
		si corralvaca<>0
			Escribir "La cantidad de vacas sin corral son " corralvaca
		FinSi
		si corralcerdo<>0
			Escribir "La cantidad de cerdo sin corral son " corralcerdo
		FinSi
		si corralcabra<>0
			Escribir "La cantidad de cabra sin corral son " corralcabra
		FinSi
		
		//Cantidad de corrales
		Escribir "**************************************************"
		Escribir  "**    " "La cantidad de corrales de vacas son " cantcorralvaca "    **"
		Escribir  "**    " "La cantidad de corrales de cerdo son " cantcorralcerdo "    **"
		Escribir  "**    " "La cantidad de corrales de cabra son " cantcorralcabra "    **"
		Escribir "**************************************************"
		
		//Escritura de resultados
		Escribir "La cantidad de vacas son " vacacon
		Escribir "La cantidad de vacas enfermas son " vacaenfcon
		Escribir "La cantidad de cerdos son " cerdocon
		Escribir "La cantidad de cerdos enfermos son " cerdoenfcon
		Escribir "La cantidad de cabra son " cabracon
		Escribir "La cantidad de cabras enfermas son " cabraenfcon
FinAlgoritmo
