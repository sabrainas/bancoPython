saldo = 0.0
LIMITE_SALDO = 500.00
LIMITE_SAQUE = 3
contador_saque = 0

while True:
    print("=========================")
    print("Movimentação Bancária")
    print("=========================")
    print("1 - Realizar um depósito")
    print("2 - Realizar um saque")
    print("3 - Ver extrato bancário")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "0":
        print("Saindo do sistema...")
        break

    nome = input("Insira o seu nome: ")

    def deposito(valor: float):
        global saldo 
        saldo += valor 
        print(f'Valor Final R${saldo}')

    def saque(valor: float):
        global saldo, contador_saque
        if contador_saque >= LIMITE_SAQUE:
            print("Limite de saques diários atingido.")
        elif valor > LIMITE_SALDO:
            print(f"O limite por saque é de R${LIMITE_SALDO}.")
        elif valor > saldo:
            print("Não é possível realizar o saque. Saldo insuficiente.")
        else:
            saldo -= valor
            contador_saque += 1
            print(f'Saque realizado. Saldo Final: R${saldo}')
            print(f'Saques restantes para hoje: {LIMITE_SAQUE - contador_saque}')
        

    def extrato():
        print("=========================")
        print(f'Titular: {nome}')
        print(f'Saldo R${saldo}')
        print("=========================")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif opcao == "3":
        extrato()
    else:
        print("Opção inválida, tente novamente.")