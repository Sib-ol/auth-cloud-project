#!/usr/bin/env bash
# build.sh

# Exit on error
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🧱 Running migrations..."
python manage.py makemigrations
python manage.py migrate
