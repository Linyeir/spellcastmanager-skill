from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.intent_get_spell_description import IntentGetSpellDescription
from .src.intents.intent_get_all_details import IntentGetAllDetails
from .src.intents.intent_get_all_details import IntentGetHelp


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
        .require('theSpell')
        )
    def handle_get_all_details(self, message):
        intent = IntentGetAllDetails()
        intent.execute(self, message)

    # reads help to the user (padatious)
    @intent_handler('get.help.intent')

    def handle_get_help(self, message):
        intent = IntentGetHelp()
        intent.execute(self, message)

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()