Algoritmo Granja_corrales
	Definir vacas, cerdos, cabras, vacas_enfermas, cerdos_enfermos, cabras_enfermas, vacas_sanas, cerdos_sanos, cabras_sanas, cant_animales, corral_vacas, corral_cerdos, corral_cabras, cant_corral_vacas, cant_corral_cerdos, cant_corral_cabras Como Real
	Definir estado_salud, animal, finalizar Como Caracter
	
	Escribir "Ingresar animal y su estado de salud, si no hay más animales escribir: finalizar"
	Escribir ""
	
Mientras animal<>"finalizar" y estado_salud<>"finalizar" //Cuando la palabra "finalizar" sea ingresada el proceso terminará
		Escribir "¿Qué animal es?"
		Leer animal
	si animal="vaca" //Si el animal es una vaca se suma a las vacas al corral de las mismas
		vacas=vacas+1
		corral_vacas=corral_vacas+1
		Escribir "¿Está sana o enferma?"
		Leer estado_salud
		si estado_salud="enferma" //Si la vaca está enferma se suma a las vacas enfermas
			vacas_enfermas=vacas_enfermas+1
		FinSi
	FinSi
		si animal="cerdo" //Si el animal es un cerdo se suma a los cerdos y al corral de los mismos
			cerdos=cerdos+1
			corral_cerdos=corral_cerdos+1
			Escribir "¿Está sano o enfermo?"
			Leer estado_salud
			si estado_salud="enfermo" //Si el cerdo está enfermo se suma a los cerdos enfermos
				cerdos_enfermos=cerdos_enfermos+1
			FinSi
		FinSi
			si animal="cabra" //Si el animal es una cabra se suma a las cabras y al corral de las mismas
				cabras=cabras+1
				corral_cabras=corral_cabras+1
				Escribir "¿Está sana o enferma?" 
				Leer estado_salud
				si estado_salud="enferma" //Si la cabra está enferma se suma a las cabras enfermas
					cabras_enfermas=cabras_enfermas+1
				FinSi
			FinSi
				si corral_vacas=19 //Si el corral se llena se suma a la cantidad de corrales de vacas y se "vacía el corral" para que quede vacío
					corral_vacas=0
					cant_corral_vacas=cant_corral_vacas+1
				FinSi
					si corral_cerdos=19 //Si el corral se llena se suma a la cantidad de corrales de cerdos y se "vacía el corral" para que quede vacío
						corral_cerdos=0
						cant_corral_cerdos=cant_corral_cerdos+1
					FinSi
						si corral_cabras=19 //Si el corral se llena se suma a la cantidad de corrales de cabras y se "vacía el corral" para que quede vacío
							corral_cabras=0
							cant_corral_cabras=cant_corral_cabras+1
						FinSi
FinMientras
vacas_sanas=vacas-vacas_enfermas
cabras_sanas=cabras-cabras_enfermas
cerdos_sanos=cerdos-cerdos_enfermos
//Los animales sanos se cuentan restando la cantidad de animales enfermos a los animales en total (de cada especie)
Escribir "Hay " vacas " vacas, " vacas_sanas " de ellas son sanas y " vacas_enfermas " enfermas" 
Escribir "Hay " cabras " cabras, " cabras_sanas " de ellas son sanas y " cabras_enfermas " enfermas" 
Escribir "Hay " cerdos " cerdos, " cerdos_sanos " de ellos son sanos y " cerdos_enfermos " enfermos" 
Escribir ""
Escribir "Se llenaron " cant_corral_vacas " corrales de vacas y " corral_vacas " de ellas no pudieron conformar un corral"
Escribir "Se llenaron " cant_corral_cerdos " corrales de cerdos y " corral_cerdos " de ellos no pudieron conformar un corral"
Escribir "Se llenaron " cant_corral_cabras " corrales de cabras y " corral_cabras " de ellas no pudieron conformar un corral"
FinAlgoritmo
