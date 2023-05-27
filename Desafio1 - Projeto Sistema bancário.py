menu = '''
     ### Menu ###     
[s] - Saque
[d] - Deposito
[e] - Extrato
[q] - Sair
'''
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
movimento = []

while True:

    opcao = input(menu)

    if opcao == 'd':                                                      #DEPOSITO
        print ('Depósito')
        deposito = float(input('Insira o valor de depósito desejado: '))

        if deposito > 0:                                                  #DEPOSITO REALIZADO
            saldo += deposito
            movimento.append('+' + str(deposito))
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:                                                             #VALOR DO DEPOSITO INVÁLIDO
            print('Valor inválido!')

    elif opcao == 's':                                                   #SAQUE
        print ('Saque')

        if LIMITE_SAQUES == 0:                                            #LIMITE SAQUE DIARIO ATINGIDO
            print('Limite de saque diário atingido!!!')
                
        else:                                                             #SAQUE DIARIO DISPONÍVEL
            saque = float(input('Insira o valor de saque desejado: '))
            if saque > 500:                                               #LIMITE VALOR DO SAQUE
                print('Saque superior ao valor permitido!')        
            
            elif saque > saldo:                                           #SAQUE MAIOR QUE SALDO
                print('Saldo insuficiente para saque, valor superior ao saldo atual!')

            elif saque > 0:
                saldo -= saque                                          #SAQUE REALIZADO
                movimento.append('-' + str(saque))
                print(f'Saque realizado no valor R$ {saque:.2f}')
                print(f'Saldo atual: R$ {saldo:.2f}')
                LIMITE_SAQUES -= 1
            
            else:
                print('Valor inválido para saque!')
    
    elif opcao == 'e':                                                   #EXTRATO
        print('Extrato')
        if saldo != 0:                                                   #EXTRATO DO MOVIMENTO DA CONTA
            print("\n".join(list(movimento)))
            print(f'Saldo final: R$ {saldo:.2f}')

        else:                                                            #CONTA NÃO MOVIMENTADA
            print('Não foram realizadas movimentações')

    elif opcao == 'q':
        print()
        print(' Obrigado, volte sempre! '.center(35,'*'))
        break
        

    else:
        print ('Opção inválida, por favor, selecione novamente a opção desejada')
