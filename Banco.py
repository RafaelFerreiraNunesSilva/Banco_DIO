class ContaBancaria:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.num_saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor and self.num_saques_diarios < 3 and valor <= 500:
            self.saldo -= valor
            self.extrato.append(f'Saque: R$ {valor:.2f}')
            self.num_saques_diarios += 1
        else:
            print("Não foi possível realizar o saque.")

    def ver_extrato(self):
        if len(self.extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in self.extrato:
                print(movimentacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria("João")

while True:
    print("Selecione a operação:")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver Extrato")
    print("0 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor_saque)
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor_deposito)
    elif opcao == "3":
        conta.ver_extrato()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite um número válido.")

    print()  # Linha em branco para separar as operações
