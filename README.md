# 📊 Open CNPJ Data Pipeline

Projeto de Engenharia de Dados focado na ingestão, transformação e análise de dados públicos de CNPJ disponibilizados pela Receita Federal do Brasil.

---

## 🎯 Objetivo

Criar um pipeline completo de dados com as seguintes etapas:

- Download dos dados abertos do CNPJ
- Armazenamento seguro no AWS S3 (Raw Zone)
- Processamento e transformação com Spark / Pandas
- Consulta via Athena
- Visualização com ferramentas open-source de BI (ex: Superset ou Metabase)
- (Opcional) Orquestração com Apache Airflow

---

## 📌 Tecnologias Utilizadas

| Etapa | Ferramentas |
|----|----|
| Ingestão | Python, AWS S3 |
| Processamento | Apache Spark, Pandas |
| Armazenamento | AWS S3 |
| Catálogo | AWS Glue |
| Consulta SQL | AWS Athena |
| BI | Superset / Metabase |
| Orquestração | Apache Airflow (Opcional) |

---

## 🚩 Estrutura de Pastas

```bash
open-cnpj-data-pipeline/
├── data_ingestion/
├── data_processing/
├── sql_queries/
├── bi_dashboards/
├── airflow_dags/
└── README.md
