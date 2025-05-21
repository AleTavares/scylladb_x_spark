from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, date_sub

# Configuração da SparkSession
spark = SparkSession.builder \
    .appName("ExportarDadosScyllaDB") \
    .config("spark.cassandra.connection.host", "scylla") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

# Nome do Keyspace e dicionário de tabelas com os campos de data para filtro
keyspace = "teste_estudos"
tables = {
    'alunos': 'data_cadastro'
}

# Data limite para os últimos dois anos
data_limite = date_sub(current_date(), 730)  # 730 dias = 2 anos

# Leitura e exportação dos dados do ScyllaDB
for tabela, campo_data in tables.items():
    # Leitura dos dados da tabela
    dfScylla = spark.read.format("org.apache.spark.sql.cassandra") \
        .options(table=tabela, keyspace=keyspace) \
        .load()

    # Filtrar os dados dos últimos dois anos com base no campo especificado
    dfFiltrado = dfScylla.filter(col(campo_data) >= data_limite)

    # Exportar os dados filtrados para um arquivo Parquet
    output_path = f"dados/{tabela}/"
    dfFiltrado.write.parquet(output_path, mode="overwrite")
    print(f"Dados exportados com sucesso para {output_path}")
    
    # Exibir os dados filtrados (opcional)
    dfFiltrado.show()

# Encerrar a SparkSession
spark.stop()