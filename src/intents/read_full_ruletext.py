from ..backend.spell_api_wrapper import Spell_api_wrapper

"""
 actually handles the full ruletext intent
 - the api is queried with the extracted spellname
 - the replied ruletext is spoken aloud
 - if the spell s not found or the api threw an error, the fallback is read instead
"""
def _read_full_ruletext(intent, message):
        spell_name = message.data.get('spellname')
        spell = Spell_api_wrapper(intent, spell_name)
        if spell_name is not None:
            key = ('desc',)
            ruletext = spell.get_detail(key)
            if ruletext != 'empty':
                intent.speak_dialog('long.ruletext', {'ruletext': ruletext})
            else:
                intent.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name})
        else:
            intent.speak_dialog('ruletext.fallback')