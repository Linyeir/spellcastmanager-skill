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
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')        
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})
        else:
            self._call_detail_dialog(self, Spellcastmanager, self._api_response)

        retry_counter = 0
        response_valid = False

        while response_valid == False and retry_counter < 3:
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
#                Spellcastmanager.speak_dialog('get.single.detail.request.repetition')
#                retry_counter = retry_counter + 1
            else:
#                response_valid == True

    def _fetch_casting_level(self, Spellcastmanager, detail):
        if self._casting_level_is_needed(detail):
            return Spellcastmanager.get_response('get.single.detail.casting_level')        #validation? probabaly not cause min/max
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
            raise InvalidDetailError

        return attribute


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