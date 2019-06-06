# Heroku_
CRUD 과제를 Heroku로 배포하는 과제 레포지터리 입니다.


### 주요 명령어

#### Teminal
```bash
$ pip install gunicorn
$ pip install dj-database-url 
$ pip install psycopg2-binary
$ pip install whitenoise
$ pip freeze > requirements.txt
$ heroku login
$ heroku create
$ git push heroku master
$ heroku config:set DEBUG_COLLECTSTATIC=1
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku run python manage.py migrate
$ heroku open
$ heroku apps:rename
```

#### settings.py
```python
MIDDLEWARE = [
'whitenoise.middleware.WhiteNoiseMiddleware',
]

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

#### settings.py
[![현수쓰](/static/img/layout.JPG)]

#### url 주소
[![현수쓰](/static/img/logo.jpg)](https://khs9628board.herokuapp.com)
https://khs9628board.herokuapp.com

### 하루를 기록하다 :feet:
