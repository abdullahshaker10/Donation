#!/bin/sh

# Print a message
echo "Starting the Django application..."

# Run database migrations
echo "Applying database migrations..."
python manage.py migrate


# Create Roles and Permissions
echo "Creating Rules and Permissions..."
python manage.py create_config_data

# Start the Django development server
echo "Starting the development server..."
python manage.py runserver 0.0.0.0:8004