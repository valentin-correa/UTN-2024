//C4- 4 Diseñar un algoritmo que permita el ingreso de una serie de números y determinar cuáles de esos números son primos. Además se pide la suma total de los números primos ingresados. 
Algoritmo Numeros_Primos_536870911
	resultado=0
	Escribir "Ingrese cantidad de numeros a analizar"
	leer contador
	Mientras num1<contador
		Escribir "Ingrese un numero"
		Leer num
		resto1=num%2
		resto2=num%3
		resto3=num%5
		resto4=(num+1)%2
		si resto1<>0 y resto2<>0 y resto3<>0 y resto4=0 o num=2 o num=3 o num=5
			Entonces
			Escribir num " Es un numero primo"
			resultado=num+resultado
			sino escribir num " No es primo"
		FinSi
		num1=num1+1
	FinMientras
	Escribir "La suma de todos los numeros primos es " resultado
FinAlgoritmo