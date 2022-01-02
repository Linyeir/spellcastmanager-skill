from typing import Optional
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from .src.intents.intent_get_spell_description import IntentGetSpellDescription
from .src.intents.intent_get_all_details import IntentGetAllDetails
from .src.intents.intent_get_single_detail import IntentGetSingleDetail


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

    # reads one detail of spell to user
    # For now:  Which 'range' does the spell 'fireball' have
    #           Is the spell 'alarm' a 'ritual'
    #           What 'damage' does the spell 'eldritch blast' at character level '1'
    @intent_handler(IntentBuilder('getSingleDetail')
        .optionally('spellname')
        .optionally('single_detail')    #rx
        .optionally('casting_level')    #rx
        .require('doesTheSpell')
        )
    def handle_get_single_detail(self, message):
        intent = IntentGetSingleDetail()
        intent.execute(self, message)

# name
# desc
# higher_level
# range
# components
# material
# ritual
# duration
# concentration
# casting_time
# level
# attack_type
# damage_type
# damage_slot
# damage_character
# heal_slot
# heal_character
# min_casting_level
# max_casting_level
# dc_type
# dc_success
# area_of_effect_type
# area_of_effect_size
# school

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()