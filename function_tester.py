from mycroft.util.parse import extract_number
import lingua_franca
from src.response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer
from src.response_builders.response_builder_get_single_detail import ResponseBuilderGetSingleDetail
from src.utils.detail_normalizer import DetailNormalizer


rb = ResponseBuilderInvokeCastingAssistant('healing word')
print(rb.get_casting_level_type())
print(rb.get_casting_level_limits())
print(rb.get_value_at_casting_level(5))

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