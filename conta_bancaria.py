class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor and len(self.saques) < 3:
                self.saldo -= valor
                self.saques.append(valor)
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            elif self.saldo < valor:
                print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite diário de saques atingido.')
        else:
            print('Valor inválido para saque.')

    def extrato(self):
        print('Extrato bancário:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')


# Teste do código
conta = ContaBancaria()

conta.deposito(1000.50)
conta.saque(200)
conta.deposito(500.75)
conta.saque(700)
conta.saque(300)
conta.saque(100)
conta.extrato()

