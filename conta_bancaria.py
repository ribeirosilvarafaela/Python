class ContaCorrente:
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor, *, saldo, extrato):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            extrato.append(f'Depósito: R$ {valor:.2f}')
            saldo += valor
        else:
            print('Valor inválido para depósito.')

        return saldo, extrato

    def saque(self, valor, *, saldo, extrato, limite=500, numero_saques=0, limite_saques=3):
        if valor > 0:
            if saldo >= valor and numero_saques < limite_saques:
                self.saldo -= valor
                self.saques.append(valor)
                extrato.append(f'Saque: R$ {valor:.2f}')
                saldo -= valor
                numero_saques += 1
            elif saldo < valor:
                print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite diário de saques atingido.')
        else:
            print('Valor inválido para saque.')

        return saldo, extrato

    def extrato(self, *, saldo, extrato):
        print('Extrato bancário:')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f'Saldo atual: R$ {saldo:.2f}')


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def criar_conta(self, agencia, numero):
        conta = ContaCorrente(agencia, numero)
        self.contas.append(conta)

    def desativar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                print(f'A conta {conta.numero} foi desativada.')
                break
        else:
            print(f'A conta {numero} não foi encontrada.')

# Teste do código
#usuario1 = Usuario('João', '01/01/1990', '12345678900', 'Rua A, 123')
#usuario1.criar_conta('001', '12345')
#usuario1.criar_conta('001', '67890')

#saldo = 0
#extrato = []
#saldo, extrato = usuario1.contas[0].deposito(1000.50, saldo=saldo, extrato=extrato)
#saldo, extrato = usuario1.contas[0].saque(200, saldo=saldo, extrato=extrato)
#saldo, extrato = usuario1.contas[0].deposito(500.75, saldo=saldo, extrato=extrato)
#saldo, extrato = usuario1.contas[0].saque(700, saldo=saldo, extrato=extrato)
#saldo, extrato = usuario1.contas[0].saque(300, saldo=saldo, extrato=extrato)


