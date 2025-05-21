FROM scylladb/scylla

# Copia o script de inicialização para dentro do container
COPY init-alunos.cql /docker-entrypoint-initdb.d/

CMD ["--reactor-backend=epoll"]