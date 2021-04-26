# How to run locally

- Create a new virtual environment with the command ```python3 -m venv env```
- Activate it with ```$ source env/bin/activate``` (for linux and mac only)
- On the root folder run ```$ pip install -r requirements.txt```
- Navigate to the coachadmin folder and inside of it run: ```$ python3 manage.py runserver```

# How to run with gunicorn
- On the root folder run the following: ```$ gunicorn coachadmin.wsgi --chdir ./coachadmin

# Making requests

What you need to know is that there are 5 endpoints 
- ```coaches/``` Which you can hit with a ```GET``` request and returns all registered coaches in a list
- ```coaches/create/``` This is a ```POST``` request and needs a body with the following fields in JSON format: ```firstname```, ```lastName```, ```email```, ```phone``` and ```hobby```, all of these fields are strings and email has a built-in email validation. Your request body should look like this:
```
{
	"firstName": "Braulio",
	"lastName": "Jimenez",
	"email": "braulio@something.com",
	"phone": "120210299",
	"hobby": "Monster hunter"
}
```

- ```coaches/<id>/``` This gets you only one coach with the given Id and needs a ```GET``` request, for example: ```localhost:8000/coaches/1/``` will return the coach with the ID 1

- ```coaches/delete/<id>/``` Just like the past endpoint, except it deletes it with a ```DELETE``` request

- ```coaches/update/``` This last one is a ```PUT``` request and needs a matching email, right here you can send even a new email by adding the field ```newEmail``` in your request body. The body (if you want to change the email) would look something like this:
```
{
	"firstName": "Braulio",
	"lastName": "Jimenez",
	"email": "braulio@something.com",
	"phone": "120210299",
	"hobby": "Monster hunter",
    "newEmail": "test@test.com"
}
```

