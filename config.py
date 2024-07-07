# config.py

import os

DB_HOST = 'localhost'
DB_NAME = 'projet_api_rest_bd'
DB_USER = 'Helicia'
DB_PASS = 'HeliciaTsika 2'

SECRET_KEY = os.urandom(24)
JWT_SECRET_KEY = 'your_jwt_secret_key'  # Remplacez par votre propre clé secrète
