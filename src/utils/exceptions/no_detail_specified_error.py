from intent_exception import IntentException


class NoDetailSpecifiedError(IntentException):
    """raised when the user does not state a detail name

    Attributes:
            - _spell_name 	    -- the spell name, the user stated
            - _message	        -- description of exception
    """

    def __init__(self, spell_name, message="no detail utterance detected"):
        self._spell_name = spell_name
        self._message = message
        super().__init__(self.message)
