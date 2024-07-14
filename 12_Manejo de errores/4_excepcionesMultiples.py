#Validación para cancelar la ejecución con ctrl+c

while True:
    try:
        edad = int(input ("Ingrese su edad: "));
        print("Tu edad es: ",edad);
        break
    except KeyboardInterrupt:
        print("Ejecución cancelada");
        break