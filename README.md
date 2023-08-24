# Django Blog(DRF)

This project is a web application that allows users to create, read, update, and delete blog posts. The blog posts can have tags that categorize them by topics. Users can also search for blog posts by title keywords or tags. The app also tracks the number of views for each post

### Features

- Pagination: The app uses HTMX for efficient and user-friendly pagination.
- CRUD: Users can Read posts and Authenticated users can write, Update and delete a blog posts.
- Track Views:  The app tracks the number of views for each post.

### Tech Stack

- Django
- Django Rest Framework
- Bootstrap


### Installation

```
git clone https://github.com/ali-abbaszade/django-myblog.git
```

Create virtual environment and activate

```
python -m venv venv

windows: venv\Scripts\activate
linux: source venv/bin/activate
```

Install the dependencies of the project

```
pip install -r requirements.txt
```

Create all migrations file then apply the migrations

```
python manage.py makemigrations

python manage.py migrate
```

Start the server and run the app

```
python manage.py runserver
```