menu = """
    [d] Depositar
    [s] Sacar 
    [e] Extrato
    [q] Sair
    
=> """

saldo = 0
limite = 500
extrato = []  
numeros_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato.append(("Depósito", valor))
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "s":
        if numeros_saque < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato.append(("Saque", valor))
                numeros_saque += 1
                print(f"Saque de R${valor:.2f} realizado.")
            else:
                print("Valor de saque inválido.")
        else:
            print("Limite máximo de saques atingido.")
    
    elif opcao == "e":
        print("Extrato:")
        print("Saldo:", saldo)
        for transacao in extrato:
            tipo, valor = transacao
            if tipo == "Depósito":
                print(f"Depósito: R${valor:.2f}")
            else:
                print(f"Saque: R${valor:.2f}")
    
    elif opcao == "q":
        print("Saindo do sistema.")
        break
    
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
