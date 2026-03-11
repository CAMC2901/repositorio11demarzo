n=int(input("ingrese un numero: "))
matriz=[]
for  i in range(n):
    fila=[]
    for j in range(n):
        if j == 0 or j == i: 
         fila.append(1)
        elif j < i:
           fila.append(matriz[i-1][j-1] + matriz[i-1][j])
        else:
           fila.append(0)

    matriz.append(fila)

for fila in matriz:
   print(fila)