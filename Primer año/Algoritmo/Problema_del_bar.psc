Algoritmo Problema_del_bar
	Escribir "Ingrese un producto de entre jugo de manzana, jugo de naranja o jugo de mango"
	Escribir "Al finalizar el dia escriba fin"
	
	Mientras bebida<>"fin"
		Leer bebida 
		Si bebida="jugo de naranja"
			cantidad_de_jugo_de_naranja=cantidad_de_jugo_de_naranja+1
		FinSi
		Si bebida="jugo de manzana"
			cantidad_de_jugo_de_manzana=cantidad_de_jugo_de_manzana+1
		FinSi
		Si bebida="jugo de mango"
			cantidad_de_jugo_de_mango=cantidad_de_jugo_de_mango+1
		Finsi
		Si bebida <>"jugo de naranja" y bebida <>"jugo de manzana" y bebida <>"jugo de mango" y bebida <> "fin"
			escribir "Ingrese un producto valido"
		FinSI
	FinMientras
	Dinero_de_naranja=cantidad_de_jugo_de_naranja*100
	Dinero_de_manzana=cantidad_de_jugo_de_manzana*150
	Dinero_de_mango=cantidad_de_jugo_de_mango*200
	
	Dinero_caja=Dinero_de_naranja+Dinero_de_manzana+Dinero_de_mango
	Si cantidad_de_jugo_de_naranja>cantidad_de_jugo_de_manzana y  cantidad_de_jugo_de_naranja>cantidad_de_jugo_de_mango
		entonces
		la_mas_consumida="Jugo de naranja"
	FinSi
	
	Si cantidad_de_jugo_de_manzana>cantidad_de_jugo_de_naranja y  cantidad_de_jugo_de_manzana>cantidad_de_jugo_de_mango
		entonces
		la_mas_consumida="Jugo de manzana"
	FinSi
	Si cantidad_de_jugo_de_mango>cantidad_de_jugo_de_naranja y  cantidad_de_jugo_de_mango>cantidad_de_jugo_de_manzana
		entonces
		la_mas_consumida="Jugo de mango"
	FinSi
	Si cantidad_de_jugo_de_mango=cantidad_de_jugo_de_naranja o cantidad_de_jugo_de_mango=cantidad_de_jugo_de_manzana
		entonces
		la_mas_consumida="Hay dos igual de vendidas"
	FinSi
	
	Escribir "El ingreso por jugo de manzana " Dinero_de_manzana
	Escribir "El ingreso por jugo naranja " Dinero_de_naranja
	Escribir "El ingreso por jugo de mango " Dinero_de_mango
	Escribir "Ingresos totales " dinero_caja
	Escribir "La cantidad de jugos de naranja fué " cantidad_de_jugo_de_naranja
	Escribir "La cantidad de jugos de manzana fué " cantidad_de_jugo_de_manzana
	Escribir "La cantidad de jugos de mango fué " cantidad_de_jugo_de_mango
	Escribir "El jugo mas comprado fue " la_mas_consumida

FinAlgoritmo
