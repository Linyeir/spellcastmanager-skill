from ..backend import spell_api_wrapper as spell_api

"""
 actually handles the full ruletext intent
 - the api is queried with the extracted spellname
 - the replied ruletext is spoken aloud
 - if the spell s not found or the api threw an error, the fallback is read instead
"""
def _read_full_ruletext(self, message):
        spell_name = message.data.get('spell')

        if spell_name is not None:
            ruletext = spell_api.get_full_ruletext(spell_name)
            if ruletext != 'empty':
                self.speak_dialog('long.ruletext', {'ruletext': ruletext})
            else:
                self.speak_dialog('ruletext.invalid.spell', {'spell_name', spell_name})
        else:
            self.speak_dialog('ruletext.fallback')