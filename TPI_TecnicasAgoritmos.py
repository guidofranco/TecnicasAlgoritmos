
import random

def inicializarTabla(fi,col):
	tabla=[0]*(fi)
	for i in range(fi):
		tabla[i]=[0]*(col)
	return tabla

def cargarIntereses(tabla, filas, colum):
	for i in range(filas):
		for j in range(1,colum):
			tabla[i][j] = (j*1000) + random.randint(1,1000) 
	return tabla
#Aplicando programación dinámica
def interesesPD(matrizF, matrizI, nroBancos, monto):
	for i in range(0, nroBancos):
		matrizI[i][0] = 0 
	for j in range(1, monto+1):
		matrizI[0][j]=matrizF[0][j]
	for i in range(1, nroBancos):
		for j in range (1, monto+1):
			matrizI[i][j] = max2(matrizI, matrizF, i,j)
	return matrizI[-1][-1]

def max2(matrizI, matrizF, i, j):
	maxSal = matrizI[i-1][j] + matrizF[i][0]
	for t in range(1, j+1):
		maxSal = max(maxSal, matrizI[i-1][j-t] + matrizF[i][t])
	return maxSal
#Fin del algoritmo empleando programación dinámica
#--
#Aplicando backtracking
def interesesBT(bancos, monto, acumulado):
	if ( (bancos > cantBancos) or (monto == 0) ):
		return acumulado
	valMax = -1
	for plata in range(0, monto+1):
	#se coloca el +1 para que el rango esté compuesto por numeros entre 0 y monto
	#y así se pueda iterar sobre todos esos nros
		valAct = interesesBT(bancos+1, monto-plata, acumulado+matrizF[bancos-1][plata])
		
		if valAct > valMax:
			valMax = valAct					
	return valMax
#fin del algoritmo empleando backtracking

#algoritmo avido
def interesesAV(monto, acum, filas):
	
	for k in range(cantBancos-1):
		sumas=[]
		for fi in range(0, filas):
			sumas.append(sum(matrizF2[fi]))
		maxSumas = max(sumas)
		indice = sumas.index(maxSumas)
		valMax = max(matrizF2[indice][:monto+1])
		monto-= matrizF2[indice].index(valMax) #a monto le resto el dinero que invierto en ese banco
		#monto = monto - j, donde j: 1<=j<=TotalDinero
		acum+=valMax + matrizF2[indice].index(valMax)*1000
		for co in range(0, miDinero+1):
			matrizF2[indice][co]=0
	
	for fi in range(0, filas):
		sumas.append(sum(matrizF2[fi]))
	maxSumas = max(sumas)
	indice = sumas.index(maxSumas)		
	acum+=matrizF2[indice][monto]+monto*1000
	return (acum)
#fin avido

cantBancos = 4
miDinero = 9 #es el monto M

matrizF=inicializarTabla(cantBancos,miDinero+1)
cargarIntereses(matrizF, cantBancos, miDinero+1)
matrizF2 = inicializarTabla(cantBancos,miDinero+1) #para el algoritmo avido
for i in range(cantBancos):
	for j in range(miDinero+1):
		matrizF2[i][j] = matrizF[i][j] - (j*1000) #para el algoritmo avido

print('TABLA DE INTERESES')
for k in range(cantBancos):
	print(matrizF[k])		
print('')


matrizI=inicializarTabla(cantBancos, miDinero+1)
print('Resultado con programación dinámica:')
print(interesesPD(matrizF, matrizI, cantBancos, miDinero))
print('')
print("Matriz rellenada con programación dinámica")
for k in range(cantBancos):
	print(matrizI[k])

print('')
print('Resultado con backtracking:')

print(interesesBT(1, miDinero, 0))	

print('')
print('Resultado del algoritmo avido:')
sumas=[] #para el algoritmo avido
print(interesesAV(miDinero, 0, cantBancos))