CREATE DATABASE kg_express_db;
CREATE USER express_user  WITH PASSWORD 'admin';
ALTER ROLE express_user SET client_encoding TO 'utf-8';
ALTER ROLE express_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE express_user SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE kg_express_db TO express_user;
