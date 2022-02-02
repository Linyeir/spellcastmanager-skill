from pickle import TRUE
from turtle import setundobuffer
from .intent_base import IntentBase
from ..response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail
from ..utils.detail_normalizer import DetailNormalizer
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError
from ..utils.exceptions.no_detail_specified_error import NoDetailSpecifiedError
from ..utils.exceptions.invalid_detail_error import InvalidDetailError


class IntentGetSingleDetail(IntentBase):
    def __init__(self):
        self._detail_normalizer = DetailNormalizer()


    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetSingleDetail(spell_name_input)
            self._fetch_detail(Spellcastmanager, spell_name_input)
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')        
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})

        
    def _fetch_detail(self, Spellcastmanager, spell_name_input):
        retry_counter = 0
        response_valid = False
        while response_valid == False and retry_counter < 3:
            detail_input = Spellcastmanager.get_response('get.single.detail.request.detail', {'name': spell_name_input})
            detail = self._normalize_detail(detail_input)
            if detail == 'empty':
                retry_counter = self._speak_error_message(Spellcastmanager, retry_counter)
                return
            casting_level = self._fetch_casting_level(Spellcastmanager, detail)
            self._api_response = self._response_builder.get_response(detail, casting_level)
            if detail == 'empty':
                retry_counter = self._speak_error_message(Spellcastmanager, retry_counter)
                return
            response_valid = True
            
            
            
            '''
            try:
                detail_input = Spellcastmanager.get_response('get.single.detail.request.detail', {'name': spell_name_input})
                detail = self._normalize_detail(detail_input)
                casting_level = self._fetch_casting_level(Spellcastmanager, detail)
                self._api_response = self._response_builder.get_response(detail, casting_level)     #casting level?
            except NoDetailSpecifiedError as err:
                Spellcastmanager.log.error(err)
                Spellcastmanager.speak_dialog('no.detail.specified.error')
            except InvalidDetailError as err:
                Spellcastmanager.log.error(err)
                Spellcastmanager.speak_dialog('invalid.detail.error', {'detail': detail_input})
            else:
                if self._api_response == 'empty':
                    Spellcastmanager.speak_dialog('get.single.detail.request.repetition')
                    retry_counter = retry_counter + 1
                else:
                    response_valid = True
                    self._call_detail_dialog(self, Spellcastmanager, self._api_response)
            '''
            
    def _speak_error_message(self, Spellcastmanager, retry_counter): 
        Spellcastmanager.speak_dialog('invalid.detail.error')
        Spellcastmanager.speak_dialog('get.single.detail.request.repetition')
        return retry_counter + 1

    def _fetch_casting_level(self, Spellcastmanager, detail):
        if self._casting_level_is_needed(detail):
            return Spellcastmanager.get_response('get.single.detail.casting_level')
        else:
            return 'min'

    def _casting_level_is_needed(self, detail):
        attributes_with_casting_level = ['damage_at_slot_level', 'damage_at_character_level', 'heal_at_slot_level', 'heal_at_character_level']
        for entry in attributes_with_casting_level:
            if detail == entry:
                return True
        return False

    def _call_detail_dialog(self, Spellcastmanager, response):
        # min max vorher abfangen
        # andere außnahmen?
        key = list(response.key())[0]

        dialog_file_name = 'get.single.detail.' + key

        Spellcastmanager.speak_dialog(dialog_file_name, response)

        if key == 'invalid_level':      # calling actual damage/ heal dialog here, above just invalid message
            key = list(response.key())[1]
            dialog_file_name = 'get.single.detail.' + key
            Spellcastmanager.speak_dialog(dialog_file_name, response)

        
    def _normalize_detail(self, Spellcastmanager, detail_input):
        if detail_input == None:
            raise NoDetailSpecifiedError
        if Spellcastmanager.voc_match(detail_input, 'valid_attributes'):
            attribute = self._detail_normalizer.match_spoken_detail_to_attribute(detail_input)
        else:
            return 'empty'

        return attribute