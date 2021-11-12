from mycroft import MycroftSkill, intent_file_handler


class Spellcastmanager(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spellcastmanager.intent')
    def handle_spellcastmanager(self, message):
        self.speak_dialog('spellcastmanager')


def create_skill():
    return Spellcastmanager()

