from mycroft.util.parse import extract_number
import lingua_franca
from src.response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer


rb = ResponseBuilderInvokeCastingAssistant('healing word')
print(rb.get_casting_level_type())
print(rb.get_casting_level_limits())
print(rb.get_value_at_casting_level(5))

