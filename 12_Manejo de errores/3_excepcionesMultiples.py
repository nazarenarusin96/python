#Validación de error con enteros, no se puede ingresar strings

while True:
    try:
        edad = int(input ("Ingrese su edad: "));
        print("Tu edad es: ",edad);
        break
    except ValueError:
        print("Valor erroneo");