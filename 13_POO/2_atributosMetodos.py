class FabricaTelefonos():
    #Atributos (caracteristicas)
    marca = "Samsung"
    color = "Negro"
    ram = 32
    storage = 128

    #Metodos (acciones)
    def llamar(self, mensaje):
        return mensaje;

    def escuchandoMusica(self):
        print("Escuchando musica");

telefono = FabricaTelefonos();
telefono.marca
telefono.color
telefono.ram
telefono.storage

#Mostrando los atributos pasados por parametro
print(telefono.storage);

#Ejecutando el metodos
print(telefono.llamar("Mensaje de prueba"));
telefono.escuchandoMusica();