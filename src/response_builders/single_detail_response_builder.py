from ..utils.Spell_class import Spell_class


# for single detail intent
def build_response_get_single_detail(spell_name_in, spell_detail_in, slot_level = 0):
    spell = Spell_class(spell_name_in)

    if spell.name is 'empty':
        return 'empty'
    else:
        detail = getattr(spell, spell_detail_in)       # spell_detail_in is assumed to be correct -> solved somewhere else
        
        # slot too low or min -> min
        # slot too high or max -> max
        # slot inbetween -> specified slot

        if detail is spell.damage_at_slot_level or detail is spell.damage_at_character_level or detail is spell.heal_at_slot_level or detail is spell.heal_at_character_level:
            first_key = list(detail())[0]
            if slot_level <= first_key:
                slot_detail = ''
                if slot_level < first_key:
                    slot_detail = 'The stated spell slot is to low. You need at least a spell slot of ' + first_key + '\n'
                slot_detail = slot_detail + ''
        return detail

        # logic for slot level not implemented yet 


