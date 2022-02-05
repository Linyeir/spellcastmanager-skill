from .intent_base import IntentBase

class IntentChangeSettings(IntentBase):
    def __init__(self):
        self._fail_message_setting = 'This setting does not exist. Choose either language or title'
        self._fail_message_value = 'You need to give me something to work with'
        

    def execute(self, Spellcastmanager):
        """
        user calls intent themself
        """
        self._spellcastmanger = Spellcastmanager
        self._setting_to_change = self._spellcastmanger.get_response('which.setting', validator=self._validate_chosen_setting, on_fail=self._fail_message_setting, num_retries=3)
        if self._setting_to_change == None:
            self._spellcastmanger.speak_dialog('too.many.fails')
            return
        setting_value_input = self._spellcastmanger.get_response('which.setting.value', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
        if setting_value_input == None:
            self._spellcastmanger.speak_dialog('too.many.fails')
            return
        if setting_value_input == 'english':
            setting_value_input = 'en'
        self._spellcastmanger.settings[self._setting_to_change] = setting_value_input
        self._spellcastmanger.speak_dialog('alright')
        

    def execute_with_guide(self, Spellcastmanager):
        """
        spellcastmanager asks user to fill gaps
        """
        if Spellcastmanager.settings.get('language') == "":
            setting_value_input = Spellcastmanager.get_response('which.language', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
            if setting_value_input == 'english':
                setting_value_input = 'en'
            if setting_value_input == None:
                Spellcastmanager.speak_dialog('assume.setting.value', {'setting_value': 'en'})
            Spellcastmanager.settings['language'] = 'en'
        if Spellcastmanager.settings.get('title') == "":
            setting_value_input = Spellcastmanager.get_response('which.title', validator=self._validate_setting_value, on_fail=self._fail_message_value, num_retries=3)
            if setting_value_input == None:
                Spellcastmanager.speak_dialog('assume.setting.value', {'setting_value': 'oaf'})
                setting_value_input = 'oaf'
            Spellcastmanager.settings['title'] = setting_value_input


    def _validate_chosen_setting(self, response):
        if self._spellcastmanger.settings.get(response, False) == False:
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