# Login Readme

## Version:<br>
  - This code was published in iteration 3 <br>

## Dependencies:<br>
  - You will need to install: python, pip, pipenv, and django
  - The following code runs in HTML5 so webpages like Safari may not be able to function properly.
  - Web browsers that disable cookies/cache will not be able to function properly
  - The webpages currently uses a fontawesome api to display the alternative login options (Facebook, Google+)
  - Fontawesome Version: 4.7.0

## How to Run It?<br>
  - Follow these instructions to run the server for the first time:
    - follow [these](https://pip.pypa.io/en/stable/installing/) instructions if you don't have pip installed
    - pip install pipenv
    - pipenv install django
    - pipenv shell
    - python manage.py migrate
    - python manage.py runserver

  - Follow these instructions once you have already installed everything above:
    - python manage.py migrate
    - python manage.py runserver

  - CTRL+CLICK the url that is provided for you in the terminal