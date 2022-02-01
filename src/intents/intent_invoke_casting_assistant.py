from .intent_base import IntentBase
from ..response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentInvokeCastinAssistant(IntentBase):
    def __init__(self):
        pass


    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderInvokeCastingAssistant(spell_name_input)
            response = self._response_builder.get_response()

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
            Spellcastmanager.speak_dialog(response)