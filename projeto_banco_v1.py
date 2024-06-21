menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Digite a opção desejada: '''


saldo = 0
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)    

    if opcao == 'd':
        deposito = int(input('Digite o valor do Depósito: '))
        saldo += deposito

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print(f'Está opção esta indisponível. LIMITE DE {LIMITE_SAQUES} SAQUES EXCEDIDOS!')
            break
        saque = int(input('Digite o valor do Saque: '))

        if saque > saldo:
            print(f"<<<<<< Saldo Insuficiente!!! Seu saldo atual é R$ {saldo}")

        else:    
            saldo -= saque
            numero_saques += 1

    elif opcao == 'e':
        if numero_saques == 0:
            saque = 0
        
            print(f'Extrato: Depósitos   R$ {deposito:.2f}')
            print(f'         Saque       R$ {saque:.2f}')
            print(f'         Saldo Atual R$ {saldo:.2f}')

        else:
            
            print(f'Extrato: Depósitos   R$ {deposito:.2f}')
            print(f'         Saque       R$ {saque:.2f}')
            print(f'         Saldo Atual R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print(' Operação inválida. Digite a opção desejada.')

