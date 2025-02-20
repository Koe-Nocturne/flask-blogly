from unittest import TestCase
import models
from app import app
from flask import Flask, redirect, render_template, request


class RouteTestCase(TestCase):
    """testing routes"""

    def test_home_redirection(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=False)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/users")

    def test_users_redirection_followed(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>USERS</h1>', html)

    def test_edit_post_redirection(self):
        with app.test_client() as client:
            resp = client.post("/users/1/edit", data={"first-name": "bob", "last-name": "joe"})
            # html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,  302)
            self.assertEqual(resp.location, "http://localhost/users")

    def test_new_post_redirection(self):
        with app.test_client() as client:
            resp = client.post("/users/new",
            data={"first-name": "bob", "last-name": "joe"})
            # html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/users")



    def test_edit_redirection(self):
       with app.test_client() as client:
            resp = client.post("/posts/1/edit", data={"title": "bob", "content": "billy-joe-bob"})

            self.assertEqual(resp.status_code,  302)
            self.assertEqual(resp.location, "http://localhost/posts/1")

    def test_users_redirection_followed(self):
        with app.test_client() as client:
            resp = client.get("/posts/1/edit", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p>by', html)

    # def test_edit_post_redirection(self):
    #     with app.test_client() as client:
    #         resp = client.post("/users/1/edit", data={"first-name": "bob", "last-name": "joe"})
    #         # html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code,  302)
    #         self.assertEqual(resp.location, "http://localhost/users")

    # def test_new_post_redirection(self):
    #     with app.test_client() as client:
    #         resp = client.post("/users/new",
    #         data={"first-name": "bob", "last-name": "joe"})
    #         # html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 302)
    #         self.assertEqual(resp.location, "http://localhost/users")
   