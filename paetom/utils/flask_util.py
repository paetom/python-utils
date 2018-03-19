from flask import current_app


def res(code, message):
    response = current_app.make_response('{ "code" : %d, "message": "%s" }' % (code, message))
    response.headers['Content-Type'] = 'application/json'

    return response
