# Crowd-Funding Web app 
- This web application aims to provide a platform for users in Egypt to create and donate to fundraising projects. Users can create projects, set fundraising goals, upload project details and images, and receive donations from other users. The application includes authentication, user profiles, project management, commenting, reporting, rating, and search functionality. 

## Installation
    - pip install django
    - venv\Scripts\activate
    - django-admin startproject Backend
    - cd Backend
    - py manage.py startapp accounts, categories, tags, projects, payments, comments, ratings, comment_report, project_reports
    - Update the settings.py with database configuration
    - create new database with name "crowdsource"
    - create new user with name "iticorwdsource" and password "123456"
        - CREATE USER 'iticorwdsource'@'localhost' IDENTIFIED BY '123456';
        - GRANT ALL PRIVILEGES ON *.* TO 'iticorwdsource'@'localhost';

    - python manage.py makemigrations
    - python manage.py migrate

 

## packages 
    - pip install mysqlclient
    - Pip install ipython
    - pip install pillow
    - pip install django_cleanup
    - pip install djangorestframework
    - pip install pygments  # We'll be using this for the code highlighting
    - pip install python-dotenv
    - pip install djangorestframework-simplejwt
    - pip install django-cors-headers
    - pip install django-multiupload

    ## Frontend
        - npm install -g @vue/cli
        - npm install
        - npm install vue-router pinia axios












