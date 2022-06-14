
import imp
from flask import Flask
from app import app
from user.models import User


@app.route("/register1", methods=['GET', 'PUT'])
def signup():
    return User().signup()
