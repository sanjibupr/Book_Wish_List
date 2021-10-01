from flask import jsonify


def validate_error(message, status):
    response = jsonify({"error": message})
    response.status_code = status
    return response
