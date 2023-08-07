menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[0] Sair

'''

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":
    print("Depósito".center(50,"-"))
    print()
    valor = float(input("Informe o valor do depósito: R$ "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R${valor: .2f}\n"
      print(f"Deposito R${valor: .2f} realizado com sucesso!")
    else:
      print("Operação falhou! O valor informado é inválido.")


  elif opcao == "2":
    print("Sacar".center(50,"-"))
    print()
    saque = float(input("Informe o valor do saque: R$ "))

    if saque <= saldo:

      if numeros_saques < LIMITES_SAQUES:

        if saque <= limite:
          saldo -= saque
          numeros_saques += 1
          extrato += f"Saque: R${saque: .2f}\n"
          print(f"Saque R${saque: .2f} realizado com sucesso!")
        else:
          print("Operação falhou! Limite de valor por saque atingido!")

      else:
        print("Operação falhou! Limite de saque diário atingido!")

    else:
      print("Operação falhou! Saldo insuficiente!")




  elif opcao == "3":
    print("Extrato".center(100,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Seu saldo: R${saldo: .2f}")
    print("=".center(100,"="))

  elif opcao == "4":
    print("Saldo".center(50,"-"))
    print()
    print(f"Seu saldo: R${saldo: .2f}")

  elif opcao == "0":
    print("Obrigado por utilizar nosso sistema!\n")
    break

  else:
    print("Operação inválida, por favor selecionar novamente a operação desejada.")
