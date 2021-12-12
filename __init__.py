from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.read_full_ruletext import _read_full_ruletext
from .src.intents.read_all_details import _read_all_details


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
    @intent_handler(IntentBuilder('readFullRuletext')
        .require('theSpell')
        .one_of('ruletext', 'description', 'explanation', 'what', 'tellMeAbout')
        .optionally('spellname'))
    def handle_read_full_ruletext(self, message):
        _read_full_ruletext(self, message)

    # reads all details of spell to user
    @intent_handler(IntentBuilder('readAllDetails')
        .optionally('spellname')
        .require('detail')
        .require('theSpell')
        )
    def handle_read_all_details(self, message):
        _read_all_details(self, message)

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()


"""
        | Give me the details to the spell fireball                             |
        | Tell me all the details to the spell bless                            |
        | Read me the details to the spell burning hands                        |
        | Give me a detailed version of the spell confusion                     |
        | Tell me the detailed version for the spell create or destroy water    |
        | Read me the detailed version of the spell darkness                    |
        | details for the spell guardian of faith                               |
        | detailed version of the spell gust of wind                            |
        | detailed version for the spell heal                                   |
"""