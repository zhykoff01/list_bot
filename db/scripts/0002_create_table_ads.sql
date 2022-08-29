drop table ads;

CREATE TABLE IF NOT EXISTS ads (
   id SERIAL PRIMARY KEY,
   ads_id VARCHAR UNIQUE NOT NULL,
   link VARCHAR,
   title VARCHAR,
   currency VARCHAR,
   price VARCHAR,
   rental_period VARCHAR,
   about VARCHAR,
   category VARCHAR
);