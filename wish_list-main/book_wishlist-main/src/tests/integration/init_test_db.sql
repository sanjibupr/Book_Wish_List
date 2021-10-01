
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
