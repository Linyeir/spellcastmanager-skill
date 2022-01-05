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
        rp.detail_validation()

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
            detail_input = Spellcastmanager.get_response('get.single.detail.request.detail', {'name': spell_name_input}, validator=self._detail_validation(self._response_builder), on_fail='invalid.detail.error', num_retries=2)      


        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')        
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})




# -hey, i want infor about fireball 
# calling getSingleIntent
# extracting spell name
# building spell (rp)
# raise if not stated or invalid
# calling request.detail.dialog <sure, what dou you want to know about fireball>
# get_response, check for valid detail -> raise  //what about spell slot/ character level?
# 



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