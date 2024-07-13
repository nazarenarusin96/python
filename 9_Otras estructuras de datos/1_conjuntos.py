#set se encarga de crear los conjuntos

#En las listas se pueden repetir valores, en los conjuntos no

conjunto =set[(1, 2, 3, 4, 5, 6)];

print(type(conjunto));

conjuntoRepetido ={1,1,3,4,5,6,7,7,8,8};

lista=[1,1,1,3,45,6,7,8,9,9,9,10];

print(conjuntoRepetido);
print(lista);

conjuntoRepetido.add(20); #Agrega elementos pasando el valor por parametro al conjunto
print(conjuntoRepetido);

print("#####################################");

conjuntoRepetido.remove(5); #Elimina elementos pasados por parametros del conjunto
print(conjuntoRepetido);

conjuntoRepetido.discard(1); #Elimina elementos pasados por parametros del conjunto
print(conjuntoRepetido);

conjuntoRepetido.pop(); #Elimina de manera aleatoria elementos del conjunto
print(conjuntoRepetido);

conjuntoRepetido.update([67,89,443]); #Agrega varios elementos iterables al conjunto
print(conjuntoRepetido);

conjuntoRepetido.clear(); #Limpia el conjunto
print(conjuntoRepetido);