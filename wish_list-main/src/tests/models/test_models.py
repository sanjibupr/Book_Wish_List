import pytest
from flaskapp.api.models.books import Book
from flaskapp.api.models.user import User
from flaskapp.api.models.wish_list import WishList


@pytest.mark.parametrize(
    "mock_model, expected",
    [
        (Book(isbn="123-123", author="bogus"), 'Book: 123-123'),
        (User(user_id=1, first_name="Lane", last_name="bogus"), 'User: 1'),
        (WishList(user_id=1, isbn="123-123"), 'WishList: 1'),
    ],
)
def test_str_model(mock_model, expected):
    result = str(mock_model)
    assert result == expected

@pytest.mark.parametrize(
    "mock_model, expected",
    [
        (Book(isbn="123-123", author="bogus"), '<Book object name=123-123>'),
        (User(user_id=1, first_name="Lane", last_name="bogus"), '<User object name=1>'),
        (WishList(user_id=1, isbn="123-123"), '<WishList object name=1>'),
    ],
)
def test_repr_model(mock_model, expected):
    result = repr(mock_model)
    assert result == expected

def test_to_dict():
    wish_list = WishList(user_id=1, isbn="123-123")
    result = wish_list.to_dict()
    expected = {'user_id': 1, 'isbn': '123-123'}
    assert result == expected
