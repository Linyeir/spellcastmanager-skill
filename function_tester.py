from mycroft.util.parse import extract_number
import lingua_franca
from src.response_builders.response_builder_invoke_casting_assistant import ResponseBuilderInvokeCastingAssistant
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer


def testo(input):
    if input == 1:
        return input
    else:
        return False

if (testo(0) != False):
    print(testo(1))
else:
    print(testo(0))

