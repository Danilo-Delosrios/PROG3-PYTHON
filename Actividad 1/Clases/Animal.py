class animal:
    def __init__(self, nombre, peso, propietario,fecha_cumpleaños, fecha_ultima_vacuna):
        self._nombre = nombre
        self._peso = peso
        self._propietario = propietario
        self._fecha_cumpleaños = fecha_cumpleaños
        self._fecha_ultima_vacuna = fecha_ultima_vacuna

    #metodos get
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def propietario(self):
        return self._propietario
    
    @property
    def fecha_cumpleaños(self):
        return self._fecha_cumpleaños
    
    @property
    def fecha_ultima_vacuna(self):
        return self._fecha_ultima_vacuna
    
    #metodos set
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    @peso.setter
    def peso(self,nuevo_peso):
        self._peso= nuevo_peso

    @propietario.setter
    def propietario(self,nuevo_propietario):
        self._propietario = nuevo_propietario

    @fecha_cumpleaños.setter
    def fecha_cumpleaños(self,nuevo_fecha_cumpleaños):
        self._fecha_cumpleaños = nuevo_fecha_cumpleaños

    @fecha_ultima_vacuna.setter
    def fecha_ultima_vacuna(self,nuevo_fecha_ultima_vacuna):
        self._fecha_ultima_vacuna = nuevo_fecha_ultima_vacuna