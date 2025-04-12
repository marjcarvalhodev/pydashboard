#!/bin/bash

# SETTINGS - Update these to match your project
DB_NAME="your_db_name"
DB_USER="your_db_user"
DJANGO_SUPERUSER_USERNAME="marcio"
DJANGO_SUPERUSER_EMAIL="marcio@example.com"
DJANGO_SUPERUSER_PASSWORD="123456"

# Drop and recreate the database
sudo -u postgres psql << EOF
DROP DATABASE IF EXISTS $DB_NAME;
CREATE DATABASE $DB_NAME OWNER $DB_USER;
ALTER SCHEMA public OWNER TO $DB_USER;
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

echo "✅ Database dropped and recreated."

# Re-run migrations
python manage.py migrate

# Create Django superuser non-interactively
export DJANGO_SUPERUSER_USERNAME
export DJANGO_SUPERUSER_EMAIL
export DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --no-input

echo "✅ Django migrations applied and superuser created."
