menu = """
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite_por_saque = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3

print("Bem Vindo ao Banco Python")
while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor}\n"
        else:
            print("Operação inválida, valor inserido menor ou igual a zero.")
            
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        
        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite_por_saque:
            print("Limite por saque excedido")
        elif qtd_saques >= LIMITE_SAQUES:
            print("Limite de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor}\n"
            qtd_saques += 1
            
        else:
            print("Operação inválida, valor inserido menor ou igual a zero.")
            
    elif opcao == "e":
        print("\n========== Extrato ==========")
        print(f"Saldo: R${saldo}")
        print(extrato)
        
    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida, selecione uma opção válida.")