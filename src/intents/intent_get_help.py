from pickle import TRUE
from .intent_base import IntentBase

class IntentGetHelp(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):
        terminate_help = False;
        Spellcastmanager.speak_dialog('help.get')

        while not terminate_help:

            options = ['You can generally ask about a specific spell',
                        'You can ask for specific details regarding a spell.',
                        'You can ask for all details i have about a spell',
                        'The spellcast manager can guide you through the casting of a specific spell']

            selection = Spellcastmanager.ask_selection(options, 'help.post.option')

            if selection == options[0]:
                Spellcastmanager.speak_dialog('help.option.all')        
            elif selection == options[1]:
                Spellcastmanager.speak_dialog('help.option.assistant')
            elif selection == options[2]:
                Spellcastmanager.speak_dialog('help.option.description')            
            elif selection == options[3]:
                Spellcastmanager.speak_dialog('help.option.detail')

            further_help = Spellcastmanager.ask_yesno('help.continue') 

            if further_help == 'no':
                  terminate_help = True

        Spellcastmanager.speak_dialog('help.terminate')