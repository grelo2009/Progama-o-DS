-- Criação da tabela Clientes
CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    emailCliente VARCHAR(100)
);

-- Criação da tabela Compras
CREATE TABLE Compras (
    CompraID INT PRIMARY KEY,
    ClienteID INT,
    NomeLivro VARCHAR(200),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);
SELECT * FROM Clientes;
SELECT c.nomeCliente, c.emailCliente
FROM Clientes c
INNER JOIN Compras co ON c.ID = co.ClienteID
WHERE co.NomeLivro = 'Quarto de Despejo';
