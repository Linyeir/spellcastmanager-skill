'''
def _read_short_ruletext(self, message):
        spell = message.data.get('spell')
        if spell is not None:
            self.speak_dialog('short.ruletext', {'spell': spell})
        else:
            self.speak_dialog('ruletext.fallback')




from ..backend import spell_api_wrapper as spell_api

"""
 actually handles the full ruletext intent
 - the api is queried with the extracted spellname
 - the replied ruletext is spoken aloud
 - if the spell s not found or the api threw an error, the fallback is read instead
"""
def _read_full_ruletext(self, message):
        spell_name = message.data.get('spellname')
        if spell_name is not None:
            ruletext = spell_api.get_full_ruletext(spell_name)
            if ruletext != 'empty':
                self.speak_dialog('long.ruletext', {'ruletext': ruletext})
            else:
                self.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name})
        else:
            self.speak_dialog('ruletext.fallback')

'''