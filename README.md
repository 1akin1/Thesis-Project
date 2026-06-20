# 📚 Thesis Database Management System

A Django-based web application for managing thesis records. Create, view, search, update, and delete thesis entries through a clean, responsive interface backed by a MySQL database.

<img width="1593" height="846" alt="1" src="https://github.com/user-attachments/assets/44f13b4b-0bea-4e48-bfdd-fe9593c98437" />


---

## ✨ Features

| Feature | Description |
| --- | --- |
| **Add** | Add new thesis records to the database. |
| **View** | Browse all stored thesis records. |
| **Search** | Find records by title, author, or type. |
| **Update** | Edit the details of an existing thesis. |
| **Delete** | Remove thesis records from the database. |

Each thesis record stores its **title**, **author**, **type**, and **year**.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python web framework)
- **Database:** MySQL
- **Frontend:** Bootstrap (responsive, modern UI)

---

## 📋 Prerequisites

Make sure the following are installed before you begin:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/)
- `pip` (comes bundled with Python)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/thesis-db-management.git
cd thesis-db-management
```

### 2. Create and activate a virtual environment

```bash
python -m venv virt

# Windows (Git Bash)
source virt/Scripts/activate

# Windows (CMD)
virt\Scripts\activate

# macOS / Linux
source virt/bin/activate
```

### 3. Install dependencies

```bash
pip install django mysqlclient
```

> 💡 If `mysqlclient` fails to install on Windows, you can use the pure-Python
> alternative instead: `pip install mysql-connector-python`.

You can also save your dependencies for others:

```bash
pip freeze > requirements.txt
```

…and later restore them with `pip install -r requirements.txt`.

### 4. Configure the database

Create a MySQL database for the project:

```sql
CREATE DATABASE thesis_db CHARACTER SET utf8mb4;
```

Then update the `DATABASES` setting in `dbproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thesis_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for the admin panel)

```bash
# Windows (Git Bash)
winpty python manage.py createsuperuser

# macOS / Linux
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit **http://127.0.0.1:8000/** to start using the app.
The admin panel is available at **http://127.0.0.1:8000/admin/**.

---

## 📂 Project Structure

```
dbproject/
├── dbproject/          # Project settings & configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── web/                # Main app (thesis records)
│   ├── models.py       # Thesis data model
│   ├── views.py        # Add / view / search / update / delete logic
│   ├── urls.py
│   └── templates/      # Bootstrap-based HTML templates
├── manage.py
└── requirements.txt
```

---

## 🧪 Testing the Application

Once the server is running, try out each feature:

1. **Add** a new thesis using the form.
2. **View** the list of all stored records.
3. **Search** by title, author, or type.
4. **Update** an existing record's details.
5. **Delete** a record you no longer need.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
