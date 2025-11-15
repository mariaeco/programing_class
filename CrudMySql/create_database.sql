CREATE DATABASE store_db;

USE store_db;

CREATE TABLE clientes (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE produtos (
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT DEFAULT 0
);

CREATE TABLE pedidos (
	id_pedido INT AUTO_INCREMENT PRIMARY KEY,
	id_cliente INT NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE itens_pedidos (
	id_item INT AUTO_INCREMENT PRIMARY KEY,
	id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);



