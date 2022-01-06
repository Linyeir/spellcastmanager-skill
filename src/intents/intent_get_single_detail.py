from .intent_base import IntentBase
from ..response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError
from ..utils.exceptions.no_detail_specified_error import NoDetailSpecifiedError
from ..utils.exceptions.invalid_detail_error import InvalidDetailError


class IntentGetSingleDetail(IntentBase):
    def __init__(self):
        pass

    def _detail_validation(Spellcastmanager, response, rp):  #or self
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


    def _extract_detail(self, message):
        detail_input = message.data.get('single_detail')
        if detail_input == None:
            raise NoDetailSpecifiedError
        return detail_input

    def _extract_casting_level(self, message):
       casting_level_input = message.data.get('casting_level')
       if casting_level_input == None:
           casting_level_input == 'min'
       return casting_level_input

    def _call_detail_dialog(self, Spellcastmanager, response):

        # min max vorher abfangen
        # andere außnahmen?

        key = list(response.key())[1]

        dialog = 'get.single.detail.' + key

        Spellcastmanager.speak_dialog(dialog, response)

        if key == 'invalid_level':      # calling actual damage/ heal dialog here, above just invalid message
            key = list(response.key())[2]
            dialog = 'get.single.detail.' + key
            Spellcastmanager.speak_dialog(dialog, response)
        
    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetSingleDetail(spell_name_input)
                            # extracting detail like in message?
            detail = Spellcastmanager.get_response('get.single.detail.request.detail', {'name': spell_name_input}, validator=self._detail_validation(self._response_builder), on_fail='invalid.detail.error', num_retries=2)
            response = self._response_builder.get_response(detail)     #casting level?


        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')        
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})



# validation: does detail input exist for this spell? (not empty where it matters)
# answer: calling right attribute (not exact match)
# build: content -> 'readable answer' (false -> not a ritual)


# -hey, i want infor about fireball 
# calling getSingleIntent
# extracting spell name
# building spell (rp)
# raise if not stated or invalid
# calling request.detail.dialog <sure, what dou you want to know about fireball>
# get_response, check for valid detail -> raise  //what about spell slot/ character level?
# find right attribute -> get content
# call answer dialog



#    def execute(self, Spellcastmanager, message):
#        try:
#            detail_input = self._extract_detail(message)
#            casting_level_input = self._extract_casting_level(message)
#            response = self._response_builder.get_response(self, detail_input, casting_level_input)
#        except NoDetailSpecifiedError as err:
#            Spellcastmanager.log.error(err)
#            Spellcastmanager.speak_dialog('no.detail.specified.error')
#        except InvalidDetailError as err:
#            Spellcastmanager.log.error(err)
#            Spellcastmanager.speak_dialog('invalid.detail.error', {'detail': detail_input})
#        else:
#            self._call_detail_dialog(self, Spellcastmanager, response)