# settings_development.py
import os

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGO_DB_ENGINE'),
        'NAME': os.environ.get('MONGO_DB_NAME'),
        'ENFORCE_SCHEMA': os.environ.get('MONGO_DB_ENFORCE_SCHEMA'),
    }
}