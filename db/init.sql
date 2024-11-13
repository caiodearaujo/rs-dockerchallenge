-- Criação do banco de dados com o charset utf8mb4 e collation utf8mb4_general_ci
CREATE DATABASE IF NOT EXISTS `rs_challenge`
    CHARACTER SET 'utf8'
    COLLATE 'utf8_general_ci';

-- Seleciona o banco de dados
USE `rs_challenge`;

-- Criação da tabela app_logs com o collation utf8mb4_general_ci
CREATE TABLE IF NOT EXISTS app_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    level VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
