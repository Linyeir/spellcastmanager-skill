from _typeshed import Self
from spell_api_wrapper import Spell_api_wrapper

class Spell():
    def __init__(self, intent_in, spell_name_in) -> None:
        self._api = Spell_api_wrapper(spell_name_in)
        self._fill_attributes()

    def _fill_attributes(self):
        self._name = self.api.get_detail(('name',))
        self._desc = self.api.get_detail(('desc',))
        self._higher_level = self.api.get_detail(('higher_level',))
        self._range = self.api.get_detail(('range',))
        self._components = self.api.get_detail(('components',)) #additional parsing necessary - complete
        self._material = self.api.get_detail(('material',))
        self._ritual = self.api.get_detail(('ritual',)) #additional parsing necessary - bool
        self._duration = self.api.get_detail(('duration',))
        self._concentration = self.api.get_detail(('concentration',)) #additional parsing necessary - bool
        self._casting_time = self.api.get_detail(('casting_time',))
        self._level = self.api.get_detail(('level',))
        self._attack_type = self.api.get_detail(('attack_type',))
        self._damage_type = self.api.get_detail(('damage', 'damage_type', 'name'))
        self._damage_at_slot_level = self.api.get_detail(('damage', 'damage_at_slot_level')) #additional parsing necessary - list 
        self._heal_at_slot_level = self.api.get_detail(('heal_at_slot_level',))             #additional parsing necessary - list
        self._damage_at_character_level = self.api.get_detail(('damage', 'damage_at_character_level'))
        self._heal_at_character_level = self.api.get_detail(('damage', 'heal_at_character_level'))
        self._dc_type = self.api.get_detail(('dc', 'dc_type', 'name'))
        self._dc_success = self.api.get_detail(('dc', 'dc_success'))
        self._area_of_effect_type = self.api.get_detail(('area_of_effect', 'type'))
        self._area_of_effect_size = self.api.get_detail(('area_of_effect', 'size'))
        self._school = self.api.get_detail(('school', 'name'))

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def higher_level(self):
        return self._higher_level

    @property
    def range(self):
        return self._range
    
    @property
    def components(self):
        return self._components

    @property
    def material(self):
        return self._material

    @property
    def ritual(self):
        return self._ritual

    @property
    def duration(self):
        return self._duration

    @property
    def concentration(self):
        return self._concentration

    @property
    def casting_time(self):
        return self._casting_time

    @property
    def level(self):
        return self._level

    @property
    def attack_type(self):
        return self._attack_type

    @property
    def damage_type(self):
        return self._damage_type

    @property
    def damage_at_slot_level(self):
        return self._damage_at_slot_level

    @property
    def heal_at_slot_level(self):
        return self._heal_at_slot_level

    @property
    def damage_at_character_level(self):
        return self._damage_at_character_level

    @property
    def heal_at_character_level(self):
        return self._heal_at_character_level

    @property
    def dc_type(self):
        return self._dc_type

    @property
    def dc_success(self):
        return self._dc_success

    @property
    def area_of_effect_type(self):
        return self._area_of_effect_type

    @property
    def area_of_effect_size(self):
        return self._area_of_effect_size

    @property
    def school(self):
        return self._school