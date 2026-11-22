-- PROJETO: Análise do Mercado Financeiro
-- RELATÓRIO: Selic acumulada mensal em 2025
-- FONTE: Banco Central do Brasil - SGS 4390

-- 1. Indicadores gerais
SELECT
    COUNT(*) AS total_meses,
    ROUND(AVG(taxa_percentual), 2) AS media_mensal,
    MIN(taxa_percentual) AS menor_taxa,
    MAX(taxa_percentual) AS maior_taxa
FROM mercado_financeiro.selic_mensal;


-- 2. Meses com Selic mensal acima da média
SELECT
    data_referencia,
    taxa_percentual
FROM mercado_financeiro.selic_mensal
WHERE taxa_percentual > (
    SELECT AVG(taxa_percentual)
    FROM mercado_financeiro.selic_mensal
)
ORDER BY taxa_percentual DESC, data_referencia;


-- 3. Variação mensal em pontos percentuais
SELECT
    data_referencia,
    taxa_percentual,
    taxa_percentual - LAG(taxa_percentual)
        OVER (ORDER BY data_referencia) AS variacao_pp
FROM mercado_financeiro.selic_mensal
ORDER BY data_referencia;