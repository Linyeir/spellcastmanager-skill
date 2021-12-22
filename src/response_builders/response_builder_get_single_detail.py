from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_detail_error import InvalidDetailError


class ResponseBuilderGetSingleDetail(ResponseBuilderBase):
    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    def _get_damage_healing_at_casting_level(self, attribute_type, attribute_dict, casting_level):
        first_key = list(attribute_dict.keys())[0]
        last_key = list(attribute_dict.keys())[-1]
        if casting_level < first_key or casting_level == 'min':
            casting_level = first_key
        elif casting_level > last_key or casting_level == 'max':
            casting_level = last_key

        res = {attribute_type: attribute_dict[casting_level], 'at_casting_level': casting_level}

        if casting_level < first_key or casting_level > last_key:
            res['validity'] = 'invalid casting level'
        
        return res

    def _get_casting_min_max_dict(self, casting_level):
        if casting_level == 'min_casting_level':
            index = 0
        elif casting_level == 'max_casting_level':
            index = -1

        if self._spell.damage_at_slot_level != 'empty':
            res = {casting_level: list(self._spell.damage_at_slot_level.keys())[index], 'type': 'slot level'}
        elif self._spell.damage_at_character_level != 'empty':
            res = {casting_level: list(self._spell.damage_at_character_level.keys())[index], 'type': 'character level'}
        elif self._spell.heal_at_slot_level != 'empty':
            res = {casting_level: list(self._spell.heal_at_slot_level.keys())[index], 'type': 'slot level'}
        elif self._spell.heal_at_character_level != 'empty':
            res = {casting_level: list(self._spell.heal_at_character_level.keys())[index], 'type': 'character level'}
        else:
            raise InvalidDetailError(casting_level)
        return res

    # definitely to refactor!
    # for now:
    # expecting almost explizit detail name
    def get_response(self, detail: str, casting_level: str) -> dict:
        if 'name' in detail:
            response = {'name': self._spell.name}
        if 'desc' in detail:
            response = {'desc': self._spell.desc}
        if 'high' in detail:
            response = {'higher_level': self._spell.higher_level}
            if response == 'empty':
                response = {'higher_level': 'stays the same'}
        if 'range' in detail:
            response = {'range': self._spell.range}
        if 'component' in detail:
            response = {'components': self._spell.components}
            if response == 'empty':
                response = {'components': 'no components'}
        if 'material' in detail:
            response = {'material': self._spell.material}
            if response == 'empty':
                response = {'material': 'no material'}
        if 'ritual' in detail:
            if self._spell.ritual == True:    
                response = {'ritual': 'a ritual'}
            if self._spell.ritual == False:
                response = {'ritual': 'not a ritual'}
        if 'duration' in detail:
            response = {'duration': self._spell.duration}
        if 'concent' in detail:
            if self._spell.concentration == True:
                response = {'concentration': 'concentration'}
            if self._spell.concentration == False:
                response = {'concentration': 'no concentration'}
        if 'time' in detail:
            response = {'casting_time': self._spell.casting_time}
        if 'level' == detail:
            response = {'level': self._spell.level}
        if 'attack' in detail:
            response = {'attack_type': self._spell.attack_type}
        if 'damage' in detail and 'type' in detail:
            response = {'damage_type': self._spell.damage_type}
            if response == 'empty':
                response = {'damage_type': 'no type'}

        if 'damage' in detail and 'slot' in detail:
            if self._spell.damage_at_slot_level != 'empty':
                attribute_type = 'damage_at_slot_level'
                response = self._get_damage_healing_at_casting_level(self, attribute_type, self._spell.damage_at_slot_level, casting_level)

        if 'damage' in detail and 'character' in detail:
            if self._spell.damage_at_character_level != 'empty':
                attribute_type = 'damage_at_character_level'
                response = self._get_damage_healing_at_casting_level(self, attribute_type, self._spell.damage_at_character_level, casting_level)

        if 'heal' in detail and 'slot' in detail:
            if self._spell.heal_at_slot_level != 'empty':
                attribute_type = 'heal_at_slot_level'
                response = self._get_damage_healing_at_casting_level(self, attribute_type, self._spell.heal_at_slot_level, casting_level)

        if 'heal' in detail and 'character' in detail:
            if self._spell.heal_at_character_level != 'empty':
                attribute_type = 'heal_at_character_level'
                response = self._get_damage_healing_at_casting_level(self, attribute_type, self._spell.heal_at_character_level, casting_level)

        if 'min' in detail and 'level' in detail:
            casting_level = 'min_casting_level'
            response = self._get_casting_min_max_dict(casting_level)

        if 'max' in detail and 'level' in detail:
            casting_level = 'max_casting_level'
            response = self._get_casting_min_max_dict(casting_level)

        if 'type' in detail and ('dc' in detail or 'difficulty class' in detail or 'saving throw' in detail):
            response = {'dc_type': self._spell.dc_type}
        if 'success' in detail and ('dc' in detail or 'difficulty class' in detail or 'saving throw' in detail):
            response = {'dc_success': self._spell.dc_success}
        if 'area' in detail and 'type' in detail:
            response = {'area_of_effect_type': self._spell.area_of_effect_type}
        if 'area' in detail and 'size' in detail:
            response = {'area_of_effect_size': self._spell.area_of_effect_size}
        if 'school' in detail:
            response = {'school': self._spell.school}
        
        if response == 'empty':
            raise InvalidDetailError(detail)

        return response

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