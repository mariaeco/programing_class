
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


def inserir_cliente(connection, nome, email, telefone=None):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        valores = (nome, email, telefone)
        
        cursor.execute(query, valores)
        connection.commit()
        
        id_cliente = cursor.lastrowid
        print(f"Cliente inserido com sucesso! ID: {id_cliente}")
        cursor.close()
        return id_cliente
        
    except Error as e:
        print(f"Erro ao inserir cliente: {e}")
        connection.rollback()
        return None


def imprimir_clientes(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        clientes = cursor.fetchall()

        if clientes:
            print(" ========= MEUS CLIENTES ===========")
            for cliente in clientes:
                print("Id:", cliente[0])
                print("Nome:", cliente[1])
                print("E-mail:", cliente[2])
                print("Telefone:", cliente[3])
                print("\n")


    except Error as e:
        print(f"Erro ao imprimir clientes: {e}")
        connection.rollback()
        return None


def editar_cliente(connection, id, novo_nome=None, novo_email=None, novo_telefone=None):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM clientes WHERE id_cliente = %s"
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        
        variaveis = []
        valores = []

        if novo_nome is not None: #se eu tiver inserido um nome
            variaveis.append("nome = %s")
            valores.append(novo_nome)
        if novo_email is not None: #se eu tiver inserido um nome
            variaveis.append("email = %s")
            valores.append(novo_email)
        if novo_telefone is not None: #se eu tiver inserido um nome
            variaveis.append("telefone = %s")
            valores.append(novo_telefone)


        valores.append(id)
        query = f"UPDATE clientes SET  {', '.join(variaveis)} WHERE id_cliente = %s"
        cursor.execute(query, valores)
        connection.commit()


    except Error as e:
        print(f"Erro ao encontrar cliente: {e}")
        connection.rollback()
        return None


def deletar_cliente(connection, id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM clientes WHERE id_cliente = %s"
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        

        query = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(query, (id,))
        connection.commit()
        print("Cliente deletado com sucesso")
        
    except Error as e:
        print(f"Erro ao encontrar cliente: {e}")
        connection.rollback()
        return None
