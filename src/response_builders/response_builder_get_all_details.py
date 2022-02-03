from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderGetAllDetails(ResponseBuilderBase):
    """
    validates user input (spell name) and formats response fitting for dialog file
    """
    def __init__(self, spell_name: str):
        """
        validates spell name and builds class spell
        """
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    def get_response(self) -> dict:
        """
        adds not empty attributes with value to dict and returns it
        """
        response = {'name': self._spell.name}
    
        if self._spell.higher_level != 'empty':
            response['higher_level'] = self._spell.higher_level
        else:
            response['higher_level'] = 'stays the same'

        if self._spell.range != 'empty':
            response['range'] = self._spell.range

        if self._spell.components != 'empty':
            response['components'] = self._spell.components
        else:
            response['components'] = 'no components'

        if self._spell.material != 'empty':
            response['material'] = self._spell.material
        else: response['material'] = 'no materials'


        if self._spell.ritual != 'empty':        # what type is ritual?
            if self._spell.ritual is True:
                response['ritual'] = 'a ritual'
            if self._spell.ritual is False:
                response['ritual'] = 'not a ritual'

        if self._spell.duration != 'empty':
            response['duration'] = self._spell.duration
            
        if self._spell.concentration != 'empty':
            if self._spell.concentration is True:
                response['concentration'] = 'concentration'
            if self._spell.concentration is False:
                response['concentration'] = 'no concentration'

        if self._spell.casting_time != 'empty':
            response['casting_time'] = self._spell.casting_time

        if self._spell.level != 'empty':
            response['level'] = self._spell.level

        if self._spell.attack_type != 'empty':
            response['attack_type'] = self._spell.attack_type

        if self._spell.damage_type != 'empty':
            response['damage_type'] = self._spell.damage_type
        else:
            response['damage_type'] = 'no type'
            
        if self._spell.damage_at_slot_level != 'empty':
            response['at_casting_level'] = ('damage at spellslot level ' + 
                list(self._spell.damage_at_slot_level.keys())[0] + 
                ' is ' + 
                list(self._spell.damage_at_slot_level.values())[0])
            response['min_casting_level'] = 'minimum slot level ' + list(self._spell.damage_at_slot_level.keys())[0]
            response['max_casting_level'] = 'maximum slot level ' + list(self._spell.damage_at_slot_level.keys())[-1]

        if self._spell.heal_at_slot_level != 'empty':
            response['at_casting_level'] = ('health increase at spellslot level ' + 
                list(self._spell.heal_at_slot_level.keys())[0] + 
                ' is ' + 
                list(self._spell.heal_at_slot_level.values())[0])
            response['min_casting_level'] = 'minimum slot level ' + list(self._spell.heal_at_slot_level.keys())[0]
            response['max_casting_level'] = 'maximum slot level ' +list(self._spell.heal_at_slot_level.keys())[-1]

        if self._spell.damage_at_character_level != 'empty':
            response['at_casting_level'] = ('damage at character level ' + 
                list(self._spell.damage_at_character_level.keys())[0] + 
                ' is ' + 
                list(self._spell.damage_at_character_level.values())[0])
            response['min_casting_level'] = 'minimum character level ' + list(self._spell.damage_at_character_level.keys())[0]
            response['max_casting_level'] = 'minimum character level ' + list(self._spell.damage_at_character_level.keys())[-1]

        if self._spell.heal_at_character_level != 'empty':
            response['at_casting_level'] = ('health increase at character level ' + 
                list(self._spell.heal_at_character_level.keys())[0] + 
                ' is ' + 
                list(self._spell.heal_at_character_level.values())[0])
            response['min_casting_level'] = 'minimum character level ' + list(self._spell.heal_at_character_level.keys())[0]
            response['max_casting_level'] = 'maximum character level ' +list(self._spell.heal_at_character_level.keys())[-1]

        if self._spell.dc_type != 'empty':
            response['dc_type'] = self._spell.dc_type

        if self._spell.dc_success != 'empty':
            response['dc_success'] = self._spell.dc_success

        if self._spell.area_of_effect_type != 'empty':
            response['area_of_effect_type'] = self._spell.area_of_effect_type

        if self._spell.area_of_effect_size != 'empty':
            response['area_of_effect_size'] = self._spell.area_of_effect_size

        if self._spell.school != 'empty':
            response['school'] = self._spell.school


        return response 
    
    @property
    def spell(self):
        return self._spell