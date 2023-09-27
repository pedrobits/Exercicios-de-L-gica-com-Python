print('===== SCRIPT DE CHECKOUT COM DESCONTO DE PEDRO PAULO DE LIMA =====\n'
      'Bem-vindo! Use o script para calcular valores com desconto.')

# Criando a função que será responsavel por verificar e aplicar descontos
def AplicarDesconto(valor):
    if valor < 1000:
        # Não há desconto
        return valor
    elif 1000 <= valor < 3000:
        # Aplica um desconto de 3%
        return valor - (0.03 * valor)
    elif 3000 <= valor < 5000:
        # Aplica um desconto de 5%
        return valor - (0.05 * valor)
    elif 5000 >= valor:
        # Aplica um desconto de 5%
        return valor - (0.08 * valor)


# Criando um Loop para validar se o valor inserido está correto
while True:
    # Aqui ele vai tentar receber e confirmar o valor, estou usando um try para pegar qualquer valor que não seja valido
    try:
        print('Utilize o padrão "00.0" ao informar o valor unitário do produto')
        valorProduto = float(input('Por favor, insira o valor do produto: R$'))
        confirmação = input(
            f'O valor do produto informado foi de: R$ {valorProduto}, tem certeza do valor? (s/n): ').strip().lower()

        # Verificando se os valores que o cliente colocou estão corretos
        if confirmação == 's':
            # Caso seja um sim, ele vai quebrar o loop
            break
        elif confirmação == 'n':
            # Caso seja um não, ele vai continuar o loop, dando a opção de colocar um novo valor
            continue
        else:
            # Caso a pessoa responda algo diferente do esperado, simplesmente reiniciar o loop
            print('Por favor, responda com "s" ou "n." (Sim ou Não)')
    # Aqui é onde a exceção será capturada, invalidando o input e solicitando outro
    except ValueError:
        print('O valor inserido não é válido. Por favor, insira um valor numérico válido.')
        
quantidadeProdutos = int(input('Qual a quantidade deste produto: '))

valorFinalProdutos = valorProduto * quantidadeProdutos

# Definindo um valor padrão para ValorComARegraDeDesconto
ValorComARegraDeDesconto = valorFinalProdutos


# Chama a função para aplicar o desconto
ValorComARegraDeDesconto = AplicarDesconto(ValorComARegraDeDesconto)

# Output sem desconto, Formatando o valor final com até duas casas decimais
print(f'Valor sem desconto: R$ {valorFinalProdutos:.2f}')

# Output com desconto, Formatando o valor final com até duas casas decimais
print(f'Valor com desconto: R$ {ValorComARegraDeDesconto:.2f}')
