
# DB scheme : https://app.dbdesigner.net/designer/schema/435975

# Deployment

**Run these command in the root folder of the project:**
1) Create an environment

*macOs/Linux*

> $ python3 -m venv venv

 *Windows*

> $ py -3 -m venv venv

2) Activate the environment

*masOs/Linux*

> $ . venv/bin/activate

*Windows*

> venv\Scripts\activate

3) Install Flask

> $ pip install flask

4) Run The Migrations and Seeds

*bash*

> $ export FLASK_APP=app
$ export FLASK_ENV=development

*cmd*

> set FLASK_APP=app
> set FLASK_ENV=development


> $ flask init-db
$ flask seed

5) Run The Application

> $ flask run

# Docker
``` docker-compose up ```

# Result
**_first task_**

localhost:5000/auth/login (username: admin, password: 1234)


**_second task_**:

localhost:5000/sources/first

localhost:5000/sources/second

localhost:5000/sources/third

the result:
localhost:5000/sources/list

