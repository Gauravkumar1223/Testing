#!/bin/bash



# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

# Run the development server
exec "$@"
