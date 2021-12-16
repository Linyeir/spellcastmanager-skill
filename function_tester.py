from src.response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from src.utils.exceptions.invalid_spell_error import InvalidSpellError


try:
    response = ResponseBuilderGetSpellDescription('fireboll')
    print(response.get_response())
except InvalidSpellError as err:
    print('hass ' + str(err))