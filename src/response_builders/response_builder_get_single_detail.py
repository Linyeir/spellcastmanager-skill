from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_detail_error import InvalidDetailError

class ResponseBuilderGetSingleDetail(ResponseBuilderBase):
    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    # definitely to refactor!
    def get_response(self, detail: str, casting_level: str) -> dict:
        if 'name' in detail:
            detail = self._spell.name
        if 'desc' in detail:
            detail = self._spell.desc
        if 'high' in detail:
            detail = self._spell.higher_level
        if 'range' in detail:
            detail = self._spell.range
        if 'component' in detail:
            detail = self._spell.components
        if 'material' in detail:
            detail = self._spell.material
        if 'ritual' in detail:
            detail = self._spell.ritual
        else:
            raise InvalidDetailError(detail)

        if detail == 'empty':
            raise InvalidDetailError(detail)

        return detail
'''
        if 'duration' in detail:
            detail = self._spell.duration
        if 'concentr' in detail:
            detail = self._spell.concentration
        if 'time' in detail:
            detail = self._spell.casting_time

        if 'level' in detail & 'cast' not in detail & 'character' not in detail & 'slot' not in detail:
            detail = self._spell.level

        if 'attack' in detail:
            detail = self._spell.attack_type
        if 'damage' in detail & 'type' in detail:
            detail = self._spell.damage_type
        if 'damage' in detail & 'slot' in detail:
            detail = self._spell.damage_at_slot_level
        if 'damage' in detail & 'character' in detail:
            detail = self._spell.damage_at_character_level
        if 'heal' in detail & 'slot' in detail:
            detail = self._spell.heal_at_slot_level
        if 'heal' in detail & 'character' in detail:
            detail = self._spell.heal_at_character_level
        if 'm'

            #dont forget generic: damage, dice, healing effect, casting level

        # check for each possible attribute
            # is attribute in detail -> call atribute
                # else raise invalid detail
            # is attribute not empty
                # else raise invalid detail
'''           


# name
# desc
# higher_level
# range
# components
# material
# ritual
# duration
# concentration
# casting_time

# level
# attack_type
# damage_type

# at_casting_level
# min_casting_level
# max_casting_level
# dc_type
# dc_success
# area_of_effect_type
# area_of_effect_size
# school