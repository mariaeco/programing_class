import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from produtos import inserir_produto, editar_produto, listar_produtos, deletar_produto

load_dotenv() #get database keys


def conectar_banco():
    try:
        config = {
            'host': os.getenv('DB_HOST'),
            'port': int(os.getenv('DB_PORT')),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }
        connection = mysql.connector.connect(**config)
        if connection:
            print("Conectado ao banco de dados!")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None


def menu():
    print("-------------- MEU MENU DE PRODUTOS ----------------")
    print("1. Inserir Produto")
    print("2. Listar Produtos")
    print("3. Editar Produto")
    print("4. Deletar Produto")
    print("0. SAIR")
    option = int(input("Digite uma opção: "))
    return option


def menu_edicao():
    print("-------------- ALTERAR PRODUTO ----------------")
    print("1. Alterar nome")
    print("2. Alterar descrição")
    print("3. Alterar valor")
    print("4. Alterar quantidade no estoque")
    print("0. RETORNAR")
    option = int(input("Digite uma opção: "))
    return option


def processar_edicao(opt):
    id = int(input("Digite o id do produto: "))
    if opt == 1:
        produto = input("Digite o novo nome do produto: ")
        editar_produto(connection, id_produto = id, novo_nome = produto)
    elif opt == 2:
        descricao = input("Digite a nova descrição: ")
        editar_produto(connection, id_produto = id, nova_descricao = descricao)
    elif opt == 3:
        valor = float(input("Digite o novo valor: "))
        editar_produto(connection, id_produto = id, novo_valor = valor)
    elif opt == 4:
        estoque = int(input("Digite a nova quantidade em estoque: "))
        editar_produto(connection, id_produto = id, novo_estoque = estoque)
    elif opt == 0:
        option = menu()
    else:
        print("Opção inválida")




if __name__ == "__main__":
    connection = conectar_banco()

    while True:
        option = menu()

        if option == 1:
            produto = input("Digite o nome do Produto: ")
            descricao = input("Digite a descrição do Produto: ")
            valor = float(input("Digite o valor: ")) #valor é float
            estoque = int(input("Digite a quantidade em estoque: "))  #quantidade é inteira
            inserir_produto(connection, produto, descricao, valor, estoque) 
        elif option == 2:
            listar_produtos(connection)
        elif option == 3:
            os.system("cls")  #limpar tela
            op_edition = menu_edicao()
            processar_edicao(op_edition)
        elif option == 4:
            id = int(input("Digite o id do produto: "))
            deletar_produto(connection, id_produto=id) 
        elif option == 0:
            break
        else:
            print("Opção inválida!")

        input("\n Pressione Enter para contiunar...")
        os.system("cls") #limpar tela



