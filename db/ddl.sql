CREATE DATABASE IF NOT EXISTS app;

USE app;

CREATE TABLE IF NOT EXISTS user(
  id int not null auto_increment,
  username varchar(128) not null unique,
  password varchar(128) not null,
  constraint user_pk PRIMARY KEY (id)
)ENGINE=INNODB;