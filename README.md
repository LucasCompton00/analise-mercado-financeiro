# 📈 Análise do Mercado Financeiro com SQL e Python

### Análise de ativos financeiros e indicadores econômicos utilizando dados históricos reais

## 📌 Sobre o projeto

Este projeto tem como objetivo explorar, organizar e analisar dados históricos do mercado financeiro, utilizando ferramentas de análise de dados para investigar o comportamento de ativos e indicadores econômicos.

A proposta é desenvolver um ambiente de análise que permita compreender a evolução dos preços, comparar rentabilidades, avaliar medidas de risco e identificar padrões históricos por meio de consultas SQL, programação em Python e visualizações.

O projeto será desenvolvido progressivamente, aplicando conceitos de bancos de dados relacionais, estatística descritiva, tratamento de dados e análise exploratória.

Além do aprendizado técnico, busca demonstrar habilidades relevantes para a atuação profissional em Análise de Dados, especialmente no setor financeiro.

## 🎯 Objetivos

**Objetivo principal**

Desenvolver análises fundamentadas em dados financeiros históricos, transformando informações em indicadores e visualizações que facilitem sua interpretação.

**Objetivos específicos**

- Coletar e organizar dados históricos de fontes verificáveis.
- Armazenar e consultar informações financeiras no PostgreSQL.
- Desenvolver consultas SQL para exploração, filtragem e agregação de dados.
- Analisar a evolução histórica de ativos e indicadores econômicos.
- Calcular e comparar rentabilidade e volatilidade.
- Investigar tendências e variações ao longo do tempo.
- Aplicar Python e Pandas no tratamento e na análise de dados.
- Desenvolver dashboards e relatórios analíticos.
- Documentar os métodos utilizados e apresentar conclusões baseadas nos resultados encontrados.

## 💡 Motivação

Meu interesse pelo mercado financeiro começou ainda na adolescência, quando abri minha primeira conta em uma corretora, com a autorização da minha mãe. Desde então, comecei a estudar investimentos, ações e diferentes produtos financeiros, desenvolvendo uma curiosidade crescente pelo funcionamento do mercado e pela relação entre risco e retorno.

A tecnologia também sempre despertou meu interesse. Desde criança, gostava de desmontar objetos para entender como funcionavam e descobrir a lógica por trás deles.

Ao ingressar na faculdade de Análise e Desenvolvimento de Sistemas, encontrei na área de dados uma oportunidade de unir essas duas paixões: tecnologia e mercado financeiro.

Este projeto nasceu dessa combinação. Meu objetivo é utilizar programação, bancos de dados e técnicas de análise para investigar informações financeiras reais, desenvolver meu raciocínio analítico e construir soluções baseadas em evidências.

## 📊 Questões que o projeto pretende investigar

A análise será orientada por perguntas relacionadas ao comportamento histórico de ativos financeiros e indicadores econômicos.

**1. Desempenho dos ativos**

- Como determinados ativos evoluíram ao longo do tempo?
- Quais apresentaram maiores retornos nos períodos analisados?
- Como comparar o desempenho de ativos com características diferentes?

**2. Risco e volatilidade**

- Quais ativos apresentaram maior volatilidade histórica?
- Como a volatilidade variou entre diferentes períodos?
- Quais foram as maiores quedas e altas registradas?

**3. Indicadores econômicos**

- Como evoluíram indicadores como câmbio e taxa Selic?
- Como o comportamento desses indicadores se compara ao desempenho dos ativos analisados?

**4. Visualização e interpretação**

- Quais indicadores ajudam a compreender o comportamento dos ativos?
- Como apresentar os resultados de forma clara para apoiar análises e decisões?

As perguntas poderão ser refinadas de acordo com a disponibilidade e a qualidade dos dados.

## 🛠️ Tecnologias e ferramentas

| Tecnologia | Aplicação no projeto | Situação |
|---|---|---|
| SQL | Consultas, filtros, agrupamentos e análises | Em estudo |
| PostgreSQL | Armazenamento e organização dos dados | Ambiente inicial configurado |
| Python | Tratamento, automação e análise de dados | Planejado |
| Pandas | Manipulação de tabelas e séries temporais | Planejado |
| Estatística descritiva | Cálculo e interpretação de indicadores | Planejado |
| Ferramenta de BI | Construção de dashboards | A definir |
| Git | Controle de versão | Iniciado |
| GitHub | Documentação e publicação do projeto | Publicação pendente |
| VS Code | Ambiente de desenvolvimento | Em uso |

## 🗂️ Organização do projeto

A estrutura inicial do repositório é:

```text
analise-mercado-financeiro/
├── README.md
├── .gitignore
├── sql/
├── dados/
├── notebooks/
├── dashboards/
└── docs/
```

**Descrição dos diretórios**

- `sql/`: consultas e scripts SQL utilizados nas análises.
- `dados/`: arquivos de dados necessários ao desenvolvimento local.
- `notebooks/`: análises e experimentos com Python e Pandas.
- `dashboards/`: arquivos e materiais relacionados às visualizações.
- `docs/`: documentação complementar, metodologia e decisões técnicas.
- `README.md`: apresentação, objetivos e evolução do projeto.
- `.gitignore`: configuração dos arquivos que não devem ser versionados.

A estrutura poderá evoluir conforme novas necessidades surgirem.

## 🗄️ Banco de dados

O projeto utilizará PostgreSQL como banco de dados relacional.

**Configuração inicial:**

- SGBD: PostgreSQL 17.
- Banco local de estudos: `laboratorio_dados`.
- Esquema previsto para este projeto: `mercado_financeiro`.

O banco permitirá organizar os dados históricos e desenvolver consultas para responder às perguntas propostas.

Os scripts necessários para reproduzir a estrutura serão documentados ao longo do desenvolvimento.

## 🌐 Fontes de dados

Serão priorizadas fontes públicas, documentadas e com procedência verificável.

Fontes inicialmente consideradas:

- [Banco Central do Brasil — Dados Abertos](https://dadosabertos.bcb.gov.br/)
- [Banco Central do Brasil — SGS](https://www3.bcb.gov.br/sgspub/)
- [B3 — Bolsa de Valores Brasileira](https://www.b3.com.br/)
- [CoinGecko — Dados de Criptomoedas](https://www.coingecko.com/en/api)

A seleção definitiva das fontes dependerá da disponibilidade dos dados, da metodologia de coleta e das condições de utilização.

As bases efetivamente utilizadas serão identificadas com suas respectivas fontes, períodos e datas de consulta.

## 🔎 Metodologia prevista

O desenvolvimento será dividido em etapas.

**1. Coleta de dados**

Identificação das fontes, seleção dos indicadores e obtenção das séries históricas.

**2. Preparação e qualidade**

Verificação de formatos, datas, valores ausentes, duplicidades e eventuais inconsistências.

**3. Armazenamento**

Organização dos dados no PostgreSQL, incluindo definição das tabelas e seus relacionamentos.

**4. Análise exploratória**

Desenvolvimento de consultas SQL e análises para compreender o conteúdo e o comportamento dos dados.

**5. Construção de indicadores**

Cálculo de métricas como retorno acumulado, variações percentuais, médias móveis e volatilidade histórica.

**6. Visualização**

Desenvolvimento de gráficos, relatórios e dashboards para comunicar os resultados.

**7. Documentação**

Registro das decisões técnicas, limitações, análises e conclusões obtidas.

## 📈 Resultados e análises

*Em desenvolvimento.*

Esta seção será preenchida conforme as análises forem realizadas e validadas.

Serão apresentados os indicadores calculados, gráficos produzidos, interpretações e limitações identificadas.

## 🚧 Status do projeto

**Em desenvolvimento — fase de estruturação.**

Concluído:

- [x] Definição inicial do tema.
- [x] Criação da estrutura local de diretórios.
- [x] Inicialização do repositório Git.
- [x] Criação do banco PostgreSQL de estudos.

Próximas atividades:

- [ ] Configurar o `.gitignore`.
- [ ] Realizar o primeiro commit.
- [ ] Selecionar a primeira fonte de dados.
- [ ] Criar o esquema do projeto no PostgreSQL.
- [ ] Importar e validar os dados históricos.
- [ ] Desenvolver as primeiras consultas SQL.
- [ ] Construir os primeiros indicadores financeiros.
- [ ] Introduzir Python e Pandas nas análises.
- [ ] Desenvolver visualizações e dashboards.
- [ ] Publicar o projeto no GitHub.

## 📚 Aprendizados

Esta seção documentará os principais conhecimentos desenvolvidos durante o projeto, incluindo:

- SQL aplicado à análise de dados.
- Modelagem e consultas em bancos relacionais.
- Tratamento e validação de dados.
- Manipulação de séries temporais.
- Estatística aplicada ao mercado financeiro.
- Comunicação de resultados analíticos.
- Versionamento e documentação de projetos.

## ⚠️ Observações

Este projeto possui finalidade educacional e analítica.

As análises utilizarão dados históricos e não constituem recomendações personalizadas de investimento.

Resultados passados não garantem desempenho futuro. As interpretações considerarão as limitações das fontes, dos períodos analisados e das metodologias utilizadas.

---

**Projeto desenvolvido como parte da minha formação em Análise e Desenvolvimento de Sistemas, com foco no desenvolvimento de competências em Análise de Dados aplicada ao mercado financeiro.**