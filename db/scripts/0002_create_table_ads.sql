drop table ads;

CREATE TABLE IF NOT EXISTS ads (
   id SERIAL PRIMARY KEY,
   ads_id VARCHAR UNIQUE NOT NULL,
   href VARCHAR,
   title VARCHAR,
   cost VARCHAR,
   about VARCHAR,
   category VARCHAR
);