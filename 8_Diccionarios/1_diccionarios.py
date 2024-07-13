#Los diccionarios son como los objetos en js

#clave y valor, no se puede repetir la clave

diccionario ={"Usuario": "nrusin", "Password": 12345, "Estatura": 1.50, "Edad":27};

print(diccionario);
print(type(diccionario));

print(diccionario.values()); #Trae todos los valores de la lista

print(diccionario["Edad"]); #Muestra el valor de una clave pasada por parametros

diccionario["Peso"]="50KG"; #Agrega nuevas claves y sus valores a la lista

print(diccionario);

diccionario["Password"]=123; #Modifica una clave existente

print(diccionario);