lista = [1,2,3,4,5];


lista.append(6); #Agrega un elemento al final de la lista

lista.append("Python");

print(lista);

lista.insert(0,0); #Agrega un elemento en la posición de la lista deseada

print(lista);

lista.append("Python");

print(lista.count("Python")); #Devuelve cuantas veces aparece en la lista el parametro deseado

print(lista.count("python"));

print(lista.index(4)); #Busca y muestra en que posición se encuentra el elemento de la lista

print("#####################################");

lista2 = [6,2,3,9,4,6,0,1];

lista2.sort(); #Ordena de forma ascendente la lista
print(lista2)

lista2.reverse(); #Ordena de forma descendente la lista
print(lista2);

print("#####################################");

datos = ["Naza", "Rusin", "lanus", "Python", "Javascript",  27, 30];

print(datos);

datos [2] ="Lanus Este"; #Modifica el elemento de una lista

print(datos[2]);
print(datos);

print("#####################################");

datos.pop(); #Elimina el ultimo elemento de una lista, en este caso el 30
print(datos);

datos.remove("Javascript"); #Elimina el elemento deseado por parametro, en este caso Javascript
print(datos);