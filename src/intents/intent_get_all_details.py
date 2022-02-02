from .intent_base import IntentBase
from ..response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from ..utils.spell_categorizer import SpellCategorizer
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError

class IntentGetAllDetails(IntentBase):
    def __init__(self):
        pass        

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetAllDetails(spell_name_input)
            Spellcastmanager.set_context('spellname', self._response_builder.spell.name)
            response = self._response_builder.get_response()
            spell_categorizer = SpellCategorizer(response)
            spell_category = spell_categorizer.get_categorie_from_details()
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
            dialog = 'get.all.details.category.' + str(spell_category)
            Spellcastmanager.speak_dialog(dialog, response)

# name
# desc
# higher_level
# range
# components
# material
# ritual
# duration
# concentration
# casting_time
# level
# attack_type
# damage_type
# at_casting_level
# min_casting_level
# max_casting_level
# dc_type
# dc_success
# area_of_effect_type
# area_of_effect_size
# school