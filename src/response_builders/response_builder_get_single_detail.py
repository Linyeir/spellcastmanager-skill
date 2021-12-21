from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_detail_error import InvalidDetailError

class ResponseBuilderGetSingleDetail(ResponseBuilderBase):
    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    def _get_casting_level_attribute(self, casting_level):
        if self._spell.damage_at_slot_level != 'empty':
            return self._spell.damage_at_slot_level[casting_level]
        elif self._spell.damage_at_character_level != 'empty':
            return self._spell.damage_at_character_level[casting_level]
        elif self._spell.heal_at_slot_level != 'empty':
            return self._spell.heal_at_slot_level[casting_level]
        elif self._spell.heal_at_character_level != 'empty':
            return self._spell.heal_at_character_level[casting_level]
        else:
            raise 'empty'

    # definitely to refactor!
    # for now:
    # expecting almost explizit detail name
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
        if 'duration' in detail:
            detail = self._spell.duration
        if 'concent' in detail:
            detail = self._spell.concentration
        if 'time' in detail:
            detail = self._spell.casting_time
        if 'level' == detail:
            detail = self._spell.level
        if 'attack' in detail:
            detail = self._spell.attack_type
        if 'damage' in detail & 'type' in detail:
            detail = self._spell.damage_type            
        if 'damage' in detail & 'slot' in detail:
            detail = self._spell.damage_at_slot_level[casting_level]    # where checks if valid?
        if 'damage' in detail & 'character' in detail:
            detail = self._spell.damage_at_character_level[casting_level]
        if 'heal' in detail & 'slot' in detail:
            detail = self._spell.heal_at_slot_level[casting_level]
        if 'heal' in detail & 'character' in detail:
            detail = self._spell.heal_at_character_level[casting_level]
        if 'min' in detail & 'level' in detail:
            casting_level = 'min'
            detail = self._get_casting_level_attribute(casting_level)
        if 'max' in detail & 'level' in detail:
            casting_level = 'min'
            detail = self._get_casting_level_attribute(casting_level)
        if 'type' in detail & ('dc' in detail | 'difficulty class' in detail | 'saving throw' in detail):
            detail = self._spell.dc_type
        if 'success' in detail & ('dc' in detail | 'difficulty class' in detail | 'saving throw' in detail):
            detail = self._spell.dc_success
        if 'area' in detail & 'type' in detail:
            detail = self._spell.area_of_effect_type
        if 'area' in detail & 'size' in detail:
            detail = self._spell.area_of_effect_size
        if 'school' in detail:
            detail = self._spell.school

            #dont forget generic: damage, dice, healing effect, casting level   -> maybe

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
