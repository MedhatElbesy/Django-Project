# Crowd-Funding Web app 
- Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. Crowdfunding is a form of crowdsourcing and alternative finance. In 2015, over US$34 billion was raised worldwide by crowdfunding. (From Wikipedia) 

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


    ## Frontend
        - npm install -g @vue/cli
        - npm install
        - npm install vue-router pinia axios












