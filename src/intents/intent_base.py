from abc import ABC, abstractmethod
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from .intent_change_settings import IntentChangeSettings

class IntentBase(ABC):
    """
    base class for all intents
    defines basic interface
    """
    def _extract_spell_name(self, message):
        """
        returns extracted spell name from user input
        """
        spell_name_input = message.data.get('spellname')
        if spell_name_input == None:
            raise NoSpellSpecifiedError
        else: 
            return spell_name_input

    def _set_settings(self, Spellcastmanager):
        if Spellcastmanager.settings.get('language') == 'empty' or Spellcastmanager.settings.get('title') == 'empty':
            Spellcastmanager.speak_dialog('settings.empty')
            ics = IntentChangeSettings
            ics.execute_with_guide()
            return Spellcastmanager.settings.get('title')


    @abstractmethod
    def execute(self, Spellcastmanager, message):
        pass