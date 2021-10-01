import logging

from flask import jsonify, request
from flask_restful import Resource
from flaskapp.api.models.wish_list import WishList
from flaskapp.extensions import db
from sqlalchemy import exc

from .error import validate_error
from .helper import is_book, is_user, validate, validate_user_id


class WishListResource(Resource):
    def get(self):
        """
        Get book wish list
        ---
        parameters:
        responses:
          200:
            description: Return list of books
          404:
            description: No book available
        """
        result = WishList.query.all()
        if not result:
            return validate_error("None books available in wish list", 404)
        response = jsonify([row.to_dict() for row in result])

        return response

    def post(self):
        """
        Add book to wish list
        ---
        parameters:
          - in: path
            name: isbn
            schema:
                type: string
            required: true
            description: isbn of the book
          - in: path
            name: user_id
            schema:
                type: int
            required: true
            description: user id
        responses:
          201:
            description: Add book to wish list
          400:
            description: Invalid request param
          404:
            description: Either user_id or isbn doesnt exists
        """
        isbn = request.args.get("isbn", None)
        user_id = request.args.get("user_id", None)
        errors = validate(isbn, user_id)
        if errors:
            logging.warning(errors)
            return validate_error(errors, 400)

        if not is_book(isbn):
            msg = f"isbn  - {isbn} doesnt exist"
            logging.warning(msg)
            return validate_error(msg, 404)

        if not is_user(user_id):
            msg = f"user_id - {user_id} doesnt exist"
            logging.warning(msg)
            return validate_error(msg, 404)

        try:
            result = WishList(isbn=isbn, user_id=user_id)
            db.session.add(result)
            db.session.commit()
        except exc.IntegrityError:
            msg = f"Fail to insert into db"
            return validate_error(msg, 400)
        return "Added", 201

    def put(self):
        """
        Update book wish list
        ---
        parameters:
          - in: path
            name: old_isbn
            schema:
                type: string
            required: true
            description: isbn of the book to be update
          - in: path
            name: new_isbn
            schema:
                type: string
            required: true
            description: isbn of the new book
          - in: path
            name: user_id
            schema:
                type: int
            required: true
            description: user id
        responses:
          201:
            description: Update book to wish list
          400:
            description: Invalid request param
          404:
            description: Either user_id or isbn doesnt exists
        """
        old_isbn = request.args.get("old_isbn", None)
        new_isbn = request.args.get("new_isbn", None)
        user_id = request.args.get("user_id", None)
        error = validate_user_id(user_id)
        if error:
            logging.warning(error)
            return validate_error(error, 400)

        if not is_book(old_isbn) or not is_book(new_isbn):
            return validate_error(
                f"Either old or new isbn {old_isbn} - {new_isbn} doesnt exist", 404
            )

        result = WishList.query.filter(WishList.isbn==old_isbn, WishList.user_id==user_id).first()
        if not result:
            result = WishList(isbn=new_isbn, user_id=user_id)
        try:
            result.isbn = new_isbn
            db.session.commit()
        except exc.IntegrityError:
            return validate_error(f"Fail to insert into db", 400)

        return "Updated", 200

    def delete(self):
        """
        Delete book from wish list
        ---
        parameters:
          - in: path
            name: isbn
            schema:
                type: string
            required: true
            description: isbn of the book
          - in: path
            name: user_id
            schema:
                type: int
            required: true
            description: user id
        responses:
          200:
            description: Add book to wish list
          400:
            description: Invalid request param
          404:
            description: Either user_id or isbn doesnt exists
        """
        isbn = request.args.get("isbn", None)
        user_id = request.args.get("user_id", None)
        error = validate_user_id(user_id)
        if error:
            logging.warning(error)
            return validate_error(error, 400)

        if isbn and isbn != "None" and not is_book(isbn):
            return validate_error(f"isbn  - {isbn} doesnt exist", 404)

        if not is_user(user_id):
            return validate_error(f"user_id - {user_id} doesnt exist", 404)

        try:
            WishList.query.filter_by(**request.args).delete()
            db.session.commit()
        except exc.IntegrityError:
            return validate_error(f"Fail to delete {request.args}", 400)

        return "Deleted", 200
