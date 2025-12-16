while True:
    dato = input("write your user name: ")
    dato1 = input("write your password : ")
    
    if dato == "carlos" and dato1 == "131201":
        print(f"Hola {dato}, tu clave es correcta.")
        break
    else:
        print("Acceso denied")

print("hola bienvenido a la tienda de mascotas presione enter para continuar")
input()
print("selecione 1 para el catalogo 2 para salir ")