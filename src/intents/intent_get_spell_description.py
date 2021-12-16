from .intent_base import IntentBase
from .response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpecifiedSpellError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentGetSpellDescription(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetSpellDescription(spell_name_input)
            response = self._response_builder.get_response('desc')
        except APINotReachableError as err:
            Spellcastmanager.log.info(err)
            Spellcastmanager.intent.speak_dialog('api.not.reachable.error.dialog')
        except NoSpecifiedSpellError as err:
            Spellcastmanager.log.info(err)
            Spellcastmanager.intent.speak_dialog('no.spell.specified.error.dialog')
        except InvalidSpellError as err:
            Spellcastmanager.log.info(err)
            Spellcastmanager.intent.speak_dialog('invalid.spell.error.dialog', {'spellname': spell_name_input})
        else:
            Spellcastmanager.intent.speak_dialog('get.spell.description.dialog', {'description': response})



