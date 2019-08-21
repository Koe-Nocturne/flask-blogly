from unittest import TestCase
import models
from app import app
from flask import Flask, redirect, render_template, request


class RouteTestCase(TestCase):
    """testing routes"""

    def test_users_redirection(self):
        with app.test_client() as client:
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.location, "http://localhost/users")

    def test_users_redirection_followed(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>USERS</h1>', html)

    def test_edit_post_redirection(self):
        with app.test_client() as client:
            resp = client.post("/users/1/edit")
            # html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.location, "http://localhost/users")

    def test_new_post_redirection(self):
        with app.test_client() as client:
            resp = client.post("/users/new")
            # html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.location, "http://localhost/users")
