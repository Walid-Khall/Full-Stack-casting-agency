
## Motivation
After two months of hard work with brilliant instructors of Udacity Full Stack Web Developer (NANODEGREE PROGRAM). I devloped this project from scratch to make use of the knowledge acquired in this nanodegree. The project name is Casting Agency which is a company that is responsible for creating movies and managing and assigning actors to those movies.

# Models: (models.py)
Movies with attributes title and release date
Actors with attributes name, age and gender

# Endpoints: (app.py)

@app.errorhandler decorators were used to format error responses as JSON objects. Custom @requires_auth decorator were used for Authorization based
on roles of the user. 

#### GET /actors 

Returns a list of all the movies and a success value.

{
  "actors": [
    {
      "age": 66,
      "gender": "Male",
      "id": 37,
      "name": "Denzel Hayes Washington"
    }
  ],
  "success": true
}

### GET/movies

Returns a list of all the movies and a success value.

{
  "movies": [
    {
      "id": 56,
      "release": "19/12/1997",
      "title": "Titanic"
    },
    {
      "id": 57,
      "release": "01/01/2000",
      "title": "Titanic2"
    },
    {
      "id": 58,
      "release": "14/03/1973",
      "title": "The godfathers"
    }
  ],
  "success": true
}

### POST /actors 
Returns the new actor posted and a success value.

{
  "actors": {
    "age": 29,
    "gender": "homme",
    "id": 38,
    "name": "Walid"
  },
  "success": true
}

### POST/movies
Returns the new movie posted and a success value.

{
  "movie": {
    "id": 59,
    "release": "14/03/2008",
    "title": "Iron Man"
  },
  "success": true
}




### DELETE /actors
Returns the delted ID and a success value:

{
  "delete": "38",
  "success": true
}


### DELETE /movies
Retuens the deleted ID and a success value:

{
  "delete": "59",
  "success": true
}

### PATCH /actors
Retuen the updates actor and a success value:

{
  "actor": {
    "age": 56,
    "gender": "Male",
    "id": 37,
    "name": "Denzel Hayes Washington"
  },
  "success": true
}

### PATCH /movies
Retuen the updated movie and a success value:

{
  "movie": {
    "id": 56,
    "release": "19/12/2002",
    "title": "Titanic 2"
  },
  "success": true
}


# Roles: (auth.py)
Three roles are assigned to this API: 'Casting Assistant', 'Casting Director' and 'Executive Producer'.

1. Casting Assistant
   - Can view actors and movies

2. Casting Director
   - All permissions a Casting Assistant has and…
   - Add or delete an actor from the database
   - Modify actors or movies

3. Executive Producer
   - All permissions a Casting Director has and…
   - Add or delete a movie from the database

# Tests: (unit_test.py)
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role



## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
pip install virtualenv
```
Creating virtual environments

```bash
python3 -m venv
```
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:


On Linux : export

```bash
export FLASK_APP=app.py;
```

On Windows : set

```bash
set FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

# URL where the application is hosted

https://udacity-fsdn-capstone-project.herokuapp.com/


### Setup Auth0 here is the access tokens 

# Casting Assistant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI1NDk4MjM1Mzg0ODM1MjI4MDQiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTU2MjIsImV4cCI6MTU5ODE4MjAyMiwiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.lJhb2sx6P19i2boh1SLcvSfTgeD5EtStr7mZjgyRGMDzyMTDu3JqOzHZp7mm2NbbJNS3ae8mswDzhqkAARURjOr6CHi8s39HQUbE4xCfNIdsiw1XLMVFaqiUs84rO1XTXNwRb3tjjXmtyccvKvItDbFGD40XZ3NrXpcW2PqNyE2Fj3CHTQ6N6TXNSehhvOpGc9cotopOBl3jmQRBR4EWkzipNKi89YwBvWC4TcYBaKNPJIwHTF0yllRjuM3frafslBk48Nsg6e6bcYyfwqdqorxF0TV0pHQ7NHL1a3KwHcYCP01mQehmjxzKCeBHErKzApNVN5-j8J6gyAb-IIb2GQ


# Casting Director

access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQwNTQwODM1MTIyNjQ3MzE2OTMiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTU1MjMsImV4cCI6MTU5ODE4MTkyMywiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.Jmfius8HU3l7_XVdipz3ko-d4sXNPKSzwGmEYARwPKocaqgQvnfS-oUtYX-kSN4oeF_nuJiyGDc6keP-gENbMV9MAGz6oRxQrtZhoM_y8tPE37wqjS6-VHXjhXI3O1jecjZD5wpw5WAT7rAQuxuYfNF5rTAmQh3RkkWbpx_DYV093AkR8cjXPBKrs0eRDS7TkDLiwmtX-RDDxxPHRpn7qXgwVHo1S4w_FQQjBzUVH6zRa1Rk-YMGXVGKfJqGJB6aPfm39N6qTdQv82XwcI2YdT_6WZjYQhlnPpxsRCO2BokVfyjq0NJafUkJZ1qNzh6WXq2HsmQnY4Na0xDh05rVvg


# Executive Producer


eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI1NDk4MjM1Mzg0ODM1MjI4MDQiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTUzOTcsImV4cCI6MTU5ODE4MTc5NywiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.N4SFoL0ffnMMkWR2-fwzLCHOWGQhd-uqm57fiyduE_LPJmH2WqgtzUEtUaaEa6-TxAxKHZGm2QwWt7tWXFHpSFdiglTUF3d3wRA0NcIaxBqmS_QZxtY1vZS1v55RyAlS5cgln5A8pNDOX4j-PI8QtgJ1KJkbN4CwOiiOo57Vp6jzmScACx_i5kVuIeMl79Yip_TCJqcvMVAzVhjfVcuFILVeVAQoM5-z2cP0GGYYpEe7rDkZSOFxB_vZoxuEGVJnQXgnSySrLTRioQghGQ2aSXjN1izvN2b9q-RC9n7h-kGh98e4tudzNuklEXswdhl-wopCafH23l0Ubwo8v0IDyw


## DATA MODELING:(MODELS.PY)

The schema for the database and helper methods to simplify API behavior are in models.py:

There are two tables created: Actor and Movie

The Actor table has four columns (id, name, age and gender)

The Movie table has three columns (id, title, release)

Each table has an insert, update, delete, and format helper functions.



## Testing
There are 16 unittests in test_app.py. To run this file use:
```
python unit_test.py
```
The tests include one test for expected success and error behavior for each endpoint, and tests demonstrating role-based access control, 
where all endpoints are tested with and without the correct authorization.



# DEPLOYMENT
The app is hosted live on heroku at the URL: 

https://casting-agency-app-capstone.herokuapp.com/

### test the application live

Go to the 
Click on Login / sing in with Google / use another account
enter the following credentials  which has been designated with Executive Producer role:


