# 📦 Open CNPJ Data Pipeline (Local Version)

Pipeline de dados **100% local** para ingestão, tratamento e exploração dos dados públicos de CNPJ disponibilizados pela **Receita Federal do Brasil**.

---

## 📌 Objetivo

Criar um fluxo local de ponta a ponta para:

✅ Fazer o download automático dos dados abertos do CNPJ  
✅ Realizar a extração (unzip) dos arquivos  
✅ Fazer a limpeza e transformação com **Python (Pandas/PySpark)**  
✅ Armazenar de forma estruturada (Parquet, CSV, SQLite ou PostgreSQL local)  
✅ Permitir consultas e geração de insights via **ferramentas de BI locais** como **Apache Superset**, **Metabase** ou **Jupyter Dashboards**

---

## 🛠️ Estrutura Atual do Projeto
```bash
open-cnpj-data-pipeline/
├── data_ingestion/
│ └── scripts/
│ ├── download_files.py
│ └── unzip_files.py
├── raw_data/ # Dados brutos baixados (ZIPs)
├── unzipped/ # Arquivos extraídos
├── processed_data/ # Dados tratados (Parquet / CSV)
├── README.md
└── requirements.txt
```
---

## ✅ Fases do Pipeline

| Etapa                         | Ferramentas                 | Local |
|-------------------------------|-----------------------------|------|
| Ingestão (download + unzip)   | Python (requests, zipfile)  | ✅ |
| Tratamento / Limpeza          | Python (Pandas ou PySpark)  | ✅ |
| Armazenamento intermediário   | Parquet, CSV, SQLite ou PostgreSQL | ✅ |
| Consulta e BI                 | Superset / Metabase / Jupyter | ✅ |

---

## ▶️ Como Rodar o Projeto

### 1. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 2. Baixe os arquivos da Receita Federal:
```bash
python data_ingestion/scripts/download_files.py
```

### 3. Extraia todos os arquivos ZIP:
```bash
python data_ingestion/scripts/unzip_files.py
```

## 4. Próximas Etapas:
🚧 Criar scripts de limpeza e transformação com Pandas / PySpark

🚧 Salvar os dados finais em Parquet, CSV ou Banco de Dados local

🚧 Configurar a ferramenta de BI escolhida (Apache Superset, Metabase ou Jupyter Dashboards)



## 📌 Roadmap Futuro:
✅ Download automatizado

✅ Extração (unzip) dos dados

🚧 Limpeza e transformação

🚧 Armazenamento estruturado

🚧 Visualização e BI local


## 🤝 Contribuições
Sugestões, issues e pull requests são muito bem-vindos!
Este projeto tem como principal objetivo o aprendizado e a troca de conhecimento.

## 📎 Repositório
🔗 https://github.com/19lemabe94/open-cnpj-data-pipeline

## ⚠️ Aviso Legal
Os dados utilizados são públicos e disponibilizados pela Receita Federal.
Este projeto não tem vínculo com a Receita Federal e é apenas um exercício educacional e de aprendizado de engenharia de dados.