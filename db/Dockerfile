# Usando a imagem oficial do MySQL
FROM mysql:latest

# Definindo variáveis de ambiente para configuração do MySQL
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=rs_challenge
ENV MYSQL_USER=rs_user
ENV MYSQL_PASSWORD=rs_password

# Copiar o arquivo de inicialização SQL para o diretório de inicialização do MySQL
COPY init.sql /docker-entrypoint-initdb.d/

# Expor a porta padrão do MySQL
EXPOSE 3306
