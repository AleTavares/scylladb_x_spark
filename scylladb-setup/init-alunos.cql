CREATE KEYSPACE IF NOT EXISTS teste_estudos WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1};

USE teste_estudos;

CREATE TABLE IF NOT EXISTS alunos (
    ra uuid PRIMARY KEY,
    nome text,
    endereco text,
    data_nascimento date,
    data_cadastro timestamp
);