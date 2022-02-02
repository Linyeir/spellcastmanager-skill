from mycroft.util.parse import extract_number
import lingua_franca
from .intent_base import IntentBase
from ..response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentInvokeCastingAssistant(IntentBase):
    def __init__(self):
        lingua_franca.load_language('en')


    def execute(self, Spellcastmanager, message):
        try:
            self._spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderInvokeCastingAssistant(self._spell_name_input) 
            self._api_response = self._response_builder.get_response       

        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': self._spell_name_input})
        else:
            self._execute_dialog(Spellcastmanager, message)


    def _execute_dialog(self, Spellcastmanager, message):
        casting_level = self._extract_casting_level(message)
        casting_level_type = self._response_builder.get_casting_level_type
        
        if (casting_level == False) and (casting_level_type != False):
            dialog_file_name = 'choose.' + casting_level_type
            casting_level_limits = self._response_builder.get_casting_level_limits
            casting_level_input = Spellcastmanager.get_response(dialog_file_name, data=casting_level_limits, valiator=self._validate_casting_level_input, on_fail='invalid slot level', num_retries=2)
                
            casting_level = self._extract_casting_level(message)

        elif (casting_level != False) and (casting_level_type != False):
            pass
        else:
            Spellcastmanager.speak_dialog('has.no.castinglevel', {'spellname': self._spell_name_input})
        
        effect_value = self._response_builder.get_value_at_casting_level(casting_level)
        effect_type = self._response_builder.get_heal_or_unheal
        area_of_effect_type = self._api_response['area_of_effect_type']

        if area_of_effect_type == False:
            dialog_file_path = 'inflict.' + effect_type
            Spellcastmanager.speak_dialog(dialog_file_path, {'value': effect_value})
        else:
            dialog_file_path = 'inflict.aoe.' + effect_type
            area_of_effect_size = self._api_response['area_of_effect_size']
            Spellcastmanager.speak_dialog(dialog_file_path, {'value': effect_value, 'aoe_size': area_of_effect_size, 'aoe_type': area_of_effect_type})

        if self._api_response['dc_type'] != False:
            Spellcastmanager.speak_dialog('saving.throw', {'value': effect_value}) 



    # extracts casting level from utterance, returns false, if invalid
    def _extract_casting_level(self, message):
        casting_level_input = message.data.get('level')
        if casting_level_input == None:
            return False
        else:
            casting_level = extract_number(casting_level_input) 
            return casting_level


    def _validate_casting_level_input(self, response):
        if not self._extract_casting_level(response):
            return True
        else:
            return False