saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor = float(input("Digite o valor a ser depositado: R$ "))
    saldo += valor
    extrato.append(f"Depósito de R$ {valor:.2f}")

def sacar():
    global saldo, extrato, numero_saques
    if numero_saques < LIMITE_SAQUES:
        valor = float(input("Digite o valor a ser sacado: R$ "))
        if valor <= saldo and valor <= limite:
            saldo -= valor
            extrato.append(f"Saque de R$ {valor:.2f}")
            numero_saques += 1
        else:
            print("Não é possível sacar este valor.")
    else:
        print("Limite diário de saques alcançado.")

def ver_extrato():
    global extrato
    print("\nExtrato:")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

while True:
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    escolha = input("Escolha a opção desejada: ")

    if escolha == '1':
        depositar()
    elif escolha == '2':
        sacar()
    elif escolha == '3':
        ver_extrato()
    elif escolha == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

