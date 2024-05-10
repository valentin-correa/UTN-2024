SubAlgoritmo indiceG=MasGrande(v1)
	Mayo=0
	Para i=1 Hasta 4
		Si v1(i)>Mayo
			v1(i)=Mayo
			inidiceG=i
		FinSi
	FinPara
FinSubAlgoritmo 

SubAlgoritmo SBigN=NGrande(v1)
	Mayo=0
	Para i=1 Hasta 4
		Si v1(i)>Mayo y i<>indiceG
			v1(i)=Mayo
			inidiceSG=i
		FinSi
	FinPara
FinSubAlgoritmo

Algoritmo P16_2
	Dimension  v1(4)
	Para i=1 Hasta 4
		Leer v1(i)
	FinPara
FinAlgoritmo
