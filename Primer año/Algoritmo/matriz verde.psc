Proceso matrizverde
	
	definir sum, prom, matriz Como real
	definir x Como Entero
	definir s, m, calculo Como Caracter
	
	dimension matriz(12,12)
	
	escribir "quiere hacer una suma o un promedio? (s/m)"
	leer calculo
	si calculo='s' o calculo='m'
		para i=1 hasta 12
			para j=1 hasta 12
				escribir "ingrese numero " j " de la fila " i
				leer matriz(i,j)
			FinPara
		FinPara
		
		x=11
		sum=0
		
		para i=1 hasta 12
			para j=x hasta 1 con paso -1
				sum = sum + matriz(i,j)
			FinPara
			x=x-1
		FinPara
		
		si calculo='m'
			prom = trunc((sum/66)*10) / 10.0
			
			escribir "el promedio es " prom
		SiNo
			sum = trunc(sum*10) / 10.0
			escribir "la suma es " sum
		FinSi
	SiNo
		escribir "ingrese una opcion valida"
	FinSi
	
	
FinProceso
