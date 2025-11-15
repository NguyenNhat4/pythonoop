CREATE TABLE product_types (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id        SERIAL PRIMARY KEY,
    name      VARCHAR(100) NOT NULL,
    price     INTEGER NOT NULL,
    type_id   INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES product_types(id)
);


INSERT INTO products_type (name)
VALUES
    ('VEGETABLES'),
    ('FRUITS'),
    ('GRAINS_LEGUMES'),
    ('DAIRY_EGGS'),
    ('MEAT_SEAFOOD');

   