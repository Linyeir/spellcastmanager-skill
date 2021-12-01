from ..backend import spell_api_wrapper

def _read_all_details(self, message):
    spell_name_input = message.data.get('spellname')
    if spell_name_input is not None:
        spell_name = self.spell_api.get_detail()    #######
        if spell_name == 'empty':
            self.speak_dialog('ruletext.invalid.spell', {'spellname': spell_name_input})
        else:
            spell_range = self.spell_api.get_detail()
            spell_components = self.spell_api.get_detail()
            spell_material = self.spell_api.get_detail()
            spell_ritual = self.spell_api.get_detail()
            spell_duration = self.spell_api.get_detail()
            spell_concentration = self.spell_api.get_detail()
            spell_castingTime = self.spell_api.get_detail()
            spell_level = self.spell_api.get_detail()
            spell_damageType = self.spell_api.get_detail()
            spell_damage = self.spell_api.get_detail()          ### automatic lowest level besides user is asking?!?!?!
            spell_savingThrow = self.spell_api.get_detail()
            spell_areaOfEffectType = self.spell_api.get_detail()
            spell_size = self.spell_api.get_detail()
            spell_school = self.spell_api.get_detail()
    else:
        self.speak_dialog('ruletext.fallback')

# ueberpruefe, name empty -> spell invalid
#
