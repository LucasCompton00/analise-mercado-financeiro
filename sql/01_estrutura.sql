CREATE SCHEMA IF NOT EXISTS mercado_financeiro;
CREATE TABLE IF NOT EXISTS mercado_financeiro.selic_mensal (
    data_referencia DATE PRIMARY KEY,
    taxa_percentual NUMERIC(6,4) NOT NULL
);