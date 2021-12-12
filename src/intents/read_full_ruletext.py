from ..response_builders.full_ruletext_response_builder import build_full_ruletext


"""
 actually handles the full ruletext intent
 - the ruletext builder provides the ruletext for the given spellname
 - the replied ruletext is spoken aloud
 - if the spell s not found or the api threw an error, the fallback is read instead
"""

def _read_full_ruletext(intent, message):
    spell_name = message.data.get('spellname')
    if spell_name is not None:
        ruletext = build_full_ruletext(spell_name)
        if ruletext != 'no spell':
                intent.speak_dialog('long.ruletext', {'ruletext': ruletext})
        else:
            intent.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name})
    else:
        intent.speak_dialog('ruletext.fallback')
