cBanko = 'DIO Bank '
cSlogan = 'More than a bank, your bank'
menu ='''         Seja bem-vindo ao DIO Bank!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''

cOpcao = 'Início'
nQtd_Lmt_Saq = 3
nVlr_Lmt_Saq = 500.0
nSldo = 1500.0
nVlr_Saq = nVlr_Dpsto = 0
lHstrco_Dpstos = []
lHstrco_Squs = []
lHstrco_Slds = [nSldo]

# Dando início ao menu
while True:
    print('-'*41)
    print(f'{cBanko:^41}'.upper())
    print(f'{cSlogan:^41}')
    print('-'*41)
    cOpcao = str(input(menu)).upper()
    print('-'*41)
    
    if cOpcao == 'S':
        # Lógica de realização do saque
        nVlr_Saq = int(input('Valor do saque: R$ '))
        print()
        
        if nQtd_Lmt_Saq > 0:
            if nVlr_Saq <= nVlr_Lmt_Saq:
                if nVlr_Saq <= nSldo:
                    nQtd_Lmt_Saq -= 1
                    nSldo -= nVlr_Saq
                    print('                SUCESSO!')
                    print(f'       Saque de R$ {nVlr_Saq:.2f} realizado')
                    
                    # Lógica registro no extrato
                    lHstrco_Squs.append(nVlr_Saq)
                       
                else:
                    print('                  ERRO!')
                    print('      Valor indisponível para saque')
            else:
                print('                  ERRO!')
                print('       Valor de saque indisponível')
        else:
            print('                  ERRO!')
            print('        Limite de saques atingido')
        
        print('\nRetornando ao menu...')
        

    elif cOpcao == 'D':
        # Lógica de realização do depósito
        nVlr_Dpsto = int(input('Valor do depósito: R$ '))
        if nVlr_Dpsto > 0:
            nSldo += nVlr_Dpsto
            print('\n                SUCESSO!')
            print(f'      Depósito de R$ {nVlr_Dpsto:.2f} realizado')
        else:
            print('\nValor de depósito inválido')
            
        print('\nRetornando ao menu...')
        
        # Lógica registro no extrato
        lHstrco_Dpstos.append(nVlr_Dpsto)
    
    elif cOpcao == 'E':
        print(f'\n{cBanko:^41}'.upper())
        print(f'{cSlogan:^41}')
        print('-' * 41)
        print('\n            Extrato da conta\n')
        if len(lHstrco_Dpstos) == 0 and len(lHstrco_Squs) == 0:
            print('       Nenhuma operação realizada')
            print('-' * 41)
        else:
            print(f'nSldo inicial: R$ {lHstrco_Slds[0]:.2f}\n')
        if len(lHstrco_Dpstos) > 0:
            print('depósitos'.upper())
            for deposito in lHstrco_Dpstos:
                print(f'R$ {deposito:.2f}')
            print('-' * 41)
        if len(lHstrco_Squs) > 0:
            print('saques'.upper())
            for saque in lHstrco_Squs:
                print(f'R$ {saque:.2f}')
            print('-' * 41)
        print(f'nSldo atual da conta: R$ {nSldo:.2f}')
        print(f'Saques diários restantes: {nQtd_Lmt_Saq}\n')
    
    elif cOpcao == 'Q':
        print('      O DIO Bank agradece a preferência!')
        print()
        break
    
    else:
        print('   Operação inválida. Tente novamente')
        print()
