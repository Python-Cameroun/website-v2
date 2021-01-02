## Installation

Install python 3.x and pip  
 
Fork and/or clone this project by running the following command
``` bash  
$ git clone https://github.com/Python-Cameroun/website-v2.git
```

Navigate into the project's directory
``` bash  
$ cd python_website 
```


Run this command to install dependencies
```bash
pip install -r requirements.txt
```
For pipenv run this command to install dependencies 
```bash
pipenv install 
```
This command will install all dependencies needed by the Akivas website to run successfully!

## Usage

Run the default laravel server
```bash
python manage.py runserver
```

To view Python Cameroon User group's Platform go to:
```bash
http://localhost:8000/
```

To view Python Cameroon's Platform dashboard go to:
```php
http://localhost:8000/admin/
```

OTHER

## 📖 Install
Make sure you have postgres install 
```
$ git clone https://github.com/Python-Cameroun/website-v2.git
$ cd python_website
$ pipenv install
$ pipenv shell

# Run Migrations
(python_website) $ python manage.py migrate

# Create a Superuser:
(python_website) $ python manage.py createsuperuser

# Confirm everything is working:
(python_website) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```