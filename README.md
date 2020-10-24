

# Shorting (https://cuturls.live/)
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)


### Installation:
1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`

4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/shorting`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/shorting/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo su postgres`
3. Log into a Postgres session:  
`psql`
4. Create database with name **shorting**:  
`CREATE DATABASE shorting;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER shorting_user WITH PASSWORD 'shorting_pass';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE shorting_user SET client_encoding TO 'utf8';`  
`ALTER ROLE shorting_user SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE shorting_user SET timezone TO 'UTC';` 
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE shorting TO shorting_user;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`

9. Activate the virtual environment:  
`source ~/.virtualenvs/shorting/bin/activate`
10. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`

##### Use admin interface:
1. Create an admin user:  
`python manage.py createsuperuser`
2. Run the project locally:  
`python manage.py runserver`
3. Navigate to: `http://localhost:8000/admin/`


### Endpoints
#### Create ShortURL
```
Endpoint: short-url/
Method: POST
body: {"original_url": "url"}
```

#### GO To Original URL
```
Endpoint: short-url/{key}
Method: GET
```