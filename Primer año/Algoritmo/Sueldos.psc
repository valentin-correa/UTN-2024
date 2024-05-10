Algoritmo Sueldos
	Leer Valor_hora
	Leer Horas_trabajadas
	Si Horas_trabajadas>40 Entonces
		horas_extras<-Horas_trabajadas-40
		valor_horas_extra<-horas_extras*valor_hora*1.5
		resultado<-valor_horas_extra+40*valor_hora
	SiNo
		resultado<-Horas_trabajadas*valor_hora
	
	Fin Si
	Escribir resultado
FinAlgoritmo
