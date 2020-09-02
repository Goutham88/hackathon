from flask import request
from flask_httpauth import HTTPDigestAuth
from flask_restful import Resource, abort

from credentials import ACCESS_LIST, PASSWORD_MAP
from custom_exception import UnAuthorizedException, ValidationException

auth = HTTPDigestAuth()


class BaseController(Resource):
    def __new__(cls, *args, **kwargs):
        @auth.get_password  # decorator for flask http digest auth
        def get_pw(username):
            if username in ACCESS_LIST.get(request.endpoint):
                return PASSWORD_MAP.get(username)

        return object.__new__(cls)

    @auth.login_required  # decorator for flask http digest auth
    def dispatch_request(self, *args, **kwargs):
        try:
            return super(BaseController, self).dispatch_request(*args, **kwargs)
        except ValidationException as VE:
            # log the exception
            abort(400, message=str(VE))
        except UnAuthorizedException as AE:
            # log the exception
            abort(401, message=str(AE))
        except Exception as ex:
            # log the exception
            abort(500, message=str(ex))
