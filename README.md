# Django Blog

This is a simple blog made with Python and Django with the purpose of simplifying my workflow and sharing my progress in my pursuit of my degree in computer science.

## The Idea

The fundamental idea behind this project is to create a community focused on understand the background of this career and provide some useful articles with some real examples and without worrying about understading the "sientists's laguage" and other abstract explanations.

> My goal with this project is to provide a different perspective on the topics covered in class and offer more understandable explanations, without scientific clichés or complicated language; just clear and to-the-point ideas with examples that are grounded enough to be relatable.

> "Mi objetivo con este proyecto es proporcionar una mirada diferente acerca de los temas tratados en clase y proporcionar explicaciones mas entendibles, sin clichés científicos o lenguaje complicado; solo ideas claras y al grano con ejemplos lo suficientemente cercanos al planeta tierra."

## Development

This project are currently beign develop and may contain so many bugs or backdors, so if you want to contribute and patch them, I'll appreciate it.

### Project Structure

Here is the basic structure of the project and what purpose each file or folder has.

```
.
+-- manage.py       # Django Project Entrypoint
+-- .env            # Local environments vars
+-- db.sqlite       # Local database
+-- /web            # Root Application.
|   +-- settings.py # Where the settings are defined.
|   +-- urls.py     # Where the urls are mapped with the view.
+-- /app            # Dedicated blog application.
|   +-- /migrations # Database migration files.
|   +-- /templates  # HTML templates.
|   +-- models.py   # Database models.
|   +-- admin.py    # Register the models in the admin dashboard.
|   +-- views.py    # Application views logic.
|   +-- managers.py # Custom database managers.
+-- /statics        # Where statics files are located.
+-- /docs           # Developer guides and other important documentation.
```

### Virtual Environment

Make sure you've enabled a virtual environment. If you doesn't have enabled one, then run the follow command to install and create a virtual environment:

```bash
# Install virtualenv globally.
\your\workspace\this-project> pip install virtualenv

# Create a virtual environment in your workspace.
\your\workspace\this-project> pip -m venv venv

# Once created, run.
\your\workspace\this-project> ./venv/Scripts/activate
```

### Dependencies

Before start develop, make sure you've installed all dependencies. Use `pip install requirements.txt` and populate the `.env` file with your local environs
variables.

```
APP_SECRET_KEY="<INSER HERE YOUR GENERATED SECRET>"
APP_DEBUG_MODE="1"
```

When a new dependency were aded, you may update the `requirements.txt` file with the follow command: `pip freeze > requirements.txt`.

### Migrations

Use `python manage.py migrate app` to generate the migrations for the project `app`. Use the same command with the `app` argument to migrate the root app `web`.

### Make migrations.

When creating new changes to the database, make you sure to use the command `python manage.py makemigrations app` to create the corresponding migration file.

### Run tests

During the development process you may wish test your code and make sure that tha application are running correctly. For this task you will run this command `python manage.py test`.

### Launch a development server

Before launching a development server, make sure you have enabled your virtual environment. Next you will run this command in your terminal `python manage.py runserver`.

## Features

- [_] Develop a custom markdown extension.
- [_] Dockerize this app.
- [_] Improve the UI.
- [_] Expose a Graphql API for other web appliances.
