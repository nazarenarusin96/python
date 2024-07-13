cadena = "Texto de prueba para metodos booleanos";

cadena2 = "TEXTO EN MAYUSCULAS";

cadena3= "texto en minusculas"

print(cadena.startswith("T")); #Valida que el string comience con el caracter ingresado por parametro, es sensible a minusculas y mayusculas

print(cadena.startswith("t"));

print("##########################################");

print(cadena.endswith("s")); #Valida que el string termine con el caracter ingresado por parametro, es sensible a minusculas y mayusculas

print(cadena.endswith("S"));

print("##########################################");

print(cadena2.isupper()); #Valida que el string este todo em mayusculas

print("##########################################");

print(cadena3.islower()); #Valida que el string este todo em minusculas