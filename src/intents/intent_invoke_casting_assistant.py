from mycroft.util.parse import extract_number
import lingua_franca
from .intent_base import IntentBase
from ..response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentInvokeCastingAssistant(IntentBase):
    """
    guides the user through the process of casting a specific spell while supplying the necessary values from the api
    """

    def __init__(self, lang):
        lingua_franca.load_language(lang)


    def execute(self, Spellcastmanager, message):
        """
        executes the casting assistant intent by first initializing the api handler and then starting the dialog
        """
        if not Spellcastmanager.set_settings():
            return
            
        try:
            self._spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderInvokeCastingAssistant(self._spell_name_input) 
            self._api_response = self._response_builder.get_response()       

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
        """
        executes the dialog by using mycrofts dialog functions 
        """

        casting_level = self._extract_casting_level(message.data.get('level'))

        if (casting_level == -1) and (self._response_builder.get_casting_level_type() != 'empty'):    
            dialog_file_name = 'choose.' + self._response_builder.get_casting_level_type()
            casting_level_limits = self._response_builder.get_casting_level_limits()
            dialog_data = casting_level_limits
            dialog_data['title'] = Spellcastmanager.settings['title']
            fail_message = 'you selected an invalid slot please choose one between ' + casting_level_limits['min_casting_level'] + ' and ' + casting_level_limits['max_casting_level']
            casting_level_input = Spellcastmanager.get_response(dialog_file_name, data=dialog_data, validator=self._validate_casting_level_input, on_fail=fail_message, num_retries=2)

            if casting_level_input is None:
                casting_level_input = casting_level_limits['min_casting_level']
                Spellcastmanager.speak('invalid spellslot, i will assume level ' + casting_level_input)
                
            casting_level = self._extract_casting_level(casting_level_input)

        elif (casting_level != -1) and (self._response_builder.get_casting_level_type != 'empty'):
            pass

        else:
            Spellcastmanager.speak_dialog('has.no.castinglevel', {'spellname': self._spell_name_input})
        
        effect_value = self._response_builder.get_value_at_casting_level(casting_level)
        effect_type = self._response_builder.get_heal_or_unheal()
        area_of_effect_type = self._api_response['area_of_effect_type']

        if effect_value == 'empty':
           Spellcastmanager.speak(self._api_response['desc']) 
        else:
            if area_of_effect_type == 'empty':
                dialog_file_path = 'inflict.' + effect_type
                Spellcastmanager.speak_dialog(dialog_file_path, {'value': effect_value})
            else:
                dialog_file_path = 'inflict.aoe.' + effect_type
                area_of_effect_size = self._api_response['area_of_effect_size']
                Spellcastmanager.speak_dialog(dialog_file_path, {'value': effect_value, 'aoe_size': area_of_effect_size, 'aoe_type': area_of_effect_type})

            if self._api_response['dc_type'] != 'empty':
                Spellcastmanager.speak_dialog('saving.throw', {'type': self._api_response['dc_type'], 'success' : self._api_response['dc_success']}) 


    def _extract_casting_level(self, message):
        """
        extracts the casting level from the utterance and returns false, if it is invalid
        """
        casting_level_input = message

        if casting_level_input == None:
            return -1
        else:
            casting_level = extract_number(casting_level_input) 
            return casting_level


    def _validate_casting_level_input(self, response):
        """
        validator function for mycrofts get_response function
        """

        castingLevel = self._extract_casting_level(response)
        if (castingLevel != -1) and (self._response_builder.get_value_at_casting_level(castingLevel) != 'empty'):
            return True
        else:
            return False