from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO users (name,location,language,comment)
                    VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_user(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, {"id":id})
        return cls(result[0])


    @staticmethod
    def validate(data):

        is_valid = True

        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False

        if len(data['location']) < 1:
            flash("Please select a location")
            is_valid = False

        if len(data['language']) < 1:
            flash("Please select a language")
            is_valid = False

        if len(data['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False

        return is_valid