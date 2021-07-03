#EJERCICIO 1
print("Hola a todos")

#EJERCICIO 2
miCadena ="!Hola mundo!"
print(miCadena)

#EJERCICIO 3
nombre = input("Pon tu nombre: ")
print("!Hola" +nombre+ "!")

#EJERCICIO 4
n=int(input("INGRESE CANTIDAD DE ESCALONES: "))
for i in range(n+1):
    print('$'*i)

#EJERCICIO 5
num=int(input("INGRESE UN VALOR: "))
if num > 1:
    cont = 0
    for i in range(2, num):
        resto=num%i
        if resto==0:
            cont+=1
    if cont==0:
        print("EL NUMERO: " +str(num)+ "ES PRIMO")
    else :
            print("EL NUMERO: "  +str(num)+ "NO ES PRIMO")

# EJERCICIO 6
clave_usuario = "contrasena"
Llave = input("INTRODUZCA LA LLAVE: ")
if clave_usuario == Llave.lower():
    print("ACCESO CONCEDIO, LA LLAVE COINCIDE")
else :
        print("CONTRASEÑA INCORRECTA, LA LLAVE NO COINCIDE IDIOTA")

#EJERCICIO 10
Frutas = ["manaza","banana","pera"]
for x in Frutas:
    print(x)

#EJERCICIO 9
a = 200
b = 33
if a>b:
    print ("La tuya")
elif a == b:
    print("la tuya tambien")
else:
    print("la tuya x2")

#EJERCICIO 7
n1 = 8
n2 = 9
def max (n1, n2):
    if n1<n2:
        print (n2)
    elif n2<n1:
        print (n1)
    else:
        print("Son iguales") 




