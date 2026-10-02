class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial=0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self._saldo = 0.0
        self.saldo = saldo_inicial  # Usa el setter para validar el saldo inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo = self._saldo + monto
        return self._saldo

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self._saldo = self._saldo - monto
        return self._saldo
    def __str__(self):
        return (
            "Cuenta: " + str(self.numero_cuenta) +
            " | Titular: " + str(self.titular) +
            " | Saldo: S/ " + str(round(self._saldo, 2))
        )


if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Juan Perez", "191-12345678-0-01", 500.0)
    print(cuenta1)

    cuenta1.depositar(200.0)
    print("Despues del deposito:", cuenta1)

    cuenta1.retirar(150.0)
    print("Despues del retiro:", cuenta1)

    # Prueba de error al retirar más de lo permitido
    try:
        cuenta1.retirar(1000.0)
    except ValueError as error:
        print("Error capturado correctamente:", error)