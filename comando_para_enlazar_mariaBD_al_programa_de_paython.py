-- 1. Entrar a MariaDB como administrador
sudo mysql -u root -p -h localhost

-- 2. Crear la base de datos que usa tu script
create database mds;
use mds;

-- 3. Crear el usuario 'admin' con su contraseña '1234'
create user 'admin'@'localhost' identified by '1234';
grant all privileges on mds.* to 'admin'@'localhost';
flush privileges;

-- 4. Crear la tabla 'DatosH' con las columnas para temperatura y humedad
create table DatosH (temp varchar(20), humed varchar(20));

-- 5. Verificar que la tabla se creó bien y salir
show tables;
exit;
