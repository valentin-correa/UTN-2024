Algoritmo Bar
	Definir  manzana, naranja, mango, cant_manzana, cant_mango, cant_naranja, cant_total, ingreso Como Entero
	Definir bebida Como Caracter
	
	Escribir "-----------------------------------------"
	Escribir "               Bebidas Bar"
	Escribir "-----------------------------------------"
	
	Escribir "Cuando el día haya finalizado escriba Día finalizado"
	Escribir ""
	
	Mientras bebida<>"Día finalizado"
		Escribir "Ingrese bebida vendida"
		Leer bebida
		
		si bebida="jugo de manzana"
			manzana=manzana+100
			cant_manzana=cant_manzana+1
			cant_total=cant_total+1
			ingreso=ingreso+100
		Finsi		
			si	bebida="jugo de naranja"
				naranja=naranja+150
				cant_naranja=cant_naranja+1
				cant_total=cant_total+1
				ingreso=ingreso+150
			Finsi		
				si bebida="jugo de mango"
					mango=mango+200
					cant_mango=cant_mango+1
					cant_total=cant_total+1
					ingreso=ingreso+200
				Finsi
	FinMientras
	Escribir "------------------------------------------"
	Escribir " Se vendieron " cant_total " bebidas"
	Escribir ""
	Escribir " Ingresaron " ingreso " pesos"
	Escribir ""
	si cant_manzana>cant_naranja y cant_manzana>cant_mango
		Escribir " La bebida más vendida fue Jugo de manzana"
	Finsi	
		si cant_naranja>cant_manzana y cant_naranja>cant_mango
			Escribir " La bebida más vendida fue Jugo de naranja"
		FinSi
			si cant_mango>cant_manzana y cant_mango>cant_naranja
				Escribir " La bebida más vendida fue Jugo de mango"
			FinSi
	Escribir ""
	Escribir " Se vendieron " manzana " pesos de jugo de manzana"
	Escribir " Se vendieron " naranja " pesos de jugo de naranja"
	Escribir " Se vendieron " mango " pesos de jugo de mango"
	Escribir "------------------------------------------"

FinAlgoritmo
