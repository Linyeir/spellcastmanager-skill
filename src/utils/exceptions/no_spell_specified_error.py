from .intent_exception import IntentException


class NoSpellSpecifiedError(IntentException):
    """raised when the user does not state a spell name

    Attributes:
            - _spell_name 	    -- the spell name, the user stated
            - _message	        -- description of exception
    """

    def __init__(self, spell_name='None', message="no spell name utterance detected"):
        self._spell_name = spell_name
        self._message = message
        super().__init__(self._message)
