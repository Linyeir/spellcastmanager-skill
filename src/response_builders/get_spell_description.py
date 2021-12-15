
from response_builder_base import ResponseBuilderBase
from ..utils.Spell_class import Spell_class


class ResponseBuilderGetSpellDescription(ResponseBuilderBase):

    def __init__(self, spell_name: str):
        self._spell = Spell_class(spell_name)

    def get_response(self, detail: str, casting_level: str) -> dict:
        response = self._spell.desc
        return response
