
from response_builder_base import ResponseBuilderBase
from ..utils.Spell_class import Spell_class

class ResponseBuilderGetSpellDescription(ResponseBuilderBase):

    def get_response(detail: str, casting_level: str) -> dict:
        
        return super().get_response(casting_level)

    def build_full_ruletext(spell_name_in):
        spell = Spell_class(spell_name_in)
        response = ''

        if spell.name == 'empty':
            return 'no spell'
        else:
            if spell.desc != 'empty':
                response = spell.desc
            else:
                response = 'No description found'
        return response