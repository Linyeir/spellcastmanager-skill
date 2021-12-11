from spell_api_wrapper import Spell_api_wrapper

class Spell_class():
    def __init__(self, spell_name_in) -> None:
        self._api = Spell_api_wrapper(spell_name_in)
        self._fill_attributes()


    def _fill_attributes(self):
        self._name = self._api.get_detail(('name',))
        self._desc = self._api.get_detail(('desc',))
        self._higher_level = self._api.get_detail(('higher_level',))
        self._range = self._api.get_detail(('range',))
        self._components = self._api.get_detail(('components',))
        self._material = self._api.get_detail(('material',))
        self._ritual = self._api.get_detail(('ritual',))
        self._duration = self._api.get_detail(('duration',))
        self._concentration = self._api.get_detail(('concentration',))
        self._casting_time = self._api.get_detail(('casting_time',))
        self._level = self._api.get_detail(('level',))
        self._attack_type = self._api.get_detail(('attack_type',))
        self._damage_type = self._api.get_detail(('damage', 'damage_type', 'name'))
        self._damage_at_slot_level = self._api.get_detail(('damage', 'damage_at_slot_level')) #additional parsing necessary - list 
        self._heal_at_slot_level = self._api.get_detail(('heal_at_slot_level',))             #additional parsing necessary - list
        self._damage_at_character_level = self._api.get_detail(('damage', 'damage_at_character_level'))
        self._heal_at_character_level = self._api.get_detail(('damage', 'heal_at_character_level'))
        self._dc_type = self._api.get_detail(('dc', 'dc_type', 'name'))
        self._dc_success = self._api.get_detail(('dc', 'dc_success'))
        self._area_of_effect_type = self._api.get_detail(('area_of_effect', 'type'))
        self._area_of_effect_size = self._api.get_detail(('area_of_effect', 'size'))
        self._school = self._api.get_detail(('school', 'name'))


    


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


    @property
    def higher_level(self):
        return self._higher_level

    @higher_level.setter
    def higher_level(self, value):
        self._higher_level = value


    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value


    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        for entry in value:
            if entry == 'V':
                entry = 'verbal'
            
            if entry == 'S':
                entry = 'somatic'

            if entry == 'M':
                entry = 'material'

        self._components = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value 


    @property
    def ritual(self):              
        return self._ritual

    @ritual.setter
    def ritual(self, value):
        self._ritual = value


    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value


    @property
    def concentration(self):
        return self._concentration

    @concentration.setter
    def concentration(self, value):
        self._concentration = value


    @property
    def casting_time(self):
        return self._casting_time

    @casting_time.setter
    def casting_time(self, value):
        self._casting_time = value


    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value


    @property
    def attack_type(self):
        return self._attack_type

    @attack_type.setter
    def attack_type(self, value):
        self._attack_type = value


    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value):
        self._damage_type = value


    @property
    def damage_at_slot_level(self):
        return self._damage_at_slot_level

    @damage_at_slot_level.setter
    def damage_at_slot_level(self, value):
        self._damage_at_slot_level = value


    @property
    def heal_at_slot_level(self):
        return self._heal_at_slot_level

    @heal_at_slot_level.setter
    def heal_at_slot_level(self, value):
        self._heal_at_slot_level = value


    @property
    def damage_at_character_level(self):
        return self._damage_at_character_level

    @damage_at_character_level.setter
    def damage_at_character_level(self, value):
        self._damage_at_character_level = value


    @property
    def heal_at_character_level(self):
        return self._heal_at_character_level

    @heal_at_character_level.setter
    def heal_at_character_level(self, value):
        self._heal_at_character_level = value


    @property
    def dc_type(self):
        return self._dc_type

    @dc_type.setter
    def dc_type(self, value):
        self._dc_type = value


    @property
    def dc_success(self):
        return self._dc_success

    @dc_success.setter
    def dc_success(self, value):
        self._dc_success = value


    @property
    def area_of_effect_type(self):
        return self._area_of_effect_type

    @area_of_effect_type.setter
    def area_of_effect_type(self, value):
        self._area_of_effect_type = value


    @property
    def area_of_effect_size(self):
        return self._area_of_effect_size

    @area_of_effect_size.setter
    def area_of_effect_size(self, value):
        self._area_of_effect_size = value


    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value


spell = Spell_class('fireball')

print(type(spell.damage_at_slot_level))
print(spell.damage_at_slot_level)