INSERT INTO mercado_financeiro.selic_mensal 
( data_referencia, taxa_percentual)
VALUES
('2025-01-01', 1.01) ON CONFLICT (data_referencia) DO NOTHING;