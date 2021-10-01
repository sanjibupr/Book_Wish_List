from flaskapp.extensions import db

from .base import Base


class WishList(Base):
    r"""
    ORM class representing wishlist

    Parameters
    ----------
    id : int
        Primary key for the wish list. This is generated by postgres.
    user_id : int
        User id
    book_id : int
        User id
    created : datetime
        Generated by postgres.
    last_modified : datetime
        Generated by postgres.
    """

    __tablename__ = "wish_list"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("wl_user.user_id"))
    isbn = db.Column(db.String, db.ForeignKey("book.isbn"))
    created = db.Column(db.DateTime, server_default=db.func.now())
    last_modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.current_timestamp())

    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
