import imp
from flask import Flask, jsonify, redirect, request, session
import uuid
#from app import mongo_db
from requests import session


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        # Create user object
        user = {
            "_id": uuid.uuid4().hex,
            # "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        return jsonify(user), 200

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = list(mongo_db.get_collection('users').find_one(
            {"user": request.form.get('email')}))
        if user:
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"})
