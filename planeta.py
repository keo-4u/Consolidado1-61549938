import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2    
    def __str__(self):
        if self.es_planeta_exterior():
            tipo = "Exterior"
        else:
            tipo = "Interior"

        if self.tiene_vida:
            vida = "Si"
        else:
            vida = "No"

        densidad = self.calcular_densidad()

        return (
            f"Planeta: {self.nombre}\n"
            f"  - Densidad media: {densidad:.2f} kg/m3\n"
            f"  - Clasificacion: {tipo}\n"
            f"  - ¿Tiene vida?: {vida}"
        )


if __name__ == "__main__":
    tierra = Planeta("Tierra", 5.972e24, 6371000.0, 1.0, True)
    jupiter = Planeta("Jupiter", 1.898e27, 69911000.0, 5.204, False)

    print("--- INFORMACION DE PLANETAS ---")
    print(tierra)
    print("-" * 30)
    print(jupiter)