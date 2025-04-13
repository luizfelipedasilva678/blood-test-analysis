CREATE DATABASE IF NOT EXISTS app;

USE app;

CREATE TABLE IF NOT EXISTS user(
  id int not null auto_increment,
  username varchar(128) not null unique,
  password varchar(128) not null,
  constraint user_pk PRIMARY KEY (id)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS analysis(
  id int not null auto_increment,
  title varchar(128) not null,
  details longtext not null,
  user_id int not null,
  constraint analysis_pk PRIMARY KEY (id),
  constraint analysis_user_fk FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=INNODB;