class Vehiculo:
    contador_vehiculo = 0       #Atributo de clase

    #CONSTRUCTOR
    def __init__(self, param_marca, param_modelo, param_estado): #self puede aparecer como "this" en otros lenguajes
        #PUBLICO
        self.marca = param_marca     
        #PUBLICO 
        self.modelo = param_modelo
        #PROTEGIDO acceder/modificar en la propia clase, o en una clase hija.   
        self._estado = param_estado
        #PRIVADO - acceder/modificar solo en la propia clase
        #No se usan parametros, por que se supone que si es privado, no deberia poder pasarse ese parametro. Se usan trucos   
        self.__id_vehiculo = Vehiculo.contador_vehiculo + 1 

        Vehiculo.contador_vehiculo +=1

    def __str__(self): #dunder metod que cambia como se imprime el objeto. 
        return f"Soy un Vehiculo marca: {self.marca}, modelo: {self.modelo}, en {self._estado} estado, con id: {self.__id_vehiculo}"

    @property #Decorador para no tener que agregar parentesis al usar el metodo. Normalmente usado para getters o setters
    def get_estado(self):
        return self._estado
    
    def set_estado(self, param_nuevo_estado):
        self._estado = param_nuevo_estado

    def get_id_vehiculo(self):
        return self.__id_vehiculo
    
    @classmethod  #Decorador para metodos de clase
    def get_contador_vehiculo(cls):
        return cls.contador_vehiculo
    
    @staticmethod #Decorador para Metodos que no depende ni de la clase, ni de la instancia
    def calcular_costo_reparacion(hs_trabajo, hs_por_hora):
        return hs_trabajo * hs_por_hora
    

    
    



### ESTO YA ES PUBLICO ###
camion = Vehiculo("Mercedes", "1114", "Bueno")
cuatri = Vehiculo("Honda", "x", "Espectacular")
auto = Vehiculo("Toyota", "Corolla", "Espectacular")

#print(camion.marca)
#print(camion.modelo)
#print(camion._estado)              #NO ES CORRECTO
print(camion.get_estado)          #ES CORRECTO#

##camion._estado = "Impecable"       #NO ES CORRECTO
##camion.set_estado("Impecable")     #ES CORRECTO
#print(camion.get_estado())         #ES CORRECTO

#print(camion._Vehiculo__id_vehiculo)    #NO ES CORRECTO/SE USA PARA DEBUGING (se agrega "_(nombre de la clase)" adelante del atributo privado)    
#print(camion.get_id_vehiculo())          #ES CORRECTO
#print(camion.get_contador_vehiculo())
#print(cuatri.get_id_vehiculo())          #ES CORRECTO
#print(cuatri.get_contador_vehiculo())    #ES CORRECTO

print(camion)