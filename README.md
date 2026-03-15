![banner](./static/img/Group%2088.png)

> [!NOTE]
> This project was created as an experiment on the existing website: [https://hollywood.od.ua/](https://hollywood.od.ua/)

## Technology Stack:

* **Django**
  A high-level Python web framework used for backend development, authentication, access control, and form handling

* **PostgreSQL**
  A powerful relational database system used for storing patient data, personal account information, appointment records, and related medical data

* **HTML & CSS**
  Standard markup and stylesheet languages used to structure and control the appearance, layout, and responsiveness of the website

* **JavaScript**
  A programming language used to create interactive elements and dynamic behavior on the frontend

* **Unfold**
  A modern Django admin interface used to enhance the appearance and usability of the administration panel

## Getting Started:

### 1. Clone the repository

```bash
git clone https://github.com/Marchello-Projects/Hollywood-Django
```

### 2. Create and activate virtual environment 

```bash
python3 -m venv .venv
source .venv/bin/activate  
# On Windows: 
# python -m venv .venv
# .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Set up environment variables

Create a `.env` file in the root directory with the following content:

```env
SECRET_KEY=Your_django_secret_key
DEBUG=True

DB_NAME=Database_Name
DB_USER=Database_user
DB_PASSWORD=Database_password
DB_HOST="localhost"

DJANGO_SUPERUSER_EMAIL=exampleadmin@gmail.com
DJANGO_SUPERUSER_PASSWORD=strongpassword_1234
```

> [!NOTE]
> **Generate a Secret Key**:
> Run the following command in your terminal to generate a new secure key:
> ```bash
> python3 -c 'import secrets; print(secrets.token_urlsafe(50))'
> # On Windows: python -c "import secrets; print(secrets.token_urlsafe(50))"
> ```

### 5. Apply database migrations

Initialize the database schema:

> [!NOTE]
> This step will also automatically create your superuser based on the credentials in your `.env` file

```bash
python3 manage.py migrate
# On Windows: python manage.py migrate
```

### 6. Run the development server

Start the server to access the application:

```bash
python3 manage.py runserver
# On Windows: python manage.py runserver
```
