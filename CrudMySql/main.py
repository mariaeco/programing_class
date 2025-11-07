from re import I
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

#funcao de conexão com o banco de dados
def conectar_banco():
    """
    Conecta ao banco de dados MySQL
    """
    try:
        config = {
            'host': os.getenv('DB_HOST'),
            'port': int(os.getenv('DB_PORT')),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }
        connection = mysql.connector.connect(**config)
        print("✅ Conectado ao banco de dados!")
        return connection
    except Error as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        return None

def inserir_cliente(connection, nome, email, telefone):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"  
        values = (nome, email, telefone)
        cursor.execute(query, values)
        connection.commit()
        print(f"✅ Cliente inserido com ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except Error as e:
        print(f"❌ Erro ao inserir cliente: {e}")
        return None




if __name__ == "__main__":
    connection = conectar_banco()
    inserir_cliente(connection, "Puffy Lima", "puffy@email.com", "2132131231")