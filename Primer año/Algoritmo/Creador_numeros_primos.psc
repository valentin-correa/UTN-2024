Algoritmo Creador_numeros_primos
	Escribir "Escriba cuantos numeros primos quiere"
	Leer numeros_primos
	Mientras numeros_primos>contador
		num=azar(999999999)
		resto1=num%2
		resto2=num%3
		resto3=num%5
		resto4=(num+1)%2
		si resto1<>0 y resto2<>0 y resto3<>0 y resto4=0 o num=2 o num=3 o num=5
			Entonces
			Escribir num
			contador=contador+1
		FinSi
FinMientras
FinAlgoritmo
