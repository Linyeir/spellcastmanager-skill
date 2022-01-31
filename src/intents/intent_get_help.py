from pickle import TRUE
from .intent_base import IntentBase

class IntentGetHelp(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):
        terminate = False;

        user_response = Spellcastmanager.ask_selection(Spellcastmanager.help_intent_selection, 'help.get')
        while not terminate:
            if user_response == 'yes':
                user_response = Spellcastmanager.ask_selection(Spellcastmanager.help_intent_selection, 'help.which.one')
            else: 
                if user_response == 'no':
                    terminate = TRUE;
                elif user_response == 'option one':
                    Spellcastmanager.speak_dialog('help.option.one')
                elif user_response == 'option two':
                    Spellcastmanager.speak_dialog('help.option.two')
                elif user_response == 'option three':
                    Spellcastmanager.speak_dialog('help.option.three')
        Spellcastmanager.speak_dialog('help.terminate')
