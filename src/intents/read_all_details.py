from ..backend.spell_api_wrapper import Spell_api_wrapper
from ..backend.response_builder import build_response_all_details

def _read_all_details(self, message):
    spell_name_input = message.data.get('spellname')
    if spell_name_input is not None:
        spell_all_details = build_response_all_details(spell_name_input)

        if spell_all_details == 'empty':
            self.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name_input})
        else:
            self.speak_dialog('all.details', {'all_details': spell_all_details})
    else:
        self.speak_dialog('ruletext.fallback')

# ueberpruefe, name empty -> spell invalid
#
# different detail profile for spells