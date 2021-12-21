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

    def _extract_detail(message):
        detail_input = message.data.get('detail')
        if detail_input == None:
            raise NoDetailSpecifiedError
        return detail_input

    def _extract_casting_level(message):
       casting_level_input = message.data.get('casting_level')
       if casting_level_input == None:
           casting_level_input == 'min'
       return casting_level_input

    def _call_detail_dialog():
        pass

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            detail_input = self._extract_detail(message)
            casting_level_input = self._extract_casting_level(message)
            self._response_builder = ResponseBuilderGetSingleDetail(spell_name_input)
            response = self._response_builder.get_response(self, detail_input, casting_level_input)
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})
        except NoDetailSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.detail.specified.error')
        except InvalidDetailError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.detail.error', {'detail': detail_input})
        else:
            self._call_detail_dialog()      # to implement

