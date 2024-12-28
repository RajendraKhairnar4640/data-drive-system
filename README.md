# Folder Management Web Application

This project is a web application for managing folders with features such as creating, renaming, and deleting folders. It also supports navigation between parent and subfolders.

## Features
- View folder details including subfolders.
- Create new subfolders within a folder.
- Rename and delete folders.
- Navigate to parent folders.
- Logout functionality.

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS
- **Templating**: Django Template Language
- **Database**: SQLite (default for Django, can be replaced as needed)

## Prerequisites
- Python 3.8 or above
- pip (Python package installer)

## Create and activate a virtual environment:
```
python -m venv venv
```
## Install dependencies:
```
pip install -r requirements.txt
```
## Apply migrations to set up the database:
```
python manage.py migrate
```
## Run the development server:
```
python manage.py runserver
```
## Open the application in your browser at:
```
http://127.0.0.1:8000/
```
## Project Structure
```bash
folder-management-app/
├── templates/              # Contains HTML templates
├── static/                 # Static files (CSS, JS, images)│
├── manage.py               # Django project management script
├── drive/                  # Main application directory
│   ├── models.py           # Database models
│   ├── views.py            # Application views (business logic)
│   ├── urls.py             # URL routing for the application
│   └── admin.py            # Django admin configuration
│
├── db.sqlite3              # SQLite database file (default)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
