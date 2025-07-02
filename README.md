
# 🚀 Projeto: Pipeline de Dados CNPJ - Receita Federal

Este projeto faz parte de um pipeline de **Engenharia de Dados** voltado para trabalhar com os **dados públicos de CNPJ da Receita Federal do Brasil**.

O foco atual é a **coleta automatizada**, **extração**, **auditoria de logs** e preparação dos dados brutos para as próximas etapas de **limpeza, transformação, carga e geração de insights analíticos**.

---

## 📂 Estrutura Atual do Projeto

```
OPEN-CNPJ-DATA-PIPELINE/
├── data_ingestion/
│   ├── raw_data/
│   ├── scripts/
│   │   ├── download_files.py
│   │   ├── re_download_failed.py
│   │   ├── unzip_analysis.py
│   │   └── unzip_files.py
│   └── unzipped/
├── .gitignore
├── LICENSE
└── README.md
```

---

## ✅ Scripts Atuais

### 📥 1) `download_files.py`
- Faz o download automático dos arquivos `.zip` de todas as pastas mensais no site da Receita Federal.
- Mantém um log (`downloaded_files.log`) para evitar downloads repetidos.

---

### 📂 2) `unzip.py`
- **Extrai todos os ZIPs dentro de `raw_data/` a cada execução**, sem verificar se já foram extraídos antes.
- Cria pastas no `unzipped/` com a **mesma estrutura de diretórios que existe no site de origem** (Exemplo: `unzipped/2024-05/`).
- **Renomeia o CSV extraído para ter o mesmo nome base do ZIP**.  
Exemplo:  
Se o ZIP for `Empresas0.zip`, o CSV resultante será `Empresas0.csv`.
- **Exclui automaticamente o arquivo ZIP** após extração bem-sucedida.
- Registra todas as ações (sucessos, erros, tempo, etc) no arquivo de log: `unzip_log.txt`.

---

### 🧾 3) `unzip_analysis.py`
- Analisa o `unzip_log.txt` e gera um resumo estatístico com:
  - ✅ Total de arquivos extraídos com sucesso
  - ❌ Total de arquivos corrompidos
  - ⏱️ Tempo total gasto no processo de unzip
- Útil para **auditoria** da etapa de ingestão de dados brutos.

---

### ♻️ 4) `re_download_failed.py`
- Lê o log de unzip.
- Identifica todos os `.zip` que falharam por estarem corrompidos.
- Faz o **re-download automático** apenas desses arquivos, sobrescrevendo os anteriores.

---

## 📊 Próximas Etapas do Projeto (Planejadas)

✅ Coleta → ✅ Extração → 🧹 Limpeza → 🏗️ Transformação → 🗄️ Armazenamento → 📈 Análise de Dados → 📊 Geração de Insights

- **Limpeza e Tratamento (ETL)**: Corrigir formatos, eliminar duplicatas e validar integridade.
- **Armazenamento**: Preparar os dados para consumo analítico (ex.: Data Lake, Data Warehouse).
- **Visualizações e Dashboards**: Criar painéis e relatórios para explorar os insights.

---

## ⚠️ Possíveis Problemas Conhecidos

| Problema | Causa | Solução |
|---|---|---|
| ❌ Erro de Extração | Arquivo ZIP corrompido | Rodar o `re_download_failed.py` |
| ❌ Espaço em Disco | Sem espaço disponível | Liberar espaço e reexecutar o processo |
| ❌ Interrupção de Internet | Download incompleto | Reexecutar o `download_files.py` |

---

## 👨‍💻 Requisitos Técnicos

- **Python 3.x**
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`

Instalação rápida das dependências:

```bash
pip install requests beautifulsoup4
```

---

## 💬 Sobre o Projeto
Projeto pessoal de **Engenharia de Dados**, focado na construção de um pipeline completo para ingestão e processamento de dados públicos do CNPJ.

O foco futuro será aplicar **limpeza**, **validação**, **transformação** e por fim, **análises exploratórias e geração de insights** para negócios, pesquisas ou projetos de ciência de dados.

---

## 🤝 Contribuições
Sugestões, issues e pull requests são muito bem-vindos!
Este projeto tem como principal objetivo o aprendizado e a troca de conhecimento.


---

## ⚠️ Aviso Legal
Os dados utilizados são públicos e disponibilizados pela Receita Federal.
Este projeto não tem vínculo com a Receita Federal e é apenas um exercício educacional e de aprendizado de engenharia de dados.

---