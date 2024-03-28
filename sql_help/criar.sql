CREATE TABLE Alunos (
    matricula INT PRIMARY KEY,
    cpf VARCHAR(14) UNIQUE,
    nomecompleto VARCHAR(255), -- Aumentei para 255 caracteres
    telefone VARCHAR(20),
    idcurso VARCHAR(1),
    nomecurso VARCHAR(100),
    datanascimento VARCHAR(10)
);


CREATE TABLE Teste (
    IDconta INT PRIMARY KEY,
    soma INT,
    num1 INT,
    num2 INT -- Ultimo não tem virgula
);
