import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class CastingTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "betadb"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.sample_actor = {
            'name': 'Denzel Hayes Washington',
            'gender': 'male',
            'age': 66
        }

        self.sample_movie = {
            'title': 'Titanic',
            'release': '19/12/1997'
        }

        self.sample_movie_ = {
            'title': 'Titanic3',
            'release': '19/12/2002'
        }

        self.casting_assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI1NDk4MjM1Mzg0ODM1MjI4MDQiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTU2MjIsImV4cCI6MTU5ODE4MjAyMiwiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.lJhb2sx6P19i2boh1SLcvSfTgeD5EtStr7mZjgyRGMDzyMTDu3JqOzHZp7mm2NbbJNS3ae8mswDzhqkAARURjOr6CHi8s39HQUbE4xCfNIdsiw1XLMVFaqiUs84rO1XTXNwRb3tjjXmtyccvKvItDbFGD40XZ3NrXpcW2PqNyE2Fj3CHTQ6N6TXNSehhvOpGc9cotopOBl3jmQRBR4EWkzipNKi89YwBvWC4TcYBaKNPJIwHTF0yllRjuM3frafslBk48Nsg6e6bcYyfwqdqorxF0TV0pHQ7NHL1a3KwHcYCP01mQehmjxzKCeBHErKzApNVN5-j8J6gyAb-IIb2GQ"
        self.casting_director_token = "access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQwNTQwODM1MTIyNjQ3MzE2OTMiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTU1MjMsImV4cCI6MTU5ODE4MTkyMywiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.Jmfius8HU3l7_XVdipz3ko-d4sXNPKSzwGmEYARwPKocaqgQvnfS-oUtYX-kSN4oeF_nuJiyGDc6keP-gENbMV9MAGz6oRxQrtZhoM_y8tPE37wqjS6-VHXjhXI3O1jecjZD5wpw5WAT7rAQuxuYfNF5rTAmQh3RkkWbpx_DYV093AkR8cjXPBKrs0eRDS7TkDLiwmtX-RDDxxPHRpn7qXgwVHo1S4w_FQQjBzUVH6zRa1Rk-YMGXVGKfJqGJB6aPfm39N6qTdQv82XwcI2YdT_6WZjYQhlnPpxsRCO2BokVfyjq0NJafUkJZ1qNzh6WXq2HsmQnY4Na0xDh05rVvg"
        self.executive_producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI1NDk4MjM1Mzg0ODM1MjI4MDQiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTgwOTUzOTcsImV4cCI6MTU5ODE4MTc5NywiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.N4SFoL0ffnMMkWR2-fwzLCHOWGQhd-uqm57fiyduE_LPJmH2WqgtzUEtUaaEa6-TxAxKHZGm2QwWt7tWXFHpSFdiglTUF3d3wRA0NcIaxBqmS_QZxtY1vZS1v55RyAlS5cgln5A8pNDOX4j-PI8QtgJ1KJkbN4CwOiiOo57Vp6jzmScACx_i5kVuIeMl79Yip_TCJqcvMVAzVhjfVcuFILVeVAQoM5-z2cP0GGYYpEe7rDkZSOFxB_vZoxuEGVJnQXgnSySrLTRioQghGQ2aSXjN1izvN2b9q-RC9n7h-kGh98e4tudzNuklEXswdhl-wopCafH23l0Ubwo8v0IDyw"

    def tearDown(self):
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_actorsـunauthorized(self):
        response = self.client().get('/actors')

        self.assertEqual(response.status_code, 401)

    def test_get_actorsـauthorized(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000/actors',
            'user_token',
            self.executive_producer_token)
        response = c.get('/actors')

        self.assertEqual(response.status_code, 200)

    def test_get_moviesـunauthorized(self):
        response = self.client().get('/movies')

        self.assertEqual(response.status_code, 401)

    def test_get_moviesـauthorized(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000/movies',
            'user_token',
            self.executive_producer_token)
        response = c.get('/movies')

        self.assertEqual(response.status_code, 200)

    def test_post_movies_unauthorized(self):
        c = self.client()
        response = c.post(
            '/actors',
            data=dict(title="The godfather", release="14/03/1972"),
        )

        self.assertEqual(response.status_code, 401)

    def test_post_movies_authorized(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000/movies',
            'user_token',
            self.executive_producer_token)
        response = c.post(
            '/movies',
            data=dict(title="The godfathers", release="14/03/1973"),
        )

        self.assertEqual(response.status_code, 200)

    def test_post_actors_unauthorized(self):
        c = self.client()
        response = c.post(
            '/actors',
            data=dict(name="Denzel Hayes Washington", age=66, gender="Male"),
        )

        self.assertEqual(response.status_code, 401)

    def test_post_actors_authorized(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000/movies',
            'user_token',
            self.executive_producer_token)
        response = c.post(
            '/actors',
            data=dict(name="Denzel Hayes Washington", age=66, gender="Male"),
        )

        self.assertEqual(response.status_code, 200)

    def test_patch_movieـauthorized(self):
        movie = Movie(
            title=self.sample_movie_['title'],
            release=self.sample_movie_['release'])
        movie.insert()
        movie_id = movie.id

        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.executive_producer_token)
        response = c.post(
            f'/movies/{movie_id}/patch',
            data=dict(title="Titanic2", release="01/01/2000"))

        self.assertEqual(response.status_code, 200)

    def test_patch_movieـunauthorized(self):

        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.casting_assistant_token)
        response = c.post(
            f'/movies/{2}/patch',
            data=dict(name="Titanic2", release="01/01/2000"),
        )

        self.assertEqual(response.status_code, 401)

    def test_delete_movieـunauthorized(self):
        movie = Movie(
            title=self.sample_movie['title'],
            release=self.sample_movie['release'])
        movie.insert()
        movie_id = movie.id

        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.casting_director_token)
        response = c.get(f'/movies/{movie_id}/delete')

        self.assertEqual(response.status_code, 401)

    def test_delete_movie_not_found(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.executive_producer_token)
        response = c.get('/movies/1845858/delete')

        self.assertEqual(response.status_code, 401)

    def test_delete_actor_not_found(self):
        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.executive_producer_token)
        response = c.get('/actors/14877488/delete')

        self.assertEqual(response.status_code, 401)

    def test_delete_movieـauthorized(self):
        movie = Movie(
            title=self.sample_movie['title'],
            release=self.sample_movie['release'])
        movie.insert()
        movie_id = movie.id

        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.executive_producer_token)
        response = c.get(f'/movies/{movie_id}/delete')

        self.assertEqual(response.status_code, 200)

    def test_delete_actorـauthorized(self):
        actor = Actor(
            name=self.sample_actor['name'],
            age=self.sample_actor['age'],
            gender=self.sample_actor['gender'])
        actor.insert()
        actor_id = actor.id

        c = self.client()
        c.set_cookie(
            'localhost:5000',
            'user_token',
            self.executive_producer_token)
        response = c.get(f'/actors/{actor_id}/delete')

        self.assertEqual(response.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
