if __name__ == '__main__':
	matriz = float()
	sumatoria = float()
	ac = float()
	matriz = [[float() for ind0 in range(12)] for ind1 in range(12)]
	letra = input()

	for i in range(0,12):
		for j in range(0,12):
			matriz[i-1][j-1] = float(input())

	for i in range(0,6):
		for j in range(0,6):
			if i<=j:
				sumatoria = sumatoria+matriz[i-1][j-1]
				ac = ac+1

	for i in range(6,12):
		for j in range(0,6):
			if (i+j)<=12:
				sumatoria = sumatoria+matriz[i-1][j-1]
				ac = ac+1

	if letra=="S":
		print(int(sumatoria*10)/10)
	if letra=="M":
		print(int((sumatoria/ac)*10)/10)
