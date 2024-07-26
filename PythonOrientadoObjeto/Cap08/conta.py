class Conta:

    def __init__(self, titular, numero, saldo, limite):
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depósita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}" .format(self.numero, self.saldo))


    #Em outro arquivo
    from conta import Conta

    conta = Conta("123-4", 'João', 120.0, 1000.0)
    conta.deposita(20.0)
    conta.extrato()

    conta.saca(15)
    conta.extrato()


