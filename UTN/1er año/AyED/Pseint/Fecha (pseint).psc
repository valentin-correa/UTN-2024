Algoritmo Fechas
		Definir dia, mes, a�o, fecha como enteros
		Escribir "Escriba una fecha"
		Leer dia, mes, a�o
		
		si mes=1 o mes=3 o mes=5 o mes=7 o mes=8 o mes=10 y dia>0 y dia<=31 y a�o>=0
			fecha=fecha+1
			//Si se cumplen las condiciones se toma como fecha v�lida ("1")
		FinSi
		si mes=4 o mes=6 o mes=9 o mes=11 o mes=12 y dia>0 y dia<=30 y a�o>=0
			fecha=fecha+1
			//Si se cumplen las condiciones se toma como fecha v�lida ("1")
		FinSi
		si dia>0 y dia<=28 y a�o>=0 y mes=2
			fecha=fecha+1
			//Si se cumplen las condiciones se toma como fecha v�lida ("1")
		FinSi
		si fecha=1 Entonces
			//Si la fecha es igual a 1 es v�lida, sino no
			Escribir "La fecha es v�lida"
			sino
			Escribir "La fecha no es v�lida"
		FinSi
		
FinAlgoritmo
