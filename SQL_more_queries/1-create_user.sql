-- creates the MySQL server user user_0d_1
CREATE USER 'user_0d_1'@'localhost' IF NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON MySQL TO 'user_0d_1'@'localhost';