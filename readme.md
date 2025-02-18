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
<li>Chave da API OMDb (pode ser obtida em <a href="https://www.omdbapi.com/apikey.aspx">OMDb</a>) </li>
<H3>Configuração do Ambiente</H3>
<p>1. Clone o repositório:</p>
<pre><code>git clone https://github.com/pedrohrqb/desafio-data-base
cd seu_projeto</code></pre>
<p>2. Crie e ative um ambiente virtual</p>
<pre><code># No Windows
python -m venv venv
venv\Scripts\activate
<p>
# No macOS/Linux
python -m venv venv
source venv/bin/activate</code></pre>
<p>3. Instale as dependências</p>
<pre><code>pip install requests sqlmodel</code></pre>
<p>4. Configure sua chave de API OMDb:</p>
<pre><code>export OMDB_API_KEY='sua_chave_api'</code></pre>
<H3>Execução do Pipeline ETL</H3>
<p>1. Execute o script principal:</p>
<pre><code>python etl_pipeline/main.py</code></pre>
<h3>Verificação dos Dados</h3>
<p>1. Execute o script de verificação para visualizar os dados carregados no banco de dados:</p>
<pre><code>python etl_pipeline/verify_data.py</code></pre>
<h3>Limpeza do Banco de Dados</h3>
<p>1. Execute o script de limpeza para excluir todas as entradas do banco de dados:</p>
<pre><code>python clear_database.py</code></pre>
<h3>Arquitetura do Projeto</h3>
<h3>1. Extração dos Dados</h3>
<p>O arquivo <code>extract.py</code> contém a função <code>fetch_movie_data</code> que utiliza a OMDb API para obter dados de filmes.</p>
<h3>2. Transformação dos Dados</h3>
<p>O arquivo <code>transform.py</code> contém a função <code>transform_data</code> que processa e transforma os dados extraídos para garantir consistência e integridade.</p>
<h3>3. Carga dos Dados</h3>
<p>O arquivo <code>load.py</code> contém:
<br>
Classes <code>Movie</code>, <code>Genre</code> e <code>MovieGenre</code> que representam as tabelas do banco de dados.
<br>
Funções <code>create_db_and_tables</code>, <code>load_data</code> e <code>clear_db</code> para criar, carregar e limpar o banco de dados, respectivamente.
</p>

<h3>4. Orquestração do Pipeline</h3>
<p>O arquivo <code>main.py</code> orquestra o processo ETL, chamando as funções de extração, transformação e carga.</p>

<h3>5. Verificação dos Dados</h3>
<p>O arquivo <code>verify_data.py</code> verifica os dados inseridos no banco de dados e exibe os resultados no console.</p>

<h3>6. Limpeza do Banco de Dados</h3>
<p>O arquivo <code>clear_database.py</code> executa a função <code>clear_db</code> para limpar o banco de dados.</p>

<h3>Contribuição</h3>
<p>1. Fork o projeto.<br>
2. Crie uma nova branch com suas alterações: <code>git checkout -b my-feature</code>.<br>
3. Commit suas alterações: <code>git commit -m 'Add some feature'</code>.<br>
4. Push para a branch: <code>git push origin my-feature</code>.<br>
5. Abra um Pull Request.</p>
