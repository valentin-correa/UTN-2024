Algoritmo PrecioBillete
	Definir distancia, estancia, precio, descuento Como Real
	
	Escribir "�De cu�nto tiempo ser� su estancia?"
	Leer estancia
	Escribir "�Cu�ntos kil�metros recorrer�?"
	Leer distancia
	//Se recopila informaci�n necesaria para determinar si se aplica o no el descuento
	
	precio=distancia*2.5 //Se calcula precio sin descuento
	
	si estancia>7 y distancia>800 //Si se cumplen las condiciones se aplica el descuento
		precio=precio-(precio*30/100)
	SiNo
		precio=precio //Si no se cumplen las condiciones el precio no cambia
	FinSi
	Escribir "El precio de su billete es de " precio " euros" //Se muestra el precio
FinAlgoritmo
