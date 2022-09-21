#1.- Mostrar por pantalla un "Hola Mundo".
print("\n\n1.- Mostrar por pantalla un \"Hola Mundo\".")
print("Hola mundo")


#2.- Guardar una lista de asignaturas y mostrarlas por pantalla.
print("\n\n2.- Guardar una lista de asignaturas y mostrarlas por pantalla.")
subjects = ["Mates", "Biología", "Gimnasia"]
print(subjects)


#3.- Mostrar cada una de las anteriores asignaturas por pantalla una a una.
print("\n\n3.- Mostrar cada una de las anteriores asignaturas por pantalla una a una.")
print(subjects[0:3])

print("\n")
print(subjects[0])
print(subjects[1])
print(subjects[2])

print("\n")
i=0
while i < len(subjects):
    print(subjects[i])
    i = i+1
    
print("\n")
for x in range(0, len(subjects)):
    print(subjects[x])
    
print("\n")
for subject in subjects:
    print(subject)
    
    
#4.- Mostrar cada una de las anteriores asignaturas por pantalla una a una, excepto la segunda asignatura.
print("\n\n4.- Mostrar cada una de las anteriores asignaturas por pantalla una a una, excepto la segunda asignatura")
for x in range(0, len(subjects)):
    if x == 1:
        continue
    else:
        print(subjects[x])

print("\n")        
for x in range(0, len(subjects)):
    if x != 1:
        print(subjects[x])


#5.- Mostrar el siguiente dibujo por pantalla (obviando las almohadillas):
#--------
#|oxxxxx|
#|xooxxx|
#|xoooox|
#|xxxoxx|
#|xxxxox|
#|xxxxxo|
#--------
print("\n\n5.- Mostrar el siguiente dibujo por pantalla (obviando las almohadillas)")
print("|oxxxxx|")
print("|xooxxx|")
print("|xoooox|")
print("|xxxoxx|")
print("|xxxxox|")
print("|xxxxxo|")



#RECOMENDACIÓN: https://ellibrodepython.com