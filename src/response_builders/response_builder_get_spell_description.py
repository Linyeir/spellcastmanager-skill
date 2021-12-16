
from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from src.utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderGetSpellDescription(ResponseBuilderBase):

    def __init__(self, spell_name: str):
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    def get_response(self) -> dict:
        response = {'desc': self._spell.desc}
        return response
