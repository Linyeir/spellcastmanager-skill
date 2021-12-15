from abc import ABC, abstractmethod

class IntentBase(ABC):
    def _extract_spell_name(message):
        spell_name_input = message.data.get('spellname')
        if spell_name_input == None:
            raise 'no spell name stated'
        else: 
            return spell_name_input

    @abstractmethod
    def execute(self, Spellcastmanager, message):
        pass