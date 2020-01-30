# Twitter
A simple twitter application which works same as twitter,user can post and delete the tweets and he can
his recent tweets

# Prerequisites

You need to install the following packages for backend:
```
asgiref==3.2.3
Django==3.0.2
django-cors-headers==3.2.1
djangorestframework==3.11.0
pkg-resources==0.0.0
psycopg2==2.8.4
pytz==2019.3
sqlparse==0.3.0
```
Installing

Clone the repository
```
https://github.com/Harikrishna9738/CabAllocationSystem
```
Setting up your virtual environment:
```
python3 -m venv .env
```
Activate the Virtual Environment:
```
source .env/bin/activate
```
Set Up a Database on local system: During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks:
```
sudo su - postgres
```
You should now be in a shell session for the postgres user. Log into a Postgres session by typing:
```
psql
```
First, we will create a database for our Django project. Each project should have its own isolated database for security reasons. We will call our database myproject in this guide, but it’s always better to select something more descriptive:
```
CREATE DATABASE cabsystem;
```
Remember to end all commands at an SQL prompt with a semicolon.

Next, we will create a database user which we will use to connect to and interact with the database. Set the password to something strong and secure:
```
CREATE USER cabsystemuser WITH PASSWORD 'cabsystem';
```
Afterwards, we’ll modify a few of the connection parameters for the user we just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django projects will be set to use UTC:
```
ALTER ROLE cabsystemuser SET client_encoding TO 'utf8';
ALTER ROLE cabsystemuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE cabsystemuser SET timezone TO 'UTC';
```
Now, all we need to do is give our database user access rights to the database we created:
```
GRANT ALL PRIVILEGES ON DATABASE cabsystem TO cabsystemuser;
```
Exit the SQL prompt to get back to the postgres user’s shell session:
```
\q
```
Exit out of the postgres user’s shell session to get back to your regular user’s shell session:
```
exit
```


Then to run the server, go to the directory 'cabAllocationSystem/backend/cabSystem/' and type the following code in terminal :

python3 manage.py runserver

Your server is set up with all the APIs active.

For Frontend which is html, Dependencies are:
```
"html": "^5",
"css": "^3.12.0",
"Ajax": "^16.12.0",
```



Go to 'twitter/frontend/' and type the following code in the terminal:


The server has been set up and you are up to work on the application.

To make this project following Languages and Libraries have been used: ##Frontend : html,css,Ajax; ##Backend : Python/Django; ##Database : PostgreSQL; ##Python : 3.6.8

P.S:The aesthetics of the page is at the most basic level. Some more work could be put in to beautify the UI. The project has been completed keeping the sole aim as working completion rather than aesthetically pleasing.
