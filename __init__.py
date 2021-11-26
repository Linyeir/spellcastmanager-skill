from mycroft import MycroftSkill, intent_file_handler


class Spellcastmanager(MycroftSkill):

    # the constructor
    def __init__(self):
        super().__init__()
        self.learning = true

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
        .require('long')
        .require('ruletext')
        .require('Spell'))
    def handle_read_full_ruletext(self, message):
        spell = message.data.get('Spell')
        if spell is not None:
            self.speak_dialog('read.long.ruletext', {'Spell': spell})
        else:
            self.speak_dialog('read.ruletext.fallback')

    def stop(self):
        pass


def create_skill():
    return Spellcastmanager()



 

