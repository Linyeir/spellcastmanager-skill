from ..backend.spell_api_wrapper import Spell_api_wrapper

def _read_all_details(self, message):
    spell_name_input = message.data.get('spellname')
    spell = Spell_api_wrapper(self, spell_name_input)
    if spell_name_input is not None:
        spell_name = spell.get_detail()    #######
        if spell_name == 'empty':
            self.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name_input})
        else:
            spell_range = spell.get_detail('range')
            spell_components = spell.get_detail('components')
            spell_material = spell.get_detail('material')
            spell_ritual = spell.get_detail('ritual')
            spell_duration = spell.get_detail('duration')
            spell_concentration = spell.get_detail('concentration')
            spell_castingTime = spell.get_detail('casting_time')
            spell_level = spell.get_detail('level')
            spell_damageType = spell.get_detail('desc')
            spell_damage = spell.get_detail('damage')                           # automatic lowest level besides user is asking?, Damage type?
            spell_savingThrow = spell.get_detail('school')                      # dc_type, dc_success
            spell_areaOfEffectType = spell.get_detail('area_of_effect[type]')   # not implemented yet
            spell_size = spell.get_detail('area_of_effect[size]')               # not implemented yet
            spell_school = spell.get_detail('desc')
    else:
        self.speak_dialog('ruletext.fallback')

# ueberpruefe, name empty -> spell invalid
#
