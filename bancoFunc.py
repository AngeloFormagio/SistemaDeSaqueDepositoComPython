def menu():
    escolha = input(
        '''
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [nc] Nova Conta
        [nu] Novo usuario
        [l] listar contas
        '''
    )
    return escolha

def sacar(saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    
    if excedeu_saldo:
        print("Operação falhou! Você nao tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor o saque e maior que o limite")

    elif excedeu_saques:
        print("Operação falhou! Numero maximo de saques diarios excedido")
    elif valor < 0:
            print('insira um valor positivo')
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de {valor:.2f}\n"
            numero_saques += 1
            print(f'Voce realizou um saque de {valor}')
    return saldo, extrato
    


def depositar(saldo,valor,extrato):

    if valor > 0:
        novo_saldo = saldo + valor
        novo_extrato = extrato + f'Deposito no valor de R${valor}\n'
        return novo_saldo,novo_extrato
    else:
        print('insira um valor positivo')


def mostrar_extrato(saldo,extrato):

    print("\n=============EXTRATO===============")
    print("Não Foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================================")

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('JA existe um usuario com esse cpf')
        return
    
    nome = input('seu nome: ')
    data_nascimento = input('data nascimento: ')
    endereco = input('endereço: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('usuario criado com sucesso')

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios,contas):
    cpf = input('Informe o cpf')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
    else: 
        print('usuario nao encontrado encerrando criação de conta')

def listar_contas(contas):
    print(contas)


def main():
    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('insira o valor do deposito'))
            saldo, extrato = depositar(saldo,valor,extrato)
            print('deposito realizado com sucesso')

        if opcao == 's':
            valor = float(input('insira valor do saque'))
            saldo, extrato = sacar(saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES)
            

        if opcao == 'e':
            mostrar_extrato(saldo,extrato)

        if opcao == 'q':
            break
        if opcao == 'nu':
            criar_usuario(usuarios)
        if opcao == 'nc':
            numero_conta = input('insira os numeros da conta')
            criar_conta(AGENCIA, numero_conta, usuarios,contas)
        if opcao == 'l':
            listar_contas(contas)


main()