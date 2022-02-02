from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderInvokeCastingAssistant(ResponseBuilderBase):

    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)


    def get_response(self) -> dict:

        response = {'name': self._spell.name}

        if self._spell.dc_type != 'empty':
            response['dc_type'] = self._spell.dc_type
        else:
            response['dc_type'] = False

        if self._spell.dc_success != 'empty':
            response['dc_success'] = self._spell.dc_success

        if self._spell.area_of_effect_type != 'empty':
            response['area_of_effect_type'] = self._spell.area_of_effect_type
        else:
            response['area_of_effect_type'] = False

        if self._spell.area_of_effect_size != 'empty':
            response['area_of_effect_size'] = self._spell.area_of_effect_size

        return response 


    def _get_casting_level_type(self):
        if self._spell.damage_at_slot_level != 'empty':
            return 'spellslot'    

        elif self._spell.heal_at_slot_level != 'empty':
            return 'spellslot'

        elif self._spell.damage_at_character_level != 'empty':
            return 'characterlevel'

        elif self._spell.heal_at_character_level != 'empty':
            return 'characterlevel'
        else:
            return False

    def get_heal_or_unheal(self):
        if self._spell.damage_at_slot_level != 'empty':
            return 'damage'    

        elif self._spell.heal_at_slot_level != 'empty':
            return 'heal'

        elif self._spell.damage_at_character_level != 'empty':
            return 'damage'

        elif self._spell.heal_at_character_level != 'empty':
            return 'heal'
        else:
            return False


    def get_casting_level_limits(self):
        response = {}
        if self._spell.damage_at_slot_level != 'empty':
            response['min_casting_level'] = list(self._spell.damage_at_slot_level.keys())[0]
            response['max_casting_level'] = list(self._spell.damage_at_slot_level.keys())[-1]

        elif self._spell.heal_at_slot_level != 'empty':
            response['min_casting_level'] = list(self._spell.heal_at_slot_level.keys())[0]
            response['max_casting_level'] = list(self._spell.heal_at_slot_level.keys())[-1]

        elif self._spell.damage_at_character_level != 'empty':
            response['min_casting_level'] = list(self._spell.damage_at_character_level.keys())[0]
            response['max_casting_level'] = list(self._spell.damage_at_character_level.keys())[-1]

        elif self._spell.heal_at_character_level != 'empty':

            response['min_casting_level'] = list(self._spell.heal_at_character_level.keys())[0]
            response['max_casting_level'] = list(self._spell.heal_at_character_level.keys())[-1]
        else:
            response['min_casting_level'] = None
            response['max_casting_level'] = None


    def get_value_at_casting_level(self, casting_level):
        if (self._spell.damage_at_slot_level != 'empty'):
            value_at_casting_level = self._spell.damage_at_slot_level[str(casting_level)]

        elif self._spell.heal_at_slot_level != 'empty':
            value_at_casting_level = self._spell.heal_at_slot_level[str(casting_level)]
            
        elif self._spell.damage_at_character_level != 'empty':
            value_at_casting_level = self._spell.damage_at_character_level[str(casting_level)]

        elif self._spell.heal_at_character_level != 'empty':
            value_at_casting_level = self._spell.heal_at_character_level[str(casting_level)]

        else:
            value_at_casting_level = False
        
        return value_at_casting_level



