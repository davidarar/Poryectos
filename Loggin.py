'''
-damos una bienvenida 
-pedimos datos 
-imprimimos datos 

'''
print(""" 
         ***********************************************   
         ********Bienvenido Al sistema de registro******
         ***********************************************
         
      """)

print("Dijite su Nombre")
nombre = input()
print("Su nombre es: ", nombre)

print("Dijite su Primer Apellido")
apellido1 = input()
print("Su Primer Apellido es: ", apellido1)

print("Dijite su Segundo Apellido")
apellido2 = input()
print("Su Primer Apellido es: ", apellido2)

print("Dijite su edad")
edad = input()
print("edad : ", edad)

print("Dijite su Numero de telefono")
telefono = input()
print("Su Numero de telefono es : ", telefono)


Registro=(nombre)
registro1=(apellido1)
registro2=(apellido2)
registro4=(edad)
registro3=(telefono)

print("\nSus Datos Son:")

print("\nNombre",Registro)
print("\nPrimer Apellido:",registro1)
print("\nSuegundo Apellido:",registro2)
print("\nEdad",registro4)
print("\nNumero de Telefono:",registro3)

print(""" 
      **************************
      ***Bienvenido al Loging***
      **************************
      """)

def agregar_persona(l):
    nueva_persona=dict()
    nueva_persona['nombre']=input ("Nombre: ")
    nueva_persona['apellido1']=input ("Primer apellido: ")
    nueva_persona['apellido2']=input ("Segundo apellido: ")
    nueva_persona['cedula']=tuple ((input('Cedula: '),))
    if ("S"==input('Desea agregar telefonos (S o N):').upper()):
        lista_telefono=[]
        while True:
            lista_telefono.append(input("Número de teléfono: "))
            if ("N"==input('Desea agregar más telefonos (S o N):').upper()):
                break
        nueva_persona['telefono']=lista_telefono


