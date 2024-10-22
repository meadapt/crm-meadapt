# CRM Me Adapt

Neste repositório construímos um modelo simples de CRM para controlar vendas de uma empresa como execício de como fazer um projeto Django.

Confira no nosso [canal do Youtube](https://www.youtube.com/@me-adapt) o passo a passo desse projeto e faça junto com a gente!

## Setup

- Clonar repositório
```$
git clone https://github.com/automatiza-mg/aura.git
```

- Criar ambiente virtual python e instalar pacotes

```python
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

- Rodar migrações

```python
$ python manage.py migrate
```

- Criar usuário[^1]

```python
$ python manage.py createsuperuser
```

- Ligar o servidor

```python
$ $ python manage.py runserver
```
- Acessar a url informada e adicionar ao final ```/admin```

   ```http://127.0.0.1:8000/admin/```

[^1]: Ao tentar criar seu usuário, se você encontrar o erro `Superuser creation skipped due to not running in a TTY. You can run manage.py createsuperuser in your project to create one manually.`, você pode utilizar o comando `winpty python manage.py createsuperuser`.