from .intent_exception import IntentException


class InvalidSpellSlotLevelError(IntentException):
    """raised when an invalid spellslot level was stated

    Attributes:
            - _spellslot_levell -- the stated level
            - _message	        -- description of exception
    """

    def __init__(self, spellslot_level, message="the entered spellslot level was not found"):
        self._spellslot_level = spellslot_level
        self._message = message
        super().__init__(self._message)
