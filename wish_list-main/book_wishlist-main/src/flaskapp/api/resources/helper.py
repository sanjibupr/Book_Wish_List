from datetime import datetime

from flaskapp.api.models.books import Book
from flaskapp.api.models.user import User


def validate_user_id(user_id):
    try:
        if int(user_id) < 0:
            return "user_id must be int and bigger than 0"
    except ValueError:
        return "user_id must be int"

def validate(isbn, user_id):
    errors = []
    if not all([isbn, user_id]) or "None" in [isbn, user_id]:
        return [
            f"Both isbn and user_id are required - {isbn} {user_id}"
        ]
    user_id_error = validate_user_id(user_id)
    if user_id_error:
        errors.append(user_id_error)
    return errors

def is_book(isbn):
    return Book.query.filter(Book.isbn == isbn).first()

def is_user(user_id):
    return User.query.filter(User.user_id == user_id).first()
