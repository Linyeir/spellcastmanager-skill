from ..Spell_class import Spell_class

def build_response_all_details(spell_name_in):
    spell = Spell_class(spell_name_in)
    response = ''

    # remove if statements from not optional attributes? which ones are not optional?

    if spell.name == 'empty':
        return 'empty'
    else:
        response = 'Name ' + spell.name + '\n'
    
        if spell.higher_level != 'empty':
            response = response + 'Changes for higher levels are ' + '\n'

        if spell.range != 'empty':
            response = response + 'Range ' + spell.range + '\n'

        if spell.components != 'empty':
            response = response + 'Components '
            for entry in spell.components:
                response = response + entry + ' ' 
            response = response + '\n'

        if spell.material != 'empty':
            response = response + 'Material ' + spell.material + '\n'

        if spell.ritual != 'empty':        # what type is ritual?
            if spell.ritual is True:
                response = response + 'Is a ritual\n'
            if spell.ritual is False:
                response = response + 'is not a ritual\n'

        if spell.duration != 'empty':
            response = response + 'Spell duration ' + spell.duration + '\n'
            
        if spell.concentration != 'empty':
            if spell.concentration is True:
                response = response + 'Concentration yes\n'
            if spell.concentration is False:
                response = response + 'Concentration no\n'

        if spell.casting_time != 'empty':
            response = response + 'Casting time ' + spell.casting_time + '\n'

        if spell.level != 'empty':
            response = response + 'Level ' + spell.level + '\n'

        if spell.attack_type != 'empty':
            response = response + 'Attack type ' + spell.attack_type + '\n'

        if spell.damage_type != 'empty':
            response = response + 'Damage type ' + spell.damage_type + '\n'
            
        if spell.damage_at_slot_level != 'empty':
            response = response + 'Damage at lowest slot level ' + list(spell.damage_at_slot_level.values())[0] + '\n'

        if spell.heal_at_slot_level != 'empty':
            response = response + 'Healing at lowest slot level ' + list(spell.heal_at_slot_level.values())[0] + '\n'

        if spell.damage_at_character_level != 'empty':
            response = response + 'Damage at lowest character level ' + list(spell.damage_at_character_level.values())[0] + '\n'

        if spell.heal_at_character_level != 'empty':
            response = response + 'Healing at lowest slot level ' + list(spell.heal_at_slot_level.values())[0] + '\n'

        if spell.dc_type != 'empty':
            response = response + 'dc type ' + spell.dc_type + '\n'

        if spell.dc_success != 'empty':
            response = response + 'dc success ' + spell.dc_success + '\n'

        if spell.area_of_effect_type != 'empty':
            response = response + 'Area of effect type ' + spell.area_of_effect_type + '\n'

        if spell.area_of_effect_size != 'empty':
            response = response + 'Area of effect size ' + spell.area_of_effect_size + '\n'

        if spell.school != 'empty':
            response = response + 'School ' + spell.school + '\n'


        return response 