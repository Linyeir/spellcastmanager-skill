from .response_builder_base import ResponseBuilderBase
from ..utils.Spell_class import Spell_class
from src.utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderGetAllDetails(ResponseBuilderBase):

    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell_class(spell_name)

    def get_response(self, detail: str, casting_level: str) -> dict:
        response = ''

        response = 'Name ' + self._spell.name + '\n'
    
        if self._spell.higher_level != 'empty':
            response = response + 'Changes for higher levels are ' + '\n'

        if self._spell.range != 'empty':
            response = response + 'Range ' + self._spell.range + '\n'

        if self._spell.components != 'empty':
            response = response + 'Components '
            for entry in self._spell.components:
                response = response + entry + ' ' 
            response = response + '\n'

        if self._spell.material != 'empty':
            response = response + 'Material ' + self._spell.material + '\n'

        if self._spell.ritual != 'empty':        # what type is ritual?
            if self._spell.ritual is True:
                response = response + 'Is a ritual\n'
            if self._spell.ritual is False:
                response = response + 'is not a ritual\n'

        if self._spell.duration != 'empty':
            response = response + 'Spell duration ' + self._spell.duration + '\n'
            
        if self._spell.concentration != 'empty':
            if self._spell.concentration is True:
                response = response + 'Concentration yes\n'
            if self._spell.concentration is False:
                response = response + 'Concentration no\n'

        if self._spell.casting_time != 'empty':
            response = response + 'Casting time ' + self._spell.casting_time + '\n'

        if self._spell.level != 'empty':
            response = response + 'Level ' + self._spell.level + '\n'

        if self._spell.attack_type != 'empty':
            response = response + 'Attack type ' + self._spell.attack_type + '\n'

        if self._spell.damage_type != 'empty':
            response = response + 'Damage type ' + self._spell.damage_type + '\n'
            
        if self._spell.damage_at_slot_level != 'empty':
            response = response + 'Damage at lowest slot level ' + list(self._spell.damage_at_slot_level.values())[0] + '\n'

        if self._spell.heal_at_slot_level != 'empty':
            response = response + 'Healing at lowest slot level ' + list(self._spell.heal_at_slot_level.values())[0] + '\n'

        if self._spell.damage_at_character_level != 'empty':
            response = response + 'Damage at lowest character level ' + list(self._spell.damage_at_character_level.values())[0] + '\n'

        if self._spell.heal_at_character_level != 'empty':
            response = response + 'Healing at lowest slot level ' + list(self._spell.heal_at_slot_level.values())[0] + '\n'

        if self._spell.dc_type != 'empty':
            response = response + 'dc type ' + self._spell.dc_type + '\n'

        if self._spell.dc_success != 'empty':
            response = response + 'dc success ' + self._spell.dc_success + '\n'

        if self._spell.area_of_effect_type != 'empty':
            response = response + 'Area of effect type ' + self._spell.area_of_effect_type + '\n'

        if self._spell.area_of_effect_size != 'empty':
            response = response + 'Area of effect size ' + self._spell.area_of_effect_size + '\n'

        if self._spell.school != 'empty':
            response = response + 'School ' + self._spell.school + '\n'


        return response 