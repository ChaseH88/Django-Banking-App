# Banking Application

This is a simple banking application that allows users to create accounts, deposit and withdraw money, and view their account balance. This application was created using Python and SQLite.

## Installation
```
pip install django 
```

## Usage

Running the application:
```
python3 manage.py runserver
```

Create Tables:
```
python3 manage.py makemigrations banking_app
```

Updating the database:

Any time you make changes to the models, you will need to run the following commands to update the database:
```
python3 manage.py makemigrations && python3 manage.py migrate 
```
