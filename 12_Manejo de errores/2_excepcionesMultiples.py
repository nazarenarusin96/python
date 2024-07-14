#Validación de error con números

while True:
    try:
        num = int(input ("Ingrese un numero: "));
        resultado = 100/num
        print(resultado);
        break;
    except:
        ZeroDivisionError
        print("No se puede dividir entre 0");
        break; 
