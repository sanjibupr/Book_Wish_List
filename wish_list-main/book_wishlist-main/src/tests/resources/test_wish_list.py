import pytest
from flaskapp.api.resources.helper import validate, validate_user_id


@pytest.mark.parametrize(
    "mock_isbn, mock_user_id, expected",
    [
        (None, None, ['Both isbn and user_id are required - None None']),
        ("123-123", None, ['Both isbn and user_id are required - 123-123 None']),
        (None, 1, ['Both isbn and user_id are required - None 1']),
        ("123-123", -4, ['user_id must be int and bigger than 0']),
        ("123-123", "bogus_val", ['user_id must be int']),
    ],
)
def test_validate(mock_isbn, mock_user_id, expected):
    result = validate(mock_isbn, mock_user_id)

    assert result == expected

@pytest.mark.parametrize(
    "mock_user_id, expected",
    [
        (-4, 'user_id must be int and bigger than 0'),
        ("bogus_val", 'user_id must be int'),
    ],
)
def test_validate_user_id(mock_user_id, expected):
    result = validate_user_id(mock_user_id)

    assert result == expected
