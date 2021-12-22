from src.response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer
from src.response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail

# noch abzufangen: slot/character level mittendrin aber ungültig

response = ResponseBuilderGetSingleDetail('fireball')

detail = response.get_response('school')

print(detail)

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