from abc import ABC, abstractmethod

class IntentBase(ABC):
    @abstractmethod
    def extract_spell_name(message):
        pass

    @abstractmethod
    def execute(Spellcastmanager, message):
        pass