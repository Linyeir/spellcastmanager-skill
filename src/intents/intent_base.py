from abc import ABC, abstractmethod
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError

class IntentBase(ABC):
    def _extract_spell_name(message):
        spell_name_input = message.data.get('spellname')
        if spell_name_input == None:
            raise NoSpellSpecifiedError
        else: 
            return spell_name_input

    @abstractmethod
    def execute(self, Spellcastmanager, message):
        pass