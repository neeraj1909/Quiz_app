# Online Quiz App in Django
*TODO: Add a short description of this project.*

### Getting started with development
Dependenciies:
- Python 3.6.x
- Django 1.11.x
- MySQL 5.7.x
- Ubuntu 17.04 or later

#### 1. Clone this repoistory
```bash
git clone git@github.com:neeraj1909/quiz_app.git
cd quiz_app
```

#### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

#### 3. Create the virtualenv
```bash
## run following command from `quiz_app` directory
mkvirtualenv quiz_app -a "$(pwd)" -p python3.6
```

#### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step
workon quiz_app
pip install -r requirements.txt
```

#### 5. Setup the database
*TODO - Add instructions for this when we start using MySQL database.*

#### 6. Run database migrations
```bash
python manage.py migrate
```

#### 7. Import initial data
```bash
## open Django shell
python manage.py shell
```

Run following command inside the python shell
```python
%run scripts/initialize_data.py
```


#### 8. Run development server
```bash
python manage.py runserver
```
