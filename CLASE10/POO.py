class Vehiculo:
    #CONSTRUCTOR
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    #METODO
    def mostrar_info(self):
        return f"\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}"
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, num_puertas):
        super().__init__(marca, modelo, color)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        return f"{super().mostrar_info()} \nPuertas: {self.num_puertas}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        return f"{super().mostrar_info()} \nCilindradas: {self.cilindrada}"
    

#auto = Vehiculo("Jeep", "Compass", "Blanco")
auto = Auto("Jeep", "Compass", "Blanco", 5)
moto = Moto("Kawa", "Ninja", "Verde", 1500)
camion = Vehiculo("Mercedes", "1114", "Azul")

#print(auto)
print(auto.mostrar_info())
print(moto.mostrar_info())
print(camion.mostrar_info())

