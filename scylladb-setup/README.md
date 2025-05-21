# Configuração do ScyllaDB

Este projeto fornece uma configuração Docker para executar uma instância do ScyllaDB já preparada com a tabela `alunos`, incluindo os campos RA, nome, endereço, data de nascimento e data de cadastro.

## Estrutura do Projeto

```
scylladb-setup
├── Dockerfile
├── init-alunos.cql
└── README.md
```

## Dockerfile

O `Dockerfile` utiliza a imagem oficial do ScyllaDB, copia o script de criação da tabela para dentro do container e executa o ScyllaDB com a opção `--reactor-backend=epoll`.

## Script de Inicialização

O arquivo `init-alunos.cql` contém:

```sql
CREATE KEYSPACE IF NOT EXISTS teste_estudos WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor':1};

USE teste_estudos;

CREATE TABLE IF NOT EXISTS alunos (
    ra uuid PRIMARY KEY,
    nome text,
    endereco text,
    data_nascimento date,
    data_cadastro timestamp
);
```

## Construindo a Imagem Docker

Navegue até o diretório do projeto e execute:

```bash
docker build -t my-scylla-image .
```

## Executando o Contêiner Docker

Após construir a imagem, execute:

```bash
docker run --name some-scylla -d my-scylla-image --reactor-backend=epoll
```

## Acessando o ScyllaDB

Para acessar a instância do ScyllaDB:

```bash
docker exec -it some-scylla cqlsh
```

## Inserindo Registros de Exemplo

Exemplo de inserção de registros na tabela `alunos`:

```sql
INSERT INTO alunos (ra, nome, endereco, data_nascimento, data_cadastro) VALUES (uuid(), 'João Silva', 'Rua A, 123', '2000-01-01', toTimestamp(now()));
INSERT INTO alunos (ra, nome, endereco, data_nascimento, data_cadastro) VALUES (uuid(), 'Maria Oliveira', 'Rua B, 456', '1999-05-12', toTimestamp(now()));
-- Adicione mais registros conforme necessário
```

## Informações Adicionais

Para mais detalhes sobre o ScyllaDB, consulte a [Documentação do ScyllaDB](https://docs.scylladb.com).