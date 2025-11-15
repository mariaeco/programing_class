
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

#inserir produto
def inserir_produto(connection, nome, descricao, preco, estoque):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
        values = (nome, descricao, preco, estoque)
        cursor.execute(query, values) 
        connection.commit()
        print(f"Produto inserido com sucesso com ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except Error as e:
        print(f"Erro ao inserir produto: {e}")
        return None

#editar produto
def editar_produto(connection, id_produto, novo_nome=None, nova_descricao=None, novo_valor=None, novo_estoque=None):
    try:
        cursor = connection.cursor()
        query = "SELECT id_produto, nome, descricao, preco, estoque FROM produtos WHERE id_produto = %s" #ACHAR O PRODUTO PELO NOME
        cursor.execute(query, (id_produto,)) 
        variaveis = cursor.fetchone()
        
        campos = []
        valores = []

        if novo_nome is not None:
            campos.append("nome = %s")
            valores.append(novo_nome)

        if nova_descricao is not None:
            campos.append("descricao = %s")
            valores.append(nova_descricao)

        if novo_valor is not None:
            campos.append("preco = %s")
            valores.append(novo_valor)

        if novo_estoque is not None:
            campos.append("estoque = %s")
            valores.append(novo_estoque)

        valores.append(id_produto)
        query = f"UPDATE produtos SET {', '.join(campos)} WHERE id_produto = %s"  
        cursor.execute(query, valores)
        connection.commit()

    except Error as e:
        print(f"Erro ao editar produto: {e}")
        return None


def listar_produtos(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT id_produto, nome, descricao, preco, estoque FROM produtos" #seleciona todos
        cursor.execute(query)
        produtos = cursor.fetchall()

        print(produtos)

        if produtos:
            print("=========== LISTA DE PRODUTOS ============")
            for produto in produtos:
                print(f"Id do produto: {produto[0]}")
                print(f"Nome do produto: {produto[1]}")
                print(f"Descrição do produto: {produto[2]}")
                print(f"Preço do produto: {produto[3]}")
                print(f"Estoque do produto: {produto[4]}")
                print("\n")


    except Error as e:
        print(f"Erro ao listar produto: {e}")
        return None

    
def deletar_produto(connection, id_produto):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM produtos WHERE id_produto = %s"

        cursor.execute(query, (id_produto,))
        connection.commit()

        print("Produto deletado com sucesso!")


    except Error as e:
        print(f"Erro ao deletar produto: {e}")
        return None