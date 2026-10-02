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