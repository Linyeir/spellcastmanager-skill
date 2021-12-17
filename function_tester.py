from src.response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer
from src.response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail


response = ResponseBuilderGetSingleDetail('fireball')

print(response.get_response('spellname', '3'))
