from intent_exception import IntentException


class APINotReachableError(IntentException):
    """raised when api is not reachable

    Attributes:
            - _value 	-- http response
            - _message	-- description of exception
    """

    def __init__(self, value, message="The API does not answer your Requests"):
        self._value = value
        self._message = message
        super().__init__(self.message)
