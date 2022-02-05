from .intent_base import IntentBase
from ..response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail
from ..utils.detail_normalizer import DetailNormalizer
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError


class IntentGetSingleDetail(IntentBase):
    """
    prompts for user input and validates it
    chooses dialog based on validation
    """
    def __init__(self):
        """
        builds DetailNormalizer
        """
        self._detail_normalizer = DetailNormalizer()


    def execute(self, Spellcastmanager, message):
        """
        prompts user for spell name, detail and when necessary the casting level
        validates the input
        chooses dialog based on validation
        """
        self._title = super()._set_settings(Spellcastmanager)
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetSingleDetail(spell_name_input)
            Spellcastmanager.set_context('spellname', self._response_builder.spell.name)
            should_repeat_iteration = 'yes'
            reask_counter = 0
            already_asked = False
            detail_valid = True

            while should_repeat_iteration == 'yes' and reask_counter < 3:
                if already_asked and detail_valid:
                    should_repeat_iteration = Spellcastmanager.get_response('get.single.detail.something.else', {'name': spell_name_input})
                if should_repeat_iteration == 'no':
                    Spellcastmanager.speak_dialog('alright')
                    self._continue(Spellcastmanager)
                    return
                if should_repeat_iteration != 'no' and should_repeat_iteration != 'yes':
                    reask_counter = reask_counter + 1
                    continue
                detail_valid = self._fetch_detail(Spellcastmanager, spell_name_input, detail_valid)
                already_asked = True
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')        
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})
            Spellcastmanager.remove_context('spellname')

    
    def _continue(self, Spellcastmanager):
        """
        prompts user for more questions
        """
        to_continue = Spellcastmanager.get_response('prompt.questions', {'name': self._response_builder.spell.name}, validator=self._validate_yes_no, on_fail='get.single.detail.request.repetition', num_retries=1)
        if to_continue == 'yes':
            Spellcastmanager.speak_dialog('what.do.you.want.to.know', expect_response=True)
        else:
            Spellcastmanager.speak_dialog('alright')
            Spellcastmanager.remove_context('spellname')

    def _validate_yes_no(self, response):
        """
        validates, if user response is something else then yes or no
        """
        if response == 'yes' or response == 'no':
            return True
        else:
            return False

        
    def _fetch_detail(self, Spellcastmanager, spell_name_input, detail_valid):
        """
        prompts user for detail and repeats if invalid
        calls choose dialog function
        """
        retry_counter = 0
        response_valid = False

        # retry for invalid responses
        while response_valid == False and retry_counter < 3:
            if detail_valid:
                detail_input = Spellcastmanager.get_response('get.single.detail.request.detail', {'name': spell_name_input})
            else:
                detail_input = Spellcastmanager.get_response()
            detail = self._normalize_detail(Spellcastmanager, detail_input)
            if detail == 'empty':
                retry_counter = self._speak_error_message(Spellcastmanager, retry_counter)
                return False
            casting_level = self._fetch_casting_level(Spellcastmanager, detail)
            self._api_response = self._response_builder.get_response(detail, casting_level)
            if self._api_response == 'empty':
                retry_counter = self._speak_error_message(Spellcastmanager, retry_counter)
                return False
            response_valid = True
        self._call_detail_dialog(Spellcastmanager, self._api_response)
        return True

            
    def _speak_error_message(self, Spellcastmanager, retry_counter): 
        """
        reads error and prompt repetition message
        increases retry counter for repetition
        """
        Spellcastmanager.speak_dialog('invalid.detail.error')
        Spellcastmanager.speak_dialog('get.single.detail.request.repetition')
        return retry_counter + 1

    def _fetch_casting_level(self, Spellcastmanager, detail):
        """
        prompts user for casting level if necessary
        """
        if self._casting_level_is_needed(detail):
            return Spellcastmanager.get_response('get.single.detail.prompt.casting_level')
        else:
            return 'min'

    def _casting_level_is_needed(self, detail):
        """
        checks if casting level is necessary, returns confirmation
        """
        attributes_with_casting_level = ['damage_at_slot_level', 'damage_at_character_level', 'heal_at_slot_level', 'heal_at_character_level']
        for entry in attributes_with_casting_level:
            if detail == entry:
                return True
        return False

    def _call_detail_dialog(self, Spellcastmanager, response):
        """
        chooses detail dialog based on asked details and validation
        """
        key = list(response.keys())[0]
        dialog_file_name = 'get.single.detail.' + key
        Spellcastmanager.speak_dialog(dialog_file_name, response)

        if key == 'invalid_level':      # calling actual damage/ heal dialog here, above just invalid message
            key = list(response.keys())[1]
            dialog_file_name = 'get.single.detail.' + key
            Spellcastmanager.speak_dialog(dialog_file_name, response)
        
    def _normalize_detail(self, Spellcastmanager, detail_input):
        """
        input: detail in spoken form
        returns detail as attribute form (normalized)
        """
        if detail_input == None:
            return 'empty'
        if Spellcastmanager.voc_match(detail_input, 'valid_attributes'):
            attribute = self._detail_normalizer.match_spoken_detail_to_attribute(detail_input)
        else:
            return 'empty'

        return attribute
