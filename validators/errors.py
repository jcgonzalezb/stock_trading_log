# flask packages
from flask import Response, jsonify


def trade_not_found() -> Response:
    msg1 = "Trade could not be found."
    msg2 = "This route is currently not supported."
    output = {"message": msg1 + msg2}
    resp = jsonify(output)
    resp.status_code = 404
    return resp


def forbidden() -> Response:
    msg1 = "The trade_id or user_id or trade_status values cannot be updated."
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


def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is currently not supported."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp
