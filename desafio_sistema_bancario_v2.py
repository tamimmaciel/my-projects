
def menu():
    menu = '''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Novo Usuário
    [6] Listar Contas
    [0] Sair

    '''
    return input(menu)

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITES_SAQUES):
    if valor <= saldo:
        if numero_saques < LIMITES_SAQUES:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! Limite de valor por saque atingido!")
        else:
            print("Operação falhou! Limite de saque diário atingido!")
    else:
        print("Operação falhou! Saldo insuficiente!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("Extrato".center(100, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Seu saldo: R$ {saldo:.2f}")
    print("=".center(100, "="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (Longradouro, Nº - Bairro - Cidade/Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, por favor realizar o cadastro!")

def listar_contas(contas):
    for conta in contas:
        lista = f'''
        Nome: {conta["usuario"]["nome"]}
        Agência: {conta["agencia"]}
        C/C: {conta["numero_conta"]}
        '''
        print(lista)

def main():
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "1":
            print("Depósito".center(50, "-"))
            print()
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            print("Sacar".center(50, "-"))
            print()
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITES_SAQUES=LIMITES_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            print("Lista de contas corrente".center(100, "="))
            listar_contas(contas)

        elif opcao == "0":
            print("Obrigado por utilizar nosso sistema!\n")
            break

        else:
            print("Operação inválida, por favor selecionar novamente a operação desejada.")

main()
