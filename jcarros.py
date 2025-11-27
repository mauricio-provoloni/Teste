cliente = {
"nome": input("Digite seu nome: "),
"email": input("Digit seu e-mail: "),
"saldo": float(input("Digite seu saldo inicial (R$): "))
}


tabela_precos = {

    "Jeep Compass Longitude": 50900,
    "Renault Kwid": 70000,
    "Fiat Mobi": 60700,
    "Kia Sportage LX Automático": 79900,
    "Honda HR-V EX Automático": 88900,
}


carros_para_alugar = [
  ("Jeep Compass Longitude","Jeep"),
    ("Renault Kwid","Renault"),
    ("Fiat Mobi","Fiat"),
    ("Kia Sportage LX Automatico","Kia"),
    ("Honda HR-V EX Automático","Honda"),
]

carros_para_venda = [
  

 ("Jeep Compass Longitude","Jeep"),
    ("Renault Kwid","Renault"),
    ("Fiat Mobi","Fiat"),
    ("Kia Sportage LX Automatico","Kia"),
    ("Honda HR-V EX Automático","Honda"),

]


def menu():
   print("\n===== CONSECIONARIA =====")
   print("1 - vende de carro")
   print("2 - alugar o carro")
   print("3 - comprar de carro")
   print("4 - var saldo")
   print("0 - sair")

def vender_carro():
    print("\n--- VENDA DE CARRO ---")

    carro = input("Digite o nome exato do carro: ")
    marca = input("digite o nome da marca do carro: ")

    if carro not in tabela_precos:
        print("Este carro não está na lista de preços.")
        return
    
    valor_ref = tabela_precos[carro]
    proposta = valor_ref * 0.80

    print(f"\nValor de referencia: R$ {valor_ref:.2f}")
    print(f"proposta da consecionaria: R$ {proposta:.2f}")
     
    if input("Deseja vender o carro? (s/n):").lower() == "s":
       cliente["saldo"] += proposta
       carros_para_venda.append((carro,marca))
       print("carro vendido com sucesso!")
    
    else:
         print("venda cancelada.")


def alugar_carro():
    print("\n--- ALUGUEL DE CARROS ---")

    if not carros_para_alugar:
            print("Nenhum carro disponível para aluguel. ")
            return
    
    print("\ncarros disponiveis:")
    for i, carro in enumerate(carros_para_alugar):
            print(f"{i + 1} - {carro}")

    escolha = int(input("Escolha o número do carro: ")) - 1

    if escolha < 0 or escolha >= len(carros_para_alugar):
        print("Opção inválida.")
        return
            
    dias = int(input("por quantos dias deseja alugar? "))
    valor_total = dias * 50

    print(f"Valor total da aluguel: R$ {valor_total:.2f}")

    if cliente["saldo"] < valor_total:
       print("Saldo insuficiente.")
       return
            
    if input("confirmar aluguel? (s/n): ").lower() == "s":
        cliente["saldo"] -= valor_total
        carro = carros_para_alugar.pop(escolha)

        print(f"Voce alugou '{carro}")
    else:
        print("Aluguel cancelado.")


def compra_carro():
    print("\n----- COMPRA DE CARROS -----")

    if not tabela_precos:
        print("nao demos este carro nalista de vendas.")
        return
                    
    print("\ncarros a venda:")
    for i, carro in enumerate(carros_para_venda):
        print(f"{i + 1} - ({carro})")

    escolha = int(input("Escolha o numero do carro: ")) - 1

    if escolha < 0 or escolha >= len(carros_para_venda):
        print("opçao invalida.")
        return
                        
    carro = carros_para_venda[escolha][0]
    valor_base = tabela_precos[carro]
    valor_final = valor_base * 1.15

    print(f"Valor do carro: R$ {valor_final:.2f}")

    if cliente["saldo"] < valor_final:
        print("Saldo insuficiente.")
        return
                        
    if input("Confirmar compra? (s/n): ").lower() == "s":

        cliente["saldo"] -= valor_final
        carros = carros_para_venda.pop(escolha)
        print(f"voce comprou'{carros}'.")
    else:
        print("compra cancelada.")

def new_func(compra_carro):
    compra_carro()

while True:
    menu()                    
    opcao = input("escolha uma opção: ")

    match opcao:
        case "1":
         vender_carro()
        case "2": 
          alugar_carro()
        case "3":
         compra_carro()
        case "4":
            print(f"\nSaldo atual: R$ {cliente['saldo']:.2f}")
        case "0":
            print("saindo do sastema. ate logo!")
            break
        case _:
            print("Opção invalida. tente navamente.")
