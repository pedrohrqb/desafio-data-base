<!DOCTYPE html>
<h1>ETL Pipeline para Dados de Filmes
<h3>Descrição</h3>
<p>Este projeto desenvolve um pipeline ETL (Extract, Transform, Load) que consome dados de uma API pública sobre filmes (OMDb API), realiza as transformações necessárias e armazena as informações em um banco de dados SQL usando SQLModel.<p>
<h3>Estrutura do Projeto
<pre><code>
├── etl_pipeline/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── clear_database.py
│   ├── main.py
│   └── verify_data.py
├── venv/
├── movies.db
└── README.md</code></pre>
<h3> Requisitos </h3>
<li>Python 3.6+</li>
<li>Bibliotecas: requests, sqlmodel</li>
<li>Chave da API OMDb (pode ser obtida em <a href="https://www.omdbapi.com/apikey.aspx">OMDb)</a> </li>
<H3>Configuração do Ambiente</H3>
<p>1.</p> Clone o repositório:
<code>git clone https://github.com/pedrohrqb/desafio-data-base
      cd seu_projeto</code>

