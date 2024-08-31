from datetime import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.historico = []
        self.saques_diarios = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        hoje = datetime.now().date()
        saques_hoje = [s for s in self.saques_diarios if s['data'] == hoje]

        if len(saques_hoje) >= 3:
            print("Limite diário de 3 saques atingido.")
        elif valor > 500:
            print("Valor do saque excede o limite de R$ 500,00.")
        elif valor > self.saldo:
            print("Saque inválido. Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: -R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            self.saques_diarios.append({'valor': valor, 'data': hoje})
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        print("\nExtrato: ")
        for operacao in self.historico:
            print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


# Exemplo de uso
banco = Banco()
banco.depositar(1000.45)
banco.sacar(300)
banco.sacar(200)
banco.extrato()