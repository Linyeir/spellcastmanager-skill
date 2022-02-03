
from .response_builder_base import ResponseBuilderBase
from ..utils.spell import Spell
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError


class ResponseBuilderGetSpellDescription(ResponseBuilderBase):
    """
    validates user input (spell name) and formats response fitting for dialog file
    """
    def __init__(self, spell_name: str):
        """
        validates spell name and builds class spell
        """
        if spell_name is None:
            raise NoSpellSpecifiedError()
        self._spell = Spell(spell_name)

    def get_response(self) -> dict:
        """
        fills response with content from description attribute
        """
        response = {'desc': self._spell.desc}
        return response


    @property
    def spell(self):
        return self._spell
