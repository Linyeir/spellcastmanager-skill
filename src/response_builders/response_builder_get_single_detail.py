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
        res = {}
        first_key = list(attribute_dict.keys())[0]
        casting_level = str(casting_level)

        if casting_level not in list(attribute_dict.keys()) and casting_level != 'min':
            res = {'invalid_level': 'invalid casting level'}

        if casting_level == 'min' or casting_level not in list(attribute_dict.keys()):
            casting_level = first_key

        res[attribute_type] = attribute_dict[casting_level]
        res['at_casting_level'] = casting_level
        
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
    def get_response(self, detail, casting_level = 'min'):
        response = 'empty'
        if 'name' in detail:
            response = {'name': self._spell.name}
        if 'desc' in detail:
            response = {'desc': self._spell.desc}
        if 'high' in detail:
            if self._spell.higher_level == 'empty':
                response = {'higher_level': 'stays the same'}
            else:
                response = {'higher_level': self._spell.higher_level}
        if 'range' in detail:
            response = {'range': self._spell.range}
        if 'component' in detail:
            if self._spell.components == 'empty':
                response = {'components': 'no components'}
            else:
                response = {'components': self._spell.components}
        if 'material' in detail:
            if self._spell.material == 'empty':
                response = {'material': 'no material'}
            else:
                response = {'material': self._spell.material}
        if 'ritual' in detail:
            if self._spell.ritual == True:    
                response = {'ritual': 'a ritual'}
            elif self._spell.ritual == False:
                response = {'ritual': 'not a ritual'}
        if 'duration' in detail:
            response = {'duration': self._spell.duration}
        if 'concent' in detail:
            if self._spell.concentration == True:
                response = {'concentration': 'concentration'}
            elif self._spell.concentration == False:
                response = {'concentration': 'no concentration'}
        if 'time' in detail:
            response = {'casting_time': self._spell.casting_time}
        if 'level' == detail:
            response = {'level': self._spell.level}
        if 'attack' in detail:
            response = {'attack_type': self._spell.attack_type}
        if 'damage' in detail and 'type' in detail:
            if self._spell.damage_type == 'empty':
                response = {'damage_type': 'no type'}
            else:
                response = {'damage_type': self._spell.damage_type}
            
        if 'damage' in detail and 'slot' in detail:
            if self._spell.damage_at_slot_level != 'empty':
                attribute_type = 'damage_at_slot_level'
                response = self._get_damage_healing_at_casting_level(attribute_type, self._spell.damage_at_slot_level, casting_level)

        if 'damage' in detail and 'character' in detail:
            if self._spell.damage_at_character_level != 'empty':
                attribute_type = 'damage_at_character_level'
                response = self._get_damage_healing_at_casting_level(attribute_type, self._spell.damage_at_character_level, casting_level)

        if 'heal' in detail and 'slot' in detail:
            if self._spell.heal_at_slot_level != 'empty':
                attribute_type = 'heal_at_slot_level'
                response = self._get_damage_healing_at_casting_level(attribute_type, self._spell.heal_at_slot_level, casting_level)

        if 'heal' in detail and 'character' in detail:
            if self._spell.heal_at_character_level != 'empty':
                attribute_type = 'heal_at_character_level'
                response = self._get_damage_healing_at_casting_level(attribute_type, self._spell.heal_at_character_level, casting_level)

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

        response['name'] = self._spell.name
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
# damage_slot
# damage_character
# heal_slot
# heal_character
# min_casting_level
# max_casting_level
# dc_type
# dc_success
# area_of_effect_type
# area_of_effect_size
# school