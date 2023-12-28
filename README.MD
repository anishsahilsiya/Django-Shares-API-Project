# Django Shares API Project

## Overview

This Django project is designed to display shares information obtained from an external API. It includes a web application that fetches data from the API, processes it, and presents it to the user.

## Requirements

Make sure you have the following installed before running the project:

- Python (3.6 or later)
- Django (3.0 or later)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/anishsahilsiya/Django-Shares-API-Project.git
    cd django-shares-api
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```


4. Migrate the database:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to [http://localhost:8000](http://localhost:8000) to view the application.

## Configuration

Update the `config/settings.py` file with your API credentials and settings.

```python
# config/settings.py

# Add your API endpoint URL
API_ENDPOINT = 'https://api.example.com/shares/'

# Add any other necessary configurations
