# ASSET MANAGER
manage user assets

#USERS
#ASSETS

#helpers
python manage.py startapp user
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
### django views
CreateView – Use this view to display a form for creating a new object and saving it to the database after validation.
UpdateView – Use this view to display a form for updating an existing object and saving the changes after validation.
DeleteView – Use this view to confirm and delete a specific object from the database.
DetailView – Use this view to display a single object's details, typically read-only.
ListView – Use this view to display a list of objects, often with pagination.
FormView – Use this view when handling forms that don’t create or update a model instance directly.
TemplateView – Use this view to render a specific template without requiring a model or form processing.
RedirectView – Use this view to redirect to another URL.
