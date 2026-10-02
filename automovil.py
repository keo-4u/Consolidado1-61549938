class Automovil:
    def __init__(self, marca, modelo, velocidad_max, nivel_combustible, año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor):
        if valor < 1886 or valor > 2026:
            raise ValueError("El año de fabricacion debe estar entre 1886 y 2026.")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if valor < 0.0 or valor > 100.0:
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0.")
        self._nivel_combustible = valor

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad maxima debe ser mayor a 0.")
        self._velocidad_max = valor