nombre= input("ingresa tu nombre")
materia_favorita=input("¿cual es tu materia favorita?")
edad=int(input("ingresa tu edad"))
print("nombre",nombre,"edad",edad,"cual es tu materia favorita", materia_favorita)
print(type(nombre))

if edad>= 16 :
   print("con", edad ,"años se puede votar")

else :
   print("no se puede votar con" , edad , "años")