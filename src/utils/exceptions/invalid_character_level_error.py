from .intent_exception import IntentException


class InvalidCharacterLevelError(IntentException):
    """raised when an invalid character level was stated

    Attributes:
            - _character_level 	-- the stated level
            - _message	        -- description of exception
    """

    def __init__(self, character_level, message="the entered character level was not found"):
        self._character_level = character_level
        self._message = message
        super().__init__(self._message)
