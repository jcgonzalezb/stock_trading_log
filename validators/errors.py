# flask packages
from flask import Response, jsonify


def empty_data() -> Response:
    msg1 = "The JSON sent is empty."
    msg2 = "The information sent is not acceptable."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 406
    return resp


def forbidden_new_user() -> Response:
    msg1 = "The id cannot be inserted."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_update_user() -> Response:
    msg1 = "The id, email or password cannot be updated."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def trade_not_found() -> Response:
    msg1 = "Trade could not be found."
    msg2 = "This route is currently not supported."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 404
    return resp


def forbidden() -> Response:
    msg1 = "The trade_id, user_id or trade_status values cannot be updated."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_new_trade() -> Response:
    msg1 = "The trade_id or user_id cannot be inserted."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_status() -> Response:
    msg1 = "The trade_status cannot be changed."
    msg2 = "The trade_status is currently in disable."
    msg3 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2 + msg3}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_register() -> Response:
    msg1 = "The user already exist."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp
