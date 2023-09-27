# Função para cadastrar um livro
def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    
    livro = {"ID": id, "Nome": nome, "Autor": autor, "Editora": editora}
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    opcao = input("Escolha uma opção (1. Consultar Todos / 2. Consultar por ID / 3. Consultar por Autor / 4. Retornar ao menu): ")
    
    if opcao == "1":
        for livro in lista_livro:
            print(f"ID: {livro['ID']}, Nome: {livro['Nome']}, Autor: {livro['Autor']}, Editora: {livro['Editora']}")
    elif opcao == "2":
        id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
        for livro in lista_livro:
            if livro['ID'] == id_consulta:
                print(f"ID: {livro['ID']}, Nome: {livro['Nome']}, Autor: {livro['Autor']}, Editora: {livro['Editora']}")
                break
        else:
            print("Livro não encontrado.")
    elif opcao == "3":
        autor_consulta = input("Digite o nome do autor que deseja consultar: ")
        for livro in lista_livro:
            if livro['Autor'] == autor_consulta:
                print(f"ID: {livro['ID']}, Nome: {livro['Nome']}, Autor: {livro['Autor']}, Editora: {livro['Editora']}")
    elif opcao == "4":
        return
    else:
        print("Opção inválida")

# Função para remover um livro
def remover_livro():
    id_remover = int(input("Digite o ID do livro que deseja remover: "))
    for livro in lista_livro:
        if livro['ID'] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            break
    else:
        print("Livro não encontrado.")

# Variáveis globais
lista_livro = []
id_global = 0

# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Livros do Pedro Paulo de Lima1")

# Loop principal do menu
while True:
    print("\nMenu:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    
    opcao_menu = input("Escolha uma opção: ")
    
    if opcao_menu == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == "2":
        consultar_livro()
    elif opcao_menu == "3":
        remover_livro()
    elif opcao_menu == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida")

# Saída de console
print("\nSaída de Console:")
# Boas-vindas
print("Mensagem de boas-vindas com seu nome: Bem-vindo ao Sistema de Gerenciamento de Livros")

# Cadastro de 3 livros
cadastrar_livro(1)
cadastrar_livro(2)
cadastrar_livro(3)

# Consulta de todos os livros
print("\nConsulta de Todos os Livros:")
consultar_livro()

# Consulta por código de um dos livros
print("\nConsulta por Código de Um dos Livros:")
consultar_livro()

# Consulta por autor (2 livros do mesmo autor)
print("\nConsulta por Autor:")
consultar_livro()

# Remoção de um livro e consulta de todos os livros
print("\nRemoção de Um Livro:")
remover_livro()
print("\nConsulta de Todos os Livros Após Remoção:")
consultar_livro()
