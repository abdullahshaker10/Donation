#!/bin/sh

# Print a message
echo "Starting the Django application..."

# Run database migrations
echo "Applying database migrations..."
python manage.py migrate


# Create Roles and Permissions
echo "Creating Rules and Permissions..."
python manage.py create_config_data

# Start the Daphne server
echo "Starting the Daphne server..."
daphne -b 0.0.0.0 -p 8004 root.config.asgi:application