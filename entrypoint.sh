#!/bin/sh

# Print a message
echo "Starting the Django application..."

# Run database migrations
echo "Applying database migrations..."
python manage.py migrate


# Create a superuser using the custom command
echo "Creating superuser..."
python manage.py create_default_super_user

# Start the Django development server
echo "Starting the development server..."
python manage.py runserver 0.0.0.0:8004