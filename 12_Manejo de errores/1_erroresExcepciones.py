while True:
    try:
        edad = int(input ("Ingrese su edad: "));
        print("Tu edad es: ", edad);
        break;
    except:
        print("Valor erroneo");
    finally:
        print("La ejecución finalizo");