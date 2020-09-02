class DBException(Exception):
    """
    If the connection with database can't be established
    """
    def __init__(self, msg="DataBase Exception occurred"):
        super(DBException, self).__init__(msg)


class UnAuthorizedException(Exception):
    """
    If the authentication error occurs
    """
    def __init__(self, msg="Authentication Exception occurred"):
        super(UnAuthorizedException, self).__init__(msg)


class ValidationException(Exception):
    """
    If a validation error occurs
    """
    def __init__(self, msg="Validation Exception occurred"):
        super(ValidationException, self).__init__(msg)
