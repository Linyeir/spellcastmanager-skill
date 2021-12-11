from requests.models import Response
from Spell_class import Spell_class


def build_response_all_details(spell_name_in):
    spell = Spell_class(spell_name_in)
    response = ''

    # remove if statements from not optional attributes? which ones are not optional?

    if spell.name is 'empty':
        return 'empty'
    else:
        response = 'Name ' + spell.name + '\n'
    
        if spell.higher_level is not 'empty':
            response = response + 'Changes for higher levels ' + spell.higher_level + '\n'

        if spell.range is not 'empty':
            response = response + 'Range ' + spell.range + '\n'

        if spell.components is not 'empty':
            response = response + 'Components ' + spell.components + '\n'

        if spell.material is not 'empty':
            response = response + 'Material ' + spell.material + '\n'

        if spell.ritual is not 'empty':        # what type is ritual?
            if spell.ritual is True:
                response = response + 'Is a ritual\n'
            if spell.ritual is False:
                response = response + 'Is not a ritual\n'

        if spell.duration is not 'empty':
            response = response + 'Spell duration ' + spell.duration + '\n'
            
        if spell.concentration is not 'empty':
            if spell.concentration is True:
                response = response + 'Concentration yes\n'
            if spell.concentration is False:
                response = response + 'Concentration no\n'

        if spell.casting_time is not 'empty':
            response = response + 'Casting time ' + spell.casting_time + '\n'

        if spell.level is not 'empty':
            response = response + 'Level ' + spell.level + '\n'

        if spell.attack_type is not 'empty':
            response = response + 'Attack type ' + spell.attack_type + '\n'

        if spell.damage_type is not 'empty':
            response = response + 'Damage type ' + spell.damage_type + '\n'
            
        if spell.damage_at_slot_level is not 'empty':
            response = response + 'Damage at lowest slot level ' + spell.damage_at_slot_level[0] + '\n'

        if spell.heal_at_slot_level is not 'empty':
            response = response + 'Healing at lowest slot level ' + spell.heal_at_slot_level[0] + '\n'

        if spell.damage_at_character_level is not 'empty':
            response = response + 'Damage at lowest character level ' + spell.damage_at_character_level[0] + '\n'

        if spell.heal_at_character_level is not 'empty':
            response = response + 'Healing at lowest slot level ' + spell.heal_at_slot_level[0] + '\n'

        if spell.dc_type is not 'empty':
            response = response + 'dc type ' + spell.dc_type + '\n'

        if spell.dc_success is not 'empty':
            response = response + 'dc success ' + spell.dc_success + '\n'

        if spell.area_of_effect_type is not 'empty':
            response = response + 'Area of effect type ' + spell.area_of_effect_type + '\n'

        if spell.area_of_effect_size is not 'empty':
            response = response + 'Area of effect size ' + spell.area_of_effect_size + '\n'

        if spell.school is not 'empty':
            response = response + 'School ' + spell.school + '\n'

        return response 