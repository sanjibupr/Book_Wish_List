import json

import pytest
from tests import mock_data as data

endpoint = "api/v1/book/wish_list"


@pytest.mark.parametrize(
    "user_id, isbn, expected_status_code, expected",
    [
        (None, "123-123", 400, data.expected_add_missing_user_id),
        ("1", None, 400, data.expected_add_missing_isbn),
        ("10", "123-123", 404, data.expected_add_invalid_user_id),
        ("1", "bogus_isbn", 404, data.expected_add_invalid_isbn),
        ("1", "123-123", 201, "Added"),
    ],
    ids=["missing_user_id", "missing_isbn", "invalid_user_id", "invalid_isbn", "good"],
)
def test_add_book(flask_client, user_id, isbn, expected_status_code, expected):
    result = flask_client.post(endpoint + f"?user_id={user_id}&isbn={isbn}")
    result_status_code = result.status_code
    result = json.loads(result.data)

    assert result_status_code == expected_status_code
    assert result == expected

@pytest.mark.parametrize(
    "user_id, isbn, expected_status_code, expected",
    [
        (None, "123-123", 400, data.expected_delete_missing_user_id),
        (None, None, 400, data.expected_delete_missing_user_id),
        ("13", None, 404, data.expected_delete_invalid_user_id),
        ("1", "123-123", 200, "Deleted"),
        ("1", None, 200, "Deleted"),
    ],
    ids=["missing_user_id", "missing_both", "invalid_user_id", "good", "good_with_only_user_id"],
)
def test_delete(flask_client, user_id, isbn, expected_status_code, expected):
    if isbn:
        url = endpoint + f"?user_id={user_id}&isbn={isbn}"
    else:
        url = endpoint + f"?user_id={user_id}"

    result = flask_client.delete(url)
    result_status_code = result.status_code
    result = json.loads(result.data)

    assert result_status_code == expected_status_code
    assert result == expected

@pytest.mark.parametrize(
    "user_id, old_isbn, new_isbn, expected_status_code, expected",
    [
        (None, "123-123", "123-345", 400, data.expected_delete_missing_user_id),
        (1, None, "123-345", 404, data.expected_put_missing_old_isbn),
        (1, "123-123", None, 404, data.expected_put_missing_new_isbn),
        (1, None, None, 404, data.expected_put_missing_isbn),
        (1, "123-123", "123-543", 200, "Updated"),
        (2, "123-123", "123-543", 200, "Updated"),
    ],
    ids=["missing_user_id", "missing_old_isbn", "missing_new_isbn", "invalid_isbn", "good", "insert_if_not_exists"],
)
def test_put(flask_client, user_id, old_isbn, new_isbn, expected_status_code, expected):
    url = endpoint + f"?user_id={user_id}&new_isbn={new_isbn}&old_isbn={old_isbn}"

    result = flask_client.put(url)
    result_status_code = result.status_code
    result = json.loads(result.data)
    assert result_status_code == expected_status_code
    assert result == expected
