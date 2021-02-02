CREATE TABLE items (
    items_id serial NOT NULL PRIMARY KEY,
    contentType VARCHAR(100),
    title VARCHAR NOT NULL,
    url_page VARCHAR(255),
    url_pdf VARCHAR(255),
    url_doi VARCHAR(255),
    publicationName VARCHAR(255),
    doi VARCHAR UNIQUE NULL,
    publicationDate DATE,
    abstract TEXT
);

CREATE TABLE authors (
    author_id serial NOT NULL PRIMARY KEY,
    author_name VARCHAR
);
-- CREATE TABLE book_authors (
--     items serial,
--     authors serial,
--     CONSTRAINT fk_items
--       FOREIGN KEY(items) 
-- 	    REFERENCES items (id)
-- 	    ON DELETE SET NULL,
--     CONSTRAINT fk_authors
--       FOREIGN KEY(authors) 
-- 	    REFERENCES authors (id)
-- 	    ON DELETE SET NULL
-- );
CREATE TABLE book_authors (

    items_id int REFERENCES items (items_id) ON DELETE SET NULL,

    author_id int REFERENCES authors (author_id) ON UPDATE SET NULL,

    CONSTRAINT nook_author PRIMARY KEY (items_id, author_id)
    
);






