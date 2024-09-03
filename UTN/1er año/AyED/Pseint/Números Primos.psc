//C4- 4 Diseñar un algoritmo que permita el ingreso de una serie de números y determinar cuáles de esos números son primos. Además se pide la suma total de los números primos ingresados.
Algoritmo NumPrimos
	Definir cant, num2, suma_primos, contador Como real
	
	Escribir "Cuántos números quiere ingresar?"
	leer cant
	//Se le pregunta al usuario cuantos números va a ingresar para que este valor sirva de límite en el ciclo
	suma_primos=0
	contador=0
	
	Escribir "Ingrese una serie de números"

Mientras contador<cant //Ciclo que define cuánto durará el proceso
	Leer num2
	
	si num2=2 o num2=3 o num2=5 o num2=7 o num2=11 //Si el número ingresado es 2, 3, 5, 7 u 11 será tomado como primo
		Escribir num2 " es un número primo"
		suma_primos=suma_primos+num2
	FinSi
	si num2<>3 y num2%11=0 o num2%7=0 o num2%5=0 o num2%3=0 o num2%2=0 //Determina si el número ingresado es primo o no
		SiNo
		Escribir num2 " es un número primo"
		suma_primos=suma_primos+num2
	FinSi
	contador=contador+1
FinMientras
	Escribir "La suma de los números primos es " suma_primos
	//Suma de los números primos
FinAlgoritmo
