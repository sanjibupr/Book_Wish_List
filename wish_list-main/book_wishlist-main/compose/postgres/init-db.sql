-- copy from Imhungry

CREATE EXTENSION dblink;
CREATE EXTENSION "uuid-ossp";

DO
$body$
BEGIN
  IF NOT EXISTS (
      SELECT *
      FROM   pg_catalog.pg_user
      WHERE  usename = 'admin') THEN

    CREATE ROLE zonar_test_admin LOGIN PASSWORD 'password_wow';
  END IF;
END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'zonar') THEN
    RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE zonar');
  END IF;
END
$body$;

DO
$body$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'zonar_test') THEN
      RAISE NOTICE 'Database already exists';
    ELSE
      PERFORM dblink_exec('dbname=' || current_database()
                          , 'CREATE DATABASE zonar_test');
    END IF;
  END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'zonar_bind') THEN RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE zonar_bind');
  END IF;
END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'zonar_mat_bind') THEN RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE zonar_mat_bind');
  END IF;
END
$body$;

\connect zonar;

CREATE EXTENSION postgis;

\connect zonar_bind;

CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION postgis;

\connect zonar_mat_bind;
CREATE EXTENSION postgis;

grant all on all tables in schema public to zonar_test_admin;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO zonar_test_admin;

\connect zonar;

CREATE TABLE wl_user (
  user_id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password TEXT,
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


CREATE TABLE book (
  isbn TEXT PRIMARY KEY,
  title TEXT,
  author TEXT,
  date_of_publication DATE,
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


CREATE TABLE wish_list (
  id SERIAL  PRIMARY KEY,
  user_id INT REFERENCES wl_user (user_id),
  isbn TEXT REFERENCES book (isbn),
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


INSERT INTO wl_user (first_name, last_name, email) VALUES
('John', 'Doe', 'johndoe@gmail.com'),
('Mary', 'Jane', 'mary@gmail.com'),
('Peter', 'Parker', 'peter@gmail.com'),
('Dan', 'Jones', 'dan@gmail.com'),
('Daniel', 'Wood', 'wood@gmail.com'),
('Lane', 'Hart', 'lane@gmail.com');


INSERT INTO book (isbn, title, author, date_of_publication) VALUES
('123-123', 'Shuggie Bain','Douglas Stuart', '2021-01-01' ),
('123-234', 'The Vanishing Half','Brit Bennett', '2021-02-01' ),
('123-235', 'The Invisible Life of Addie LaRue','V.E. Schwab', '2021-03-01' ),
('123-543', 'American Dirt','Jeanine Cummins', '2021-04-01' ),
('121-543', 'The Ballad of Songbirds and Snakes','Suzanne Collins', '2021-05-01' ),
('121-513', 'The Guest List','Lucy Foley', '2021-06-01' )
;


INSERT INTO wish_list (user_id, isbn) VALUES
(2, '123-123'),
(2, '123-234'),
(2, '123-235'),
(3, '123-123'),
(3, '121-543'),
(3, '121-513');
