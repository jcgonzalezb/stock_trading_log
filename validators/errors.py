#!/usr/bin/python3
# flask packages
from flask import Response, jsonify


def empty_data() -> Response:
    """
    This function will return an error message
    when the JSON provided is empty.
    """
    msg1 = "The JSON sent is empty."
    msg2 = "The information sent is not acceptable."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 406
    return resp


def forbidden_register() -> Response:
    """
    This function will return an error message when the user
    already exists.
    """
    msg1 = "The user already exists."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_new_user() -> Response:
    """
    This function will return an error message
    when an id is included in the JSON provided.
    """
    msg1 = "The id cannot be inserted."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_update_user() -> Response:
    """
    This function will return an error message when an id,
    email or password is included in the JSON provided.
    """
    msg1 = "The id, email or password cannot be updated."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def trade_not_found() -> Response:
    """
    This function will return an error message when the
    trade_id requested does not exist.
    """
    msg1 = "Trade could not be found."
    msg2 = "This route is currently not supported."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 404
    return resp


def forbidden() -> Response:
    """
    This function will return an error message when a trade_id,
    user_id or trade_status is included in the JSON provided.
    """
    msg1 = "The trade_id, user_id or trade_status values cannot be updated."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_new_trade() -> Response:
    """
    This function will return an error message when a trade_id or
    user_id is included in the JSON provided.
    """
    msg1 = "The trade_id or user_id cannot be inserted."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_status() -> Response:
    """
    This function will return an error message when current status of
    the trade is disable.
    """
    msg1 = "The trade_status cannot be changed."
    msg2 = "The current status of the trade is disable."
    msg3 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2 + ' ' + msg3}
    resp = jsonify(output)
    resp.status_code = 403
    return resp


def forbidden_trade() -> Response:
    """
    This function will return an error message when the current user tries
    to access the trade profile of another user.
    """
    msg1 = "The current user cannot access the trade profile of another user."
    msg2 = "The current user is not authorized to take this action."
    output = {"message": msg1 + ' ' + msg2}
    resp = jsonify(output)
    resp.status_code = 403
    return resp
