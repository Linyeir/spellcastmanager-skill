from .intent_base import IntentBase


class IntentChangeSettings(IntentBase):
    def __init__(self):
        self._fail_message_setting = 'This setting does not exist. Choose either language or title'
        self._fail_message_value = 'You need to give me something to work with'

    def execute(self, Spellcastmanager, message):
        """
        user calls intent themselves
        """
        self._spellcastmanager = Spellcastmanager
        self._setting_to_change = self._spellcastmanager.get_response(
            'which.setting', validator=self._validate_chosen_setting, on_fail=self._fail_message_setting, num_retries=3)
        if self._setting_to_change == None:
            self._spellcastmanager.speak_dialog('too.many.fails')
            return
        setting_value_input = self._spellcastmanager.get_response(
            'which.setting.value', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
        if setting_value_input == None:
            self._spellcastmanager.speak_dialog('too.many.fails')
            return
        if setting_value_input == 'english':
            setting_value_input = 'en'
        self._spellcastmanager.settings[self._setting_to_change] = setting_value_input
        self._spellcastmanager.speak_dialog('alright', {'title': self._spellcastmanager.settings['title']})
        self._spellcastmanager.speak_dialog('acknowledge.settings', {'title': self._spellcastmanager.settings['title'], 'language': 'english'})

    def execute_if_not_set(self, Spellcastmanager):
        """
        spellcastmanager forces user to provide 'necessary'
        """
        Spellcastmanager.speak_dialog('settings.empty')
        if Spellcastmanager.settings.get('language') == "":
            self._setting_to_change = 'language'
            setting_value_input = Spellcastmanager.get_response(
                'which.language', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
            if setting_value_input == 'english':
                setting_value_input = 'en'
            if setting_value_input == None:
                Spellcastmanager.speak_dialog(
                    'assume.setting.value', {'setting_value': 'en'})
            Spellcastmanager.settings['language'] = 'en'
        if Spellcastmanager.settings.get('title') == "":
            self._setting_to_change = 'title'
            setting_value_input = Spellcastmanager.get_response(
                'which.title', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
            if setting_value_input == None:
                Spellcastmanager.speak_dialog('assume.setting.value', {
                                              'setting_value': 'oaf'})
                setting_value_input = 'Oaf'
            Spellcastmanager.settings['title'] = setting_value_input
        Spellcastmanager.speak_dialog('acknowledge.settings', {'title': Spellcastmanager.settings['title'], 'language': 'english'})

    def _validate_chosen_setting(self, response):
        if self._spellcastmanager.settings.get(response, False) == False:
            return False
        return True

    def _validate_setting_value(self, response):
        if response == None:
            return False
        if self._setting_to_change == 'language' and response != 'english':
            self._fail_message_value = 'This language is not availaible. You can choose one of the following. English'
            return False
        return True


# durch settings geleitet werden

# selber intent aufrufen
