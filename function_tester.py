from src.response_builders.response_builder_get_spell_description import ResponseBuilderGetSpellDescription
from src.response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from src.utils.exceptions.invalid_spell_error import InvalidSpellError
from src.utils.spell_categorizer import SpellCategorizer



response = ResponseBuilderGetAllDetails('fireball')
details = response.get_response()

spell_categorizer = SpellCategorizer(details)
spell_category = spell_categorizer.get_categorie_from_details()
print(spell_category)

