from .intent_exception import IntentException


class InvalidSpellError(IntentException):
    """raised when invalid spell name is given

    Attributes:
            - _spell_name 		-- the stated spell name
            - _message	        -- description of exception
    """

    def __init__(self, spell_name, message="the entered spell name was not found"):
        self._spell_name = spell_name
        self._message = message
        super().__init__(self._message)
