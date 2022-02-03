from .intent_base import IntentBase
from ..response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentGetSpellDescription(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetSpellDescription(spell_name_input)
            response = self._response_builder.get_response()
            Spellcastmanager.set_context('spellname', self._response_builder.spell.name)
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
        else:
            Spellcastmanager.speak_dialog('get.spell.description',response)
            self._continue(Spellcastmanager)
    
    def _validate_yes_no(self, response):
        if response == 'yes' or response == 'no':
            return True
        else:
            return False
    
    def _continue(self, Spellcastmanager):
        """
        prompts user for more questions
        """
        to_continue = Spellcastmanager.get_response('prompt.questions', {'name': self._response_builder.spell.name}, validator=self._validate_yes_no, on_fail='get.single.detail.request.repetition', num_retries=1)
        if to_continue == 'yes':
            Spellcastmanager.speak_dialog('what.do.you.want.to.know')
        else:
            Spellcastmanager.speak_dialog('alright')
            Spellcastmanager.remove_context('spellname')
