from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.read_full_ruletext import _read_full_ruletext
from .src.intents.read_short_ruletext import _read_short_ruletext


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

    # reads the short ruletext to user
    @intent_handler(IntentBuilder('readShortRuletext')
        .require('short')
        .one_of('ruletext', 'description', 'explanation')
        .optionally('spell'))
    def handle_read_short_ruletext(self, message):
        _read_short_ruletext(self, message)

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()