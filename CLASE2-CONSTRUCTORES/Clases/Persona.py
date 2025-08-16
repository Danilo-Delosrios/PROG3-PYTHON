class Persona:
    #constructor de la clase
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    #metodo get
    @property
    def nombre(self):
        return self._nombre
    
    #metodo get
    @property
    def apellido(self):
        return self._apellido
    
    #metodo set
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    #metodo set
    @nombre.setter
    def apellido(self,nuevo_apellido):
        self._apellido = nuevo_apellido
