from .intent_exception import IntentException


class InvalidSpellCategoryError(IntentException):
    """raised when the details of a spell do not match any known category

    Attributes:
            - _details 		    -- details of the uncategorized spell
            - _message	        -- description of exception
    """

    def __init__(self, details, message="the spells details do not match any defined category"):
        self._details = details
        self._message = message
        super().__init__(self._message)