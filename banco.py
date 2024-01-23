menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0
deposito = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        deposito =  float(input("Informe o valor do depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n" 
            
        else:
            print("Valor inválido!")
    
        
    elif opcao == "s":
        saque =  float(input("Informe o valor do Saque: "))
  
        excedeu_saque = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saque:
            print("Operação falhou.Saldo insuficiente!")
            
        elif excedeu_limite:
            print("Operação falhou.O valor do saque excede o Limite!")
            
        elif excedeu_saques:
            print("Operação falhou.Número máximo de saques excedido!")
            
        elif saldo > 0:
            saldo -= saque
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
        
        

    elif opcao == "e":
        print("====================EXTRATO====================")
        print()
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print()
        print("===============================================")
        
    elif opcao == "x":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
