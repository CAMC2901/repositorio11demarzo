acum=0
acum_bajo=0
acum_medio=0
acum_alto=0
mejor_nota=0
mejor_estudiante=""
n=int(input("cuantos estudiantes va a registrar: "))
for i in range(n):
 nombre=str(input("ingrese su nombre: "))
 speaking=int(input("ingrese su nota de speaking: "))
 listening=int(input("ingrese su nota de listening: "))
 reading=int(input("ingrese su nota de reading: "))
 promedio=(speaking+listening+reading)/3
 acum+=promedio
 if promedio < 60:
  acum_bajo+=1
  print("nivel bajo")
 elif promedio >= 60 and promedio <= 79:
    acum_medio+=1
    print("nivel medio")
 else:
     acum_alto+=1
     print("nivel alto")
 if promedio > mejor_nota:
      mejor_nota = promedio
      mejor_estudiante = nombre
print("el promedio del grupo es: ", acum/n)
print("el numero de estudiantes con nivel bajo es: ", acum_bajo)
print("el numero de estudiantes con nivel medio es: ", acum_medio)
print("el numero de estudiantes con nivel alto es: ", acum_alto)
print("el estudiante con mejor nota es: ", mejor_estudiante, "con una nota de: ", mejor_nota)
