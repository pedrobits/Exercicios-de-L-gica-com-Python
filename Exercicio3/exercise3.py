# Mensagem de boas-vindas
print("Bem vindo a Papelaria Pedro Paulo de Lima")

# Lista de serviços oferecidos
print("Temos diversos serviços, segue nossa lista:\n"
      "• Serviço de Digitalização (DIG)\n"
      "• Serviço de Impressão Colorida (ICO)\n"
      "• Serviço de Impressão Preto e Branco (IBO)\n"
      "• Serviço de Fotocópia (FOT)\n")


def escolha_servico():
    while True:
        # Solicitar ao usuário que escolha um serviço
        servicoEscolhido = str(
            input("Qual serviço você escolhe: ")).strip().upper()

        # Verificar a escolha do usuário e definir o valor do serviço
        if servicoEscolhido == "DIG":
            print("Você escolheu Serviço de Digitalização")
            valorServiço = 1.10
            print(f'O valor por impressão é de R${valorServiço}')
            break
        elif servicoEscolhido == "ICO":
            print("Você escolheu Serviço de Impressão Colorida")
            valorServiço = 1
            print(f'O valor por impressão é de R${valorServiço}')
            break
        elif servicoEscolhido == "IBO":
            print("Você escolheu Serviço de impressão preto e branco")
            valorServiço = 0.40
            print(f'O valor por impressão é de R${valorServiço}')
            break
        elif servicoEscolhido == "FOT":
            print("Você escolheu Serviço de fotocópia")
            valorServiço = 20.0
            print(f'O valor por impressão é de R${valorServiço}')
            break
        else:
            print("Por favor, escolha uma opção de serviço valida")
            continue
    return valorServiço


def num_pagina(valorServiço):
    while True:
        try:
            quantidadePaginas = int(input('Qual a quantidade de páginas? '))

            if quantidadePaginas < 10:
                desconto = 0.00
            elif quantidadePaginas >= 10 and quantidadePaginas <= 100:
                desconto = 0.10
            elif quantidadePaginas >= 100 and quantidadePaginas <= 1000:
                desconto = 0.15
            elif quantidadePaginas >= 1000 and quantidadePaginas <= 10000:
                desconto = 0.20
            else:
                # Exibir mensagem de erro se a quantidade de páginas não estiver dentro dos limites permitidos
                print('Não é permitido pedidos nessa quantidade de páginas.')
                continue

            # Exibir informações sobre o desconto aplicado
            print(
                f'A quantidade de páginas é {quantidadePaginas}, então o desconto é de {int(desconto*100)}%')

            # Calcular o valor total das páginas com desconto
            valorTotalPaginas = valorServiço * quantidadePaginas

            # Retornar o valor total com desconto
            return valorTotalPaginas - (valorTotalPaginas * desconto)
        except ValueError:
            # Tratar exceção se o usuário inserir uma entrada inválida
            print('Escolha uma opção válida')
            continue


def servico_extra():
    valor_servico_extra = 0
    while True:
        print("Temos alguns adicionais:\n"
              "1 - Adicional de encadernação simples\n"
              "2 - Adicional de encadernação de capa dura\n"
              "0 - Nenhum adicional\n")

        try:
            escolha_adicional = int(
                input('Qual a opção você tem interesse: (0 | 1 | 2) '))

            if escolha_adicional == 0:
                print("Opção: Nenhum adicional")
                break
            elif escolha_adicional == 1:
                valor_servico_extra += 10
                print("Adicional de encadernação simples escolhido.")
                break
            elif escolha_adicional == 2:
                valor_servico_extra += 25
                print("Adicional de encadernação de capa dura escolhido.")
                break
            else:
                # Exibir mensagem de erro se a opção não for válida
                print('Por favor, escolha uma opção válida')
        except ValueError:
            # Tratar exceção se o usuário inserir uma entrada inválida
            print('Por favor, escolha uma opção válida')
            continue

    # Retornar o valor total dos serviços extras escolhidos
    return valor_servico_extra


# Obter o valor do serviço escolhido
valorServico = escolha_servico()

# Calcular o valor com desconto com base no número de páginas
valor_com_desconto = num_pagina(valorServico)

# Obter o valor de serviços extras, se houver
valor_servico_extra = servico_extra()

# Calcular o total a pagar
total = valor_com_desconto + valor_servico_extra

# Exibir o valor total
print(f'Total a pagar: R${total:.2f}')
