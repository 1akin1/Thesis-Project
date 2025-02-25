# Thesis Database Management System

This Django web application is designed to manage thesis-related data. It allows users to add, view, update, search, and delete thesis records in a MySQL database. The system provides a user-friendly interface for managing thesis details such as title, author, type, and year.

Features

Add: Add new thesis records to the database.

View: View all stored thesis records.

Search: Search thesis records by title, author, or type.

Update: Edit existing thesis records.

Delete: Delete thesis records from the database.

Technologies Used

Django: Web framework for building the application.

MySQL: Database management system to store thesis data.

Bootstrap: Frontend framework for responsive and modern design.

Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.x

MySQL Database server

Django 3.x or higher

Setup Instructions

Create the Project Directory

Start by creating a directory for your Django project:

mkdir /c/django

cd /c/django

Set Up a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

python -m venv virt

source virt/Scripts/activate (For Windows)

source virt/bin/activate (On macOS/Linux)

Install Dependencies

Install the required packages for Django and MySQL integration:

pip install django

pip install mysqlclient

pip install mysql-connector-python

Create the Django Project

Create a new Django project to manage the thesis data:

django-admin startproject dbproject

cd dbproject

Create a Django App

Generate a new app within the project to handle the thesis records:

python manage.py startapp web

Create the Database (Optional)

If you need to manually create the database, you can write a script and run it. Typically, Django handles database creation automatically:

touch db.py

python db.py (Run if necessary)

Run Migrations

Migrate the database schema to set up the required tables:

python manage.py migrate

Create a Superuser

Create a superuser account for accessing the Django admin panel:

winpty python manage.py createsuperuser (For Windows)

python manage.py createsuperuser (On macOS/Linux)

Follow the prompts to set up the superuser credentials.

Start the Development Server

Run the development server to begin using the application:

python manage.py runserver

You can now access the app by visiting http://127.0.0.1:8000/ in your web browser.

Testing the Application

Once the server is running, test the following features:

Add: Add new thesis records using the provided form.

View: View all stored thesis records.

Search: Search for thesis records by title, author, or type.

Update: Modify existing thesis records.

Delete: Remove thesis records from the database.
