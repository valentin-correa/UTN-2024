Algoritmo ejercicio_4_2
	Escribir "Ingrese tiempo de estancia"
	Leer estancia
	Escribir "Ingrese distancia"
	Leer distancia
	precio=distancia*2.5
	Si estancia>7 y distancia>800 
		entonces
		descuento=0.3*precio
		precio_final=precio-descuento
	sino precio_final=precio
	Finsi
	
	Escribir "El precio final es " precio_final

FinAlgoritmo
