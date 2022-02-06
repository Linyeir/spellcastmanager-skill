import re
from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderInvokeCastingAssistant(ResponseBuilderBase):
    """
    helper class that prepares the responses for the casting assistant intent
    """
    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)


    def get_response(self) -> dict:
        """
        provides a dictionary with the relevant information for the casting assistant
        """

        response = {'name': self._spell.name}

        if self._spell.desc != 'empty':
            response['desc']=  self._spell.desc
        else:
            response['desc'] = 'empty'

        if self._spell.dc_type != 'empty':
            response['dc_type'] = self._spell.dc_type
        else:
            response['dc_type'] = 'empty'

        if self._spell.dc_success != 'empty':
            response['dc_success'] = self._spell.dc_success

        if self._spell.area_of_effect_type != 'empty':
            response['area_of_effect_type'] = self._spell.area_of_effect_type
        else:
            response['area_of_effect_type'] = 'empty'

        if self._spell.area_of_effect_size != 'empty':
            response['area_of_effect_size'] = self._spell.area_of_effect_size

        return response


    def get_casting_level_type(self) -> str:
        """
        returns, if the spell requires a character level or a spellslot level
        """

        if self._spell.damage_at_slot_level != 'empty':
            return 'spellslot'

        elif self._spell.heal_at_slot_level != 'empty':
            return 'spellslot'

        elif self._spell.damage_at_character_level != 'empty':
            return 'characterlevel'

        elif self._spell.heal_at_character_level != 'empty':
            return 'characterlevel'
        else:
            return 'empty'

    def get_heal_or_unheal(self):
        """
        returns if the spell heals or deals damage
        """

        if self._spell.damage_at_slot_level != 'empty':
            return 'damage'

        elif self._spell.heal_at_slot_level != 'empty':
            return 'heal'

        elif self._spell.damage_at_character_level != 'empty':
            return 'damage'

        elif self._spell.heal_at_character_level != 'empty':
            return 'heal'
        else:
            return 'empty'


    def get_casting_level_limits(self):
        """
        returns a dict containing the minimal and the maximal casting level
        """

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
            response['min_casting_level'] = 'empty'
            response['max_casting_level'] = 'empty'
        return response


    def get_value_at_casting_level(self, casting_level):
        """
        returns the damage or heal value for a given casting level
        """

        try:
            if (self._spell.damage_at_slot_level != 'empty'):
                value_at_casting_level = self._spell.damage_at_slot_level[str(casting_level)]

            elif self._spell.heal_at_slot_level != 'empty':
                value_at_casting_level = self._spell.heal_at_slot_level[str(casting_level)]

            elif self._spell.damage_at_character_level != 'empty':
                value_at_casting_level = self._spell.damage_at_character_level[str(casting_level)]

            elif self._spell.heal_at_character_level != 'empty':
                value_at_casting_level = self._spell.heal_at_character_level[str(casting_level)]

            else:
                value_at_casting_level = 'empty'
        except:
            return 'empty'
        else:
            return value_at_casting_level



