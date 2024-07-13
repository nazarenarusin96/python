diccionario ={1:2, 2:3, 3:4, 4:5}

diccionario2 ={10:11, 24:67}


print(diccionario);

diccionario.pop(3); #A diferencia que las listas, con pop si se tiene que pasar parametro (no existe el 0 en los diccionarios)

print(diccionario);

print(diccionario.get(2)); #Trae el valor de la llave deseada, en este caso el valor es 3 

diccionario.setdefault(5,6); #Agrega un nuevo valor a la lista

print(diccionario);

diccionario.update(diccionario2); #Concatena 2 diccionarios, cuidado con las llaves repetidas

print(diccionario);

print(diccionario2.copy()); #Crea una copia de un diccionario

diccionario.clear() #Limpia toda la lista

print(diccionario);