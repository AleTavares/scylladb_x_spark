# Configuração do Apache Spark com Docker

Este diretório contém a configuração necessária para executar o Apache Spark em um ambiente Docker, além de scripts para integração com o ScyllaDB e exportação de dados.

## Estrutura do Diretório

```
spark/
├── Dockerfile
├── entrypoint.sh
├── dados/
├── jobs/
│   ├── exportscylla.py
├── spark-logs/
```

### Descrição dos Arquivos

- **`Dockerfile`**: Arquivo de configuração para construir a imagem Docker do Spark.
- **`entrypoint.sh`**: Script de inicialização para configurar o Spark Master e Worker.
- **`dados/`**: Diretório para armazenar dados utilizados ou gerados pelas tarefas Spark.
- **`jobs/`**: Diretório contendo scripts PySpark, como o `exportscylla.py` e outros scripts de tarefas.
- **`spark-logs/`**: Diretório para armazenar os logs do Spark.

## Pré-requisitos

- Docker e Docker Compose instalados no sistema.
- O ScyllaDB deve estar em execução e acessível na rede Docker.

## Configuração do Ambiente

1. **Construa e inicie os contêineres do Spark:**
   ```bash
   docker compose up -d --build
   ```

2. **Verifique se os contêineres estão em execução:**
   ```bash
   docker ps
   ```

## Executando o Script `exportscylla.py`

O script `exportscylla.py` conecta ao ScyllaDB, lê os dados das tabelas configuradas no dicionário do script (por exemplo, `alunos` no keyspace `teste_estudos`), filtra apenas os registros dos últimos dois anos (com base em um campo de data específico para cada tabela) e exporta os dados para arquivos Parquet particionados.

1. **Execute o script no Spark Master:**
   ```bash
   docker exec spark-master spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.3.0 ./jobs/exportscylla.py
   ```

2. **Verifique os arquivos Parquet gerados:**
   Os arquivos serão salvos no diretório `dados/` em subpastas para cada tabela.

## Executando Outras Tarefas no Spark

Para executar outros scripts PySpark presentes em `jobs/`, utilize:

```bash
docker exec spark-master spark-submit --deploy-mode client ./jobs/projeto1-tarefa1.py
docker exec spark-master spark-submit --deploy-mode client ./jobs/projeto1-tarefa2.py
# ... e assim por diante
```

## Logs e Depuração

- Para verificar os logs do Spark Master:
  ```bash
  docker logs spark-master
  ```

- Para verificar os logs do Spark Worker:
  ```bash
  docker logs spark-worker
  ```

## Informações Adicionais

- Certifique-se de que o conector do Cassandra para Spark está configurado corretamente no comando `spark-submit`.
- Para mais informações sobre o Apache Spark, consulte a [documentação oficial](https://spark.apache.org/docs/latest/).