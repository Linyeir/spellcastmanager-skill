from typing import Optional
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.intent_get_spell_description import IntentGetSpellDescription
from .src.intents.intent_get_all_details import IntentGetAllDetails
from .src.intents.intent_invoke_casting_assistant import IntentInvokeCastingAssistant
from .src.intents.intent_get_single_detail import IntentGetSingleDetail
from .src.intents.intent_get_help import IntentGetHelp
from .src.intents.intent_change_settings import IntentChangeSettings


class Spellcastmanager(MycroftSkill):

    # the constructor
    def __init__(self):

        super().__init__()
        self.learning = True

    # after-construction-initialisation
    def initialize(self):
        # read user setting
        self._language = self.settings.get('language')
        self._title = self.settings.get('title')

    def set_settings(self):
        if self.settings.get('language') == "" or self.settings.get('title') == "":
            ics = IntentChangeSettings()
            ics.execute_if_not_set(self)
            return self.settings.get('title')

    # -----------------------------------------------------
    # handlers

    @intent_file_handler('spellcastmanager.intent')
    def handle_spellcastmanager(self, message):
        self.speak_dialog('spellcastmanager')

    @intent_handler('change.settings.intent')
    def handle_change_settings(self):
        intent = IntentChangeSettings()
        intent.execute(self)

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
                    .require('theSpell')
                    .optionally('spellname'))
    def handle_invoke_casting_assistant(self, message):
        intent = IntentInvokeCastingAssistant(self._language)
        intent.execute(self, message)

   # reads single detail of spell to user

    @intent_handler(IntentBuilder('getSingleDetail')
                    .optionally('spellname')
                    .require('theSpell')
                    .require('want')
                    .require('information')
                    )
    def handle_get_single_detail(self, message):
        intent = IntentGetSingleDetail()
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
