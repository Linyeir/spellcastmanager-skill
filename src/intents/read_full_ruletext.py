from ..backend.response_builder import build_response_get_single_detail

"""
 actually handles the full ruletext intent
 - the api is queried with the extracted spellname
 - the replied ruletext is spoken aloud
 - if the spell s not found or the api threw an error, the fallback is read instead
"""

def _read_full_ruletext(intent, message):
    spell_name = message.data.get('spellname')
    if spell_name is not None:
        key = ('desc',)
        ruletext = build_response_get_single_detail(spell_name, key)
        if ruletext != 'empty':
                intent.speak_dialog('long.ruletext', {'ruletext': ruletext})
        else:
            intent.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name})
    else:
        intent.speak_dialog('ruletext.fallback')
