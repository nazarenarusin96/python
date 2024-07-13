nombre = input("Ingrese su nombre: ");

edad = int(input ("Ingrese su edad: "));

print(nombre,edad);

#La concatenación en python es con , no con +

print("###############################################");

print("Hola ", nombre, " tienes ", edad, " años");

print("###############################################");

print("Hola {} tienes {} años".format(nombre,edad));