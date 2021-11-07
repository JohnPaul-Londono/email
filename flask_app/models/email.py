from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Emails:
    def __init__( self, data ):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def validate_email(user_email):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        is_valid = True
        if not email_reg.match(user_email["email"]):
            flash("Invalid Email")
            is_valid = False
        return is_valid


    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL("email_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("email_schema").query_db(query)
        emails = []
        for email in results:
            emails.append(Emails(email))
            
        if len(results) < 1:
            return False

        return results

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL("email_schema").query_db(query,data)