
# lillie - Projeto de plataforma para serviços voltados a animais

## Dependências

 - Flask
 - gunicorn
 - passlib
 - python-dotenv
 - requests
 - SQLAlchemy
 - psycopg2
 - pipenv
 - Bootstrap CDN
 - Postgres SQL
 
## Setup

Clonar esse repo e acessa-lo;

```sh 
$ cd lillie-py
```
Realizar a inicialização com ambiente:

```sh 
$ pipenv shell
```

Após inicializado, use install para a configuração das dependências contidas no *Pipfile.lock*:

```
$ pipenv install
```

Em *app/.env*, configure as variáveis de ambiente usadas pela aplicação:

```
DATABASE_URI=sua_database_uri_aqui
MAPS_API_KEY=sua_chave_distancematrix_aqui
SECRET_KEY=sua_chave_secreta_aqui
UPLOAD_FOLDER=app/content/static
ALLOWED_EXTENSIONS={'png', 'jpg', 'jpeg'}
```

Execute o *app/scripts/createDatabaseAssests.py* para que as estruturas relacionais dos modelos sejam criadas no banco de dados previamente definido:

```
python app/scripts/createDatabaseAssests.py
$
```

Por fim, crie um servidor local por via do *wsgi.py*:

```
$ python wsgi.py
* Serving Flask app 'app.main'
```
## Deploy

Deploy pode ser realizado via o servidor gunircorn usando um worker.
Exemplo Heroku, contido em *Procfile*:
```
web: gunicorn wsgi:app
```