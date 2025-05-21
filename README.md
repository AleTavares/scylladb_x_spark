# Projeto ScyllaDB e Spark com Docker

Este projeto configura um ambiente Docker para executar o ScyllaDB e o Apache Spark. Permite a execução de tarefas distribuídas no Spark, integração com o banco de dados ScyllaDB e exportação de dados filtrados para arquivos Parquet.

## Estrutura do Projeto

```
projeto/
├── docker-compose.yml
├── scylladb-setup/
│   ├── Dockerfile
│   ├── init-alunos.cql
│   └── README.md
├── spark/
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── dados/
│   ├── jobs/
│   │   ├── exportscylla.py
│   └── spark-logs/
```

## Pré-requisitos

- Docker e Docker Compose instalados no sistema.
- Scripts Python para tarefas Spark localizados no diretório `./spark/jobs`.
- O conector do Cassandra para Spark deve ser referenciado ao executar scripts Spark.

## Configuração do Ambiente

1. **Construa e inicie os contêineres:**
   ```bash
   docker compose up -d --build
   ```

2. **Verifique se os contêineres estão em execução:**
   ```bash
   docker ps
   ```

## Serviços Disponíveis

### ScyllaDB
- Porta exposta: `9042`
- Para acessar o ScyllaDB via `cqlsh`:
  ```bash
  docker exec -it scylla cqlsh
  ```

### Spark Master
- Porta exposta: `9090` (Spark UI)
- Para executar tarefas no Spark Master, use o comando:
  ```bash
  docker exec spark-master spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.3.0 --deploy-mode client <caminho-do-script>
  ```

### Spark Worker
- Conectado automaticamente ao Spark Master.

## Exportação de Dados do ScyllaDB para Parquet

O script `exportscylla.py` realiza a extração dos dados das tabelas do ScyllaDB, filtrando apenas os registros dos últimos dois anos (com base em um campo de data específico para cada tabela) e exportando para arquivos Parquet.

### Exemplo de dicionário de tabelas e campos no script:

```python
tables = {
    'alunos': 'data_cadastro'
}
```

### Execução do script de exportação:

```bash
docker exec spark-master spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.3.0 ./jobs/exportscylla.py
```

Os arquivos Parquet serão gerados em subdiretórios dentro de `/sistemas/spi/extract_scylla/<nome_da_tabela>/`.

## Executando Outras Tarefas no Spark

Os scripts Python para tarefas Spark estão localizados no diretório `./spark/jobs`. Exemplos de execução:

```bash
docker exec spark-master spark-submit --deploy-mode client ./jobs/projeto1-tarefa1.py
docker exec spark-master spark-submit --deploy-mode client ./jobs/projeto1-tarefa2.py
```
Substitua o nome do arquivo para executar outras tarefas.

## Estrutura de Diretórios

- **`scylladb-setup/`**: Configuração do ScyllaDB e scripts de inicialização.
- **`spark/dados/`**: Diretório para armazenar os dados utilizados ou exportados pelas tarefas.
- **`spark/jobs/`**: Scripts Python para as tarefas Spark.
- **`spark/spark-logs/`**: Diretório para armazenar os logs do Spark.

## Logs e Depuração

- Para verificar os logs do ScyllaDB:
  ```bash
  docker logs scylla
  ```

- Para verificar os logs do Spark Master:
  ```bash
  docker logs spark-master
  ```

- Para verificar os logs do Spark Worker:
  ```bash
  docker logs spark-worker
  ```

## Informações Adicionais

Para mais informações sobre o ScyllaDB e o Apache Spark, consulte suas documentações oficiais:
- [Documentação do ScyllaDB](https://docs.scylladb.com)
- [Documentação do Apache Spark](https://spark.apache.org/docs/latest/)