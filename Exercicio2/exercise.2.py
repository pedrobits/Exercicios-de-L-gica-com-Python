# Função que determina o preço baseado na escolha do pedido
def determinandoPreco(saborEscolhido, tamanhoEscolhido):
    if tamanhoEscolhido == "P" and saborEscolhido == "CP":
        return 10.0
    if tamanhoEscolhido == "M" and saborEscolhido == "CP":
        return 15.0
    if tamanhoEscolhido == "G" and saborEscolhido == "CP":
        return 29.0
    if tamanhoEscolhido == "P" and saborEscolhido == "AC":
        return 12.0
    if tamanhoEscolhido == "M" and saborEscolhido == "AC":
        return 17.0
    if tamanhoEscolhido == "G" and saborEscolhido == "AC":
        return 21.0

# Criando uma função que gera pedidos
def gerarPedido():
    # Criando um loops (while) para escolher o sabor, para evitar que uma escolha invalida passe
    while True:
        saborEscolhido = str(
            input('Qual o sabor que você prefere? (CP ou AC): ')).strip().upper()

        if saborEscolhido != "CP" and saborEscolhido != "AC":
            print("Sabor inválido. Tente novamente")
        else:
            break

    # Criando uma lista de tamanhos
    Tamanhos = ["P", "M", "G"]

    while True:
        tamanhoEscolhido = input(
            'Qual tamanho você prefere? (P | M | G): ').strip().upper()
        # Verificando se o tamanho escolhido está na lista de tamanhos
        if tamanhoEscolhido in Tamanhos:
            print("Tamanho escolhido:", tamanhoEscolhido)
            break
        else:
            print("Tamanho inválido. Tente novamente.")
    return saborEscolhido, tamanhoEscolhido


print('===== Bem vindo a Loja de gelados de PEDRO PAULO DE LIMA =====')

print('===================CARDAPIO======================\n'
      '=============== OPÇÕES GELADAS ==================\n'
      '-- |   Tamanho   | Cupuaçu (CP) | Açai (AC)  | --\n'
      '-------| Pequeno (P) | R$10,0  | R$12,0 | -------\n'
      '-------| Médio   (M) | R$15,0  | R$17,0 | -------\n'
      '-------| Grande  (G) | R$29,0  | R$21,0 | -------\n'
      '================================================='
      )

# Iniciando a lista de pedidos vazia, preparando para guardar os pedidos
listaDePedidos = []

# Aqui começa a estrutura de execução das funções
while True:
    saborEscolhido, tamanhoEscolhido = gerarPedido()

    # Executando e guardando o preço determinado com base nas escolhas do usuario
    precoPedido = determinandoPreco(saborEscolhido, tamanhoEscolhido)

    # Criando um log resumido com as informações do pedido
    resumoPedido = f'Pedido anotado:\n Gelado sabor {saborEscolhido},\n Tamanho {tamanhoEscolhido},\n Valor: R${precoPedido:.2f}'

    # Guardando pedido na lista que criamos vazia na linha 54
    listaDePedidos.append(resumoPedido)
    print(resumoPedido)

    # Verificando se há mais pedidos a serem feitos 
    while True:
        NovoPedido = input(
            'Deseja pedir mais alguma coisa? (S/N): ').strip().upper()

        if NovoPedido == "S" or NovoPedido == "N":
            break
        else:
            print('Por favor, escolha entre sim ou não (S/N).')

    if NovoPedido == "N":
        break

# Caso passe do loop, todos os pedidos serão printados nessa parte
print("Resumo dos pedidos:")
for pedido in listaDePedidos:
    print('+----+')
    print(pedido)
