{% docs __overview__ %}
# DW Market Cap - Data Warehouse de Commodities

Bem-vindo ao **DW Market Cap**, um data warehouse moderno e escalável para análise, transformação e gerenciamento de dados de commodities do mercado financeiro.

## 📋 Visão Geral

Este projeto integra **Python** para extração de dados com **dbt (Data Build Tool)** para transformação e modelagem em um data warehouse. O sistema coleta dados de preços, tendências e análises de commodities, estruturando-os em um modelo de dados bem organizado e pronto para análise.

## 🎯 Objetivo

- **Extrair** dados de commodities via APIs (yfinance)
- **Carregar** dados em um banco de dados relacional (PostgreSQL)
- **Transformar** e modelar dados usando dbt para criar tabelas analíticas
- **Documentar** modelos e lineage de dados automaticamente
- **Fornecer** dados confiáveis e bem estruturados para análises

## 🏗️ Arquitetura do Projeto

```
testeapp/
├── src/                          # Código Python para ELT
│   ├── extract_load.py          # Script de extração e carregamento
│   └── requirements.txt          # Dependências Python
├── dwmarketcap/                  # Projeto dbt
│   ├── models/                   # Modelos SQL dbt
│   │   ├── staging/              # Modelos de staging (STA)
│   │   │   └── stg_commodities.sql
│   │   ├── datamart/             # Modelos de negócio (MAT)
│   │   └── example/              # Exemplos
│   ├── tests/                    # Testes de dados
│   ├── seeds/                    # Dados estáticos
│   ├── macros/                   # Macros reutilizáveis
│   ├── docs/                     # Documentação (este arquivo)
│   ├── target/                   # Artefatos compilados
│   └── dbt_project.yml           # Configuração do projeto
└── README.md                     # Documentação raiz
```

## 📊 Fluxo de Dados

```
APIs (CoinMarketCap) 
    ↓
extract_load.py (extração e carga)
    ↓
Banco de Dados (PostgreSQL)
    ↓
dbt (transformação & modelagem)
    ↓
Raw → Staging (stg_*) → Datamart (mat_*)
    ↓
Dados prontos para análise e BI
```

## 🛠️ Stack Técnico

### Backend & Extração
- **Python 3.x** - Lógica de extração e carregamento
- **yfinance** - API de dados de commodities
- **pandas** - Manipulação e processamento de dados
- **SQLAlchemy** - ORM para banco de dados
- **psycopg2** - Driver PostgreSQL

### Data Warehouse & Transformação
- **dbt (Data Build Tool)** - Transformação de dados em SQL
- **PostgreSQL** - Banco de dados relacional
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 🚀 Como Começar

### Pré-requisitos
- Python 3.8+
- PostgreSQL
- dbt CLI

### Instalação

1. **Clone o repositório e instale dependências Python:**
```bash
pip install -r src/requirements.txt
```

2. **Configure variáveis de ambiente** (.env):
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dwmarketcap
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

3. **Execute a extração de dados:**
```bash
python src/extract_load.py
```

4. **Configure e execute dbt:**
```bash
cd dwmarketcap
dbt debug
dbt run
dbt test
```

5. **Visualize a documentação:**
```bash
dbt docs generate
dbt docs serve
```

## 📁 Estrutura de Modelos dbt

### Staging Layer (`models/staging/`)
Modelos que espelham as tabelas brutas com renomeação de colunas e transformações básicas:
- `stg_commodities.sql` - Dimensão limpa de commodities

### Datamart Layer (`models/datamart/`)
Modelos analíticos finais otimizados para negócio:
- Tabelas de fatos
- Tabelas de dimensão
- Métricas pré-agregadas

### Example Layer (`models/example/`)
Modelos de exemplo e referência:
- `my_first_dbt_model.sql`
- `my_second_dbt_model.sql`

## ✅ Testes de Qualidade

O projeto inclui testes de dados para garantir qualidade:
- `not_null` - Validação de valores nulos
- `unique` - Validação de unicidade
- Testes customizados em `tests/`

Execute com:
```bash
dbt test
```

## 📚 Documentação

A documentação completa é gerada automaticamente a partir de:
- YAML configs em `models/*/schema.yml`
- Docstrings nos modelos SQL
- Lineage de transformações

Acesse em: `http://localhost:8000` após executar `dbt docs serve`

## 🔄 Workflow de Desenvolvimento

1. **Extração**: `python src/extract_load.py` carrega dados brutos
2. **Modeling**: Crie/edite arquivos SQL em `models/`
3. **Testing**: `dbt test` valida integridade dos dados
4. **Documentação**: `dbt docs generate` atualiza docs
5. **Deployment**: Modelos compilados em `target/`

## 📝 Padrões de Nomenclatura

- `stg_*` - Tabelas de staging
- `mat_*` - Tabelas de datamart
- `fct_*` - Tabelas de fatos
- `dim_*` - Tabelas de dimensão
- `int_*` - Modelos intermediários (não expostos)

## 🔗 Recursos Úteis

- [Documentação dbt](https://docs.getdbt.com)
- [yfinance Documentation](https://yfinance.readthedocs.io/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [dbt Best Practices](https://docs.getdbt.com/guides/best-practices)

## 👤 Autor

Desenvolvido como projeto de data warehouse para análise de commodities.

---

**Última atualização**: Dezembro 2025 | **Versão**: 1.0.0
{% enddocs %}