from intent_exception import IntentException


class InvalidDetailError(IntentException):
    """raised when an invalid detail is stated

    Attributes:
            - _detail 	-- the stated detail
            - _message	-- description of exception
    """

    def __init__(self, detail, message="the specified detail was not found"):
        self._detail = detail
        self._message = message
        super().__init__(self.message)
