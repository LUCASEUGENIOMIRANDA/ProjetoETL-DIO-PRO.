# 📊 ETL com Enriquecimento de Dados via IA

Este projeto implementa um pipeline simples de **ETL (Extract, Transform, Load)** com uma camada adicional de **enriquecimento de dados utilizando IA**.

O objetivo é ler dados de um arquivo CSV, tratar e padronizar essas informações, permitir a consulta por IDs e, por fim, gerar conteúdos personalizados para cada registro usando a API da OpenAI.

---

## 🚀 Funcionalidades

* Leitura de dados a partir de arquivo CSV
* Normalização de colunas (remoção de espaços e padronização)
* Geração automática de identificadores únicos (hash MD5)
* Filtro de registros por IDs informados pelo usuário
* Conversão dos dados para formato JSON
* Geração de conteúdo personalizado com IA
* Tratamento de erros com retry automático

---

## 🧠 Arquitetura do Pipeline

O fluxo segue as etapas clássicas de ETL:

### 1. Extract (Extração)

* Leitura do arquivo `Data.csv`
* Conversão de todos os dados para string para evitar inconsistências

### 2. Transform (Transformação)

* Padronização dos nomes das colunas
* Criação de uma coluna `id` caso não exista
* Limpeza e validação dos dados
* Filtragem baseada nos IDs informados

### 3. Load (Carga)

* Exibição dos dados filtrados no console (formato JSON)

### 4. Enrichment (Enriquecimento com IA)

* Geração de notícias personalizadas para cada usuário
* Uso de modelo de linguagem para criação de conteúdo dinâmico
* Limite de caracteres para respostas
* Retry automático em caso de falha na API

---

## 📥 Entrada

O usuário fornece uma lista de IDs via terminal:

```
Digite os IDs separados por vírgula:
```

---

## 📤 Saída

* Lista de usuários encontrados no CSV
* Notícias personalizadas geradas por IA para cada usuário

---

## ⚠️ Boas Práticas e Segurança

* **Nunca exponha sua API Key no código**
* Utilize variáveis de ambiente para armazenar credenciais sensíveis

Exemplo:

```bash
export OPENAI_API_KEY="sua-chave-aqui"
```

---

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* OpenAI API
* JSON
* Hashlib

---

## 💡 Possíveis Melhorias

* Processamento em batch para reduzir custo e latência
* Persistência dos resultados em banco de dados
* Criação de API (ex: FastAPI)
* Execução assíncrona/paralela
* Monitoramento e logging estruturado
* Deploy em ambiente cloud

---

## 📌 Observação

Este projeto é uma base para construção de pipelines mais robustos de engenharia de dados com integração de inteligência artificial.

---

## 👨‍💻 Autor
Lucas Eugênio Miranda Pinto.

Projeto de desenvolvido para fins de estudo e aplicação prática de conceitos de ETL e IA.
