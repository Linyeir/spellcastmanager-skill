from .intent_base import IntentBase
from ..response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentGetAllDetails(IntentBase):
    def __init__(self):
        pass

    #def _extract_casting_level(message):
    #    casting_level_input = message.data.get('casting_level')
    #    if casting_level_input == None:
    #        casting_level_input == 'default'
    #    return casting_level_input
        

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetAllDetails(spell_name_input)
            response = self._response_builder.get_response()
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'spellname': spell_name_input})
        else:
            Spellcastmanager.speak_dialog('get.all.details', response)

          
            # Spellcastmanager.speak_dialog('get.all.details.dialog', {'name': response['name'], 
            #                                                                 'desc': response['desc'], 
            #                                                                 'higher_level': response['higher_level'],
            #     -not complete! see list below! (casting level)              'range': response['range'],
            #                                                                 'components': response['components'],
            #                                                                 'material': response['material'],
            #                                                                 'ritual': response['ritual'],
            #                                                                 'duration': response['duration'],
            #                                                                 'concentration': response['concentration'],
            #                                                                 'casting_time': response['casting_time'],
            #                                                                 'level': response['level'],
            #                                                                 'attack_type': response['attack_type'],
            #                                                                 'damage_type': response['damage_type'],
            #                                                                 'damage_at_slot_level': response['damage_at_slot_level'],
            #                                                                 'heal_at_slot_level': response['heal_at_slot_level'],
            #                                                                 'damage_at_character_level': response['damage_at_character_level'],
            #                                                                 'heal_at_character_level': response['heal_at_character_level'],
            #                                                                 'dc_type': response['dc_type'],
            #                                                                 'dc_success': response['dc_success'],
            #                                                                 'area_of_effect_type': response['area_of_effect_type'],
            #                                                                 'area_of_effect_size': response['area_of_effect_size'],
            #                                                                 'school': response['school']
            #                                                                 }) 




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