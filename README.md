Práctica Calificada - Consolidado 1
Curso: Construcción de Software (ASUC00947)  
Estudiante: Humberto Zamora Moscoso  
Código de Alumno: 61549938

Descripción del código: Ejercicio 1 (`planeta.py`)
Este programa define y gestiona cuerpos celestes utilizando Programación Orientada a Objetos (POO) en Python.
Funcionamiento paso a paso:
1. Clase `Planeta`: Funciona como una plantilla que recibe los datos de un planeta al instanciarse: `nombre`, `masa` (en kg), `radio` (en metros), `distancia_al_sol` (en Unidades Astronómicas) y un valor booleano opcional `tiene_vida` (por defecto `False`).
2. Método `calcular_densidad()`: Aplica la fórmula física dividiendo la masa del planeta entre su volumen V = (4/3)*pi*r^3 para obtener su densidad media en kg/m^3.
3. Método `es_planeta_exterior()`: Compara la distancia al Sol con el umbral de 5.2 UA y retorna `True` si está más alejado (planetas exteriores/gigantes) o `False` si está más cerca (planetas interiores).
4. Método especial `__str__()`: Formatea automáticamente la información del planeta en un texto legible al momento de ejecutar la función `print()`.
5. Pruebas integradas:Al ejecutar el archivo directamente, se crean dos objetos de prueba (`tierra` y `jupiter`) y se imprimen sus resultados en consola para verificar los cálculos.


Descripción del código: Ejercicio 2 (`automovil.py`)
Este programa gestiona las características y el rendimiento de vehículos aplicando encapsulamiento con `@property` en Python.
Funcionamiento paso a paso:
1. Clase `Automovil`: Define la plantilla para representar vehículos recibiendo `marca`, `modelo`, `velocidad_max`, `nivel_combustible` y `año_fabricacion`.
2. Encapsulamiento con `@property`: Declara atributos privados (`_velocidad_max`, `_nivel_combustible`, `_año_fabricacion`) y utiliza decoradores `@property` para validar que el año esté entre 1886 y 2026, el combustible entre 0.0 y 100.0%, y la velocidad sea mayor a 0 (lanzando `ValueError` si son inválidos).
3. Método `tiempo_llegada(distancia_km)`: Calcula y retorna el tiempo estimado en horas requeridas para recorrer una distancia dividiéndola entre la `velocidad_max`.
4. Método especial `__str__()`: Retorna una cadena con la descripción formateada de la marca, modelo, año, velocidad máxima y porcentaje de combustible disponible.
5. Pruebas integradas: Instancia un objeto de prueba, ejecuta el cálculo de tiempo de llegada y utiliza un bloque `try/except` para demostrar la captura de errores al asignar un año de fabricación inválido.


Descripción del código: Ejercicio 3 (`cuenta_bancaria.py`)
Este programa simula operaciones bancarias básicas aplicando principios de Programación Orientada a Objetos en Python.
Funcionamiento paso a paso:
1. Clase `CuentaBancaria`: Funciona como plantilla para gestionar cuentas almacenando `titular`, `numero_cuenta` y `saldo_inicial`.
2. Encapsulamiento con `@property`: Declara el atributo privado `_saldo` y utiliza decoradores `@property` para validar que ni el saldo inicial ni el asignado sean valores negativos (lanzando `ValueError`).
3. Método `depositar(monto)`: Suma el dinero al saldo actual asegurando previamente que la cantidad a ingresar sea estrictamente mayor a cero.
4. Método `retirar(monto)`: Resta el monto especificado verificando que sea mayor a cero y que existan fondos suficientes disponibles (lanzando `ValueError` por sobregiro).
5. Método especial `__str__()`: Formatea automáticamente la información de la cuenta indicando el número, titular y el saldo disponible en texto legible.
6. Pruebas integradas: Instancia una cuenta de prueba, realiza operaciones exitosas de depósito/retiro y demuestra la captura de excepciones con `try/except` al intentar retirar más fondos de los disponibles.