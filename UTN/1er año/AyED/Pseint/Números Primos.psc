//C4- 4 Dise�ar un algoritmo que permita el ingreso de una serie de n�meros y determinar cu�les de esos n�meros son primos. Adem�s se pide la suma total de los n�meros primos ingresados.
Algoritmo NumPrimos
	Definir cant, num2, suma_primos, contador Como real
	
	Escribir "Cu�ntos n�meros quiere ingresar?"
	leer cant
	//Se le pregunta al usuario cuantos n�meros va a ingresar para que este valor sirva de l�mite en el ciclo
	suma_primos=0
	contador=0
	
	Escribir "Ingrese una serie de n�meros"

Mientras contador<cant //Ciclo que define cu�nto durar� el proceso
	Leer num2
	
	si num2=2 o num2=3 o num2=5 o num2=7 o num2=11 //Si el n�mero ingresado es 2, 3, 5, 7 u 11 ser� tomado como primo
		Escribir num2 " es un n�mero primo"
		suma_primos=suma_primos+num2
	FinSi
	si num2<>3 y num2%11=0 o num2%7=0 o num2%5=0 o num2%3=0 o num2%2=0 //Determina si el n�mero ingresado es primo o no
		SiNo
		Escribir num2 " es un n�mero primo"
		suma_primos=suma_primos+num2
	FinSi
	contador=contador+1
FinMientras
	Escribir "La suma de los n�meros primos es " suma_primos
	//Suma de los n�meros primos
FinAlgoritmo
