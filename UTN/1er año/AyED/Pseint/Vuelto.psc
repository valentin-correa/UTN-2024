Algoritmo Vuelto
	Definir pago, precio, vuelto1, billetes_1, billetes_5, billetes_10, resto1, resto2 Como Real
	
	Escribir "Ingresar precio del producto"
	Leer precio
	Escribir "Ingresar pago hecho"
	Leer pago
	
	vuelto1=pago-precio
	
	billetes_10=trunc(vuelto1/10)
	resto1=vuelto1/10-billetes_10
	
	billetes_5=trunc(10*resto1/5)
	resto2=10*resto1/5-billetes_5
	
	billetes_1=resto2*5
	
	Escribir "El vuelto se da con:"
	Escribir ""
	Escribir billetes_10 " billetes de 10"
	Escribir billetes_5 " billetes de 5"
	Escribir  billetes_1 " billetes de 1" 
FinAlgoritmo
