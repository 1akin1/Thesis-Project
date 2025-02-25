# Thesis Database Management System

This Django web application is designed to manage thesis-related data. It provides a user-friendly interface for users to perform operations like adding, viewing, updating, searching, and deleting thesis records in a MySQL database. The system handles thesis details such as title, author, type, and year.

## Features

- **Add**: Add new thesis records to the database.
- **View**: View all stored thesis records.
- **Search**: Search for thesis records by title, author, or type.
- **Update**: Update existing thesis records.
- **Delete**: Delete thesis records from the database.

## Technologies Used

- **Django**: Web framework for building the application.
- **MySQL**: Database management system to store thesis data.
- **Bootstrap**: Frontend framework for responsive and modern design.

## Prerequisites

- Python 3.x
- MySQL Database server
- Django 3.x or higher

## Setup Instructions

### 1. Create Project Directory

Create a directory for your Django project:

```bash
mkdir /c/django
cd /c/django
2. Set Up a Virtual Environment
Create and activate a virtual environment:

bash
Copy
Edit
# On Windows:
python -m venv virt
source virt/Scripts/activate  

# On macOS/Linux:
python3 -m venv virt
source virt/bin/activate
3. Install Dependencies
Install Django and MySQL connectors using pip:

bash
Copy
Edit
pip install django
pip install mysqlclient
pip install mysql-connector-python
4. Create the Django Project
Create a new Django project:

bash
Copy
Edit
django-admin startproject dbproject
cd dbproject
5. Create a Django App
Create a new Django app to manage thesis data:

bash
Copy
Edit
python manage.py startapp web
6. Configure MySQL Database
In the settings.py file of your Django project, configure the database connection to MySQL:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thesis_db',  # Database name
        'USER': 'your_mysql_user',  # MySQL user
        'PASSWORD': 'your_mysql_password',  # MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
7. Run Migrations
Run the migrations to set up the database schema:

bash
Copy
Edit
python manage.py migrate
8. Create a Superuser
Create a superuser to access the Django admin panel:

bash
Copy
Edit
# On Windows:
winpty python manage.py createsuperuser  

# On macOS/Linux:
python manage.py createsuperuser
Follow the prompts to set up your admin credentials.

9. Run the Development Server
Start the development server:

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to access the application.

Testing the Application
Once the server is running, you can test the following functionalities:

Add: Add new thesis records by filling out the provided forms.
View: View all stored thesis records.
Search: Use the search functionality to find thesis records by title, author, or type.
Update: Edit existing thesis records.
Delete: Delete thesis records from the database.
Additional Notes
Make sure you have set up your MySQL server and created the database before running migrations.
If you need a separate script to create the database, you can create and run db.py (though this step is usually managed by Django).
bash
Copy
Edit
touch db.py
python db.py  # Run if necessary
