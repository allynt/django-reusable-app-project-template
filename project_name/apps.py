from django.apps import AppConfig


class {{ camel_case_project_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ project_name }}'
