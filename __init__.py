from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.intent_get_spell_description import IntentGetSpellDescription
from .src.intents.intent_get_all_details import IntentGetAllDetails
from .src.intents.intent_invoke_casting_assistant import IntentInvokeCastingAssistant


class Spellcastmanager(MycroftSkill):

    # the constructor
    def __init__(self):
        super().__init__()
        self.learning = True

    # after-construction-initialisation
    def initialize(self):
        # read user setting
        my_setting = self.settings.get('my_setting')

    #-----------------------------------------------------
    # handlers

    @intent_file_handler('spellcastmanager.intent')
    def handle_spellcastmanager(self, message):
        self.speak_dialog('spellcastmanager')

    # reads the full ruletext to user
    @intent_handler(IntentBuilder('getSpellDescription')
        .require('theSpell')
        .one_of('ruletext', 'description', 'explanation', 'what', 'tellMeAbout')
        .optionally('spellname'))
    def handle_get_spell_description(self, message):
        intent = IntentGetSpellDescription()
        intent.execute(self, message)

    # reads all details of spell to user
    @intent_handler(IntentBuilder('getAllDetails')
        .optionally('spellname')
        .require('detail')
        .require('theSpell'))
    def handle_get_all_details(self, message):
        intent = IntentGetAllDetails()
        intent.execute(self, message)

    # guides user through casting
    @intent_handler(IntentBuilder('invokeCastinAssistant')
        .require('i')
        .require('cast')
        .optionally('spellname_cast'))
    def handle_invoke_casting_assistant(self, message):
        intent = IntentInvokeCastingAssistant()
        intent.execute(self, message)

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()