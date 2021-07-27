# DB scheme : https://app.dbdesigner.net/designer/schema/435975
# Docker
``` docker-compose up ```

**_second task_**:
localhost:5000/sources/first

localhost:5000/sources/second

localhost:5000/sources/third

the result:
localhost:5000/sources/list

# Installing dependencies: 
_1) cd to the directory where requirements.txt is located.
2) activate your virtualenv.
3) run: pip install -r requirements.txt in your shell._

# Setting env
run this command in command line:

_set FLASK_APP=flaskr

set FLASK_ENV=development

# Run project
flask run

# Routes
http://localhost:5000/sources/list - get sorted array of data collected from sources
