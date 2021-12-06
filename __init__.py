from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
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

    # starts spellcastmanager aka. sets the spellcastmanager context
    @intent_file_handler('startSpellcastmanager.intent')
    #@adds_context('Started')
    def start_handle_spellcastmanager(self, message):
        self.speak_dialog('spellcastmanager.started')

    # stopps spellcastmanager aka. removes the spellcastmanager context
    @intent_file_handler('stopSpellcastmanager.intent')
    #@removes_context('Started')
    def start_handle_spellcastmanager(self, message):
        self.speak_dialog('spellcastmanager.stopped')

    # reads the full ruletext to user
    @intent_handler(IntentBuilder('readFullRuletext')
        .require('theSpell')
        .one_of('ruletext', 'description', 'explanation', 'what', 'tellMeAbout')
        .optionally('spellname'))
        #.require('Started')
    def handle_read_full_ruletext(self, message):
        _read_full_ruletext(self, message)

    # reads the short ruletext to user
    @intent_handler(IntentBuilder('readShortRuletext')
        .require('short')
        .one_of('ruletext', 'description', 'explanation')
        .optionally('spell'))
        #.require('Started')
    def handle_read_short_ruletext(self, message):
        _read_short_ruletext(self, message)

    def stop(self):
        pass

def create_skill():
    return Spellcastmanager()