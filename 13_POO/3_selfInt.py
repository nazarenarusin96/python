#Self engloba

class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarMotorola(self):
        self.marca = "Motorola"

telefono = FabricaTelefonos();
print(telefono.marca);
telefono.ElaborarMotorola();
print(telefono.marca);