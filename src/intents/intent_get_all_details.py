from .intent_base import IntentBase
from ..response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription

class IntentGetAllDetails(IntentBase):
    def __init__(self):
        pass

    def _extract_casting_level(message):
        casting_level_input = message.data.get('casting_level')
        if casting_level_input == None:
            casting_level_input == 'default'
        return casting_level_input
        

    def execute(self, Spellcastmanager, message):
        requested_details = ({'name': 'name', 'desc': 'desc', 'higher_level': 'higher_level', 'range': 'range', 'components': 'components',
        'material': 'material', 'ritual': 'ritual', 'duration': 'duration', 'concentration': 'concentration', 'casting_time': 'casting_time',
        'level': 'level', 'attack_type': 'attack_type', 'damage_type': 'damage_type', 'damage_at_slot_level': 'damage_at_slot_level',
        'heal_at_slot_level': 'heal_at_slot_level', 'damage_at_character_level': 'damage_at_character_level', 
        'heal_at_character_level': 'heal_at_character_level', 'dc_type': 'dc_type', 'dc_success': 'dc_success', 
        'area_of_effect_type': 'area_of_effect_type', 'area_of_effect_size': 'area_of_effect_size', 'school': 'school',
        })

        try:
            spell_name_input = super()._extract_spell_name(message)
            casting_level_input = self._extract_casting_level(message)
            self._response_builder = ResponseBuilderGetSpellDescription(spell_name_input, casting_level_input)
            response = self._response_builder.get_response(requested_details, casting_level_input)
        except: # api wrapper not reachable
            Spellcastmanager.intent.speak_dialog('api.not.reachable.error.dialog')
        except: # no spell name stated
            Spellcastmanager.intent.speak_dialog('no.spell.specified.error.dialog')
        except: # invalid spell name
            Spellcastmanager.intent.speak_dialog('invalid.spell.error.dialog', {'spellname': spell_name_input})
        else:
            Spellcastmanager.intent.speak_dialog('get.all.details.dialog', response)

          
            # Spellcastmanager.intent.speak_dialog('get.all.details.dialog', {'name': response['name'], 
            #                                                                 'desc': response['desc'], 
            #                                                                 'higher_level': response['higher_level'],
            #                                                                 'range': response['range'],
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
# damage_at_slot_level
# heal_at_slot_level
# damage_at_character_level
# heal_at_character_level
# dc_type
# dc_success
# area_of_effect_type
# area_of_effect_size
# school