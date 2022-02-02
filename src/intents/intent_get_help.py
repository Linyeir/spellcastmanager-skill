from pickle import TRUE
from .intent_base import IntentBase

class IntentGetHelp(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):
        Spellcastmanager.speak_dialog('help.get')

        options = ['You can generally ask about a specific spell',
                    'You can ask for specific details regarding a spell.',
                    'You can ask for all details i have about a spell',
                    'The spellcast manager can guide you through the casting of a specific spell']

        selection = Spellcastmanager.ask_selection(options, 'help.post.option')

        if selection == 'You can generally ask about a specific spell':
            Spellcastmanager.speak_dialog('help.option.all')        
        elif selection == 'You can ask for specific details regarding a spell.':
            Spellcastmanager.speak_dialog('help.option.assistant')
        elif selection == 'You can ask for all details i have about a spell':
            Spellcastmanager.speak_dialog('help.option.description')            
        elif selection == 'The spellcast manager can guide you through the casting of a specific spell':
            Spellcastmanager.speak_dialog('help.option.detail')

