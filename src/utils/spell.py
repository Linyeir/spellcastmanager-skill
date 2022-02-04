import ast
from .api_wrapper import APIWrapper


class Spell():
    """
    If instantiated with a valid spellname, this class provides an easy way to access the spells details.
    """
    def __init__(self, spell_name_in) -> None:
        self._api = APIWrapper(spell_name_in)
        self._fill_attributes()

    
    def _clean_string(self, json_input):
        """
        prepares a query result for reading
        """
        output_string = str(json_input).replace(
            '[', '').replace(']', '').replace('"', '').replace("'", '')
        return output_string

    def _fill_attributes(self):
        self.name = self._api.get_detail(('name',))
        self.desc = self._api.get_detail(('desc',))
        self.higher_level = self._api.get_detail(('higher_level',))
        self.range = self._api.get_detail(('range',))
        self.components = self._api.get_detail(('components',))
        self.material = self._api.get_detail(('material',))
        self.ritual = self._api.get_detail(('ritual',))
        self.duration = self._api.get_detail(('duration',))
        self.concentration = self._api.get_detail(('concentration',))
        self.casting_time = self._api.get_detail(('casting_time',))
        self.level = self._api.get_detail(('level',))
        self.attack_type = self._api.get_detail(('attack_type',))
        self.damage_type = self._api.get_detail(('damage', 'damage_type', 'name'))
        self.damage_at_slot_level = self._api.get_detail(('damage', 'damage_at_slot_level'))  # additional parsing necessary - list
        self.damage_at_slot_level = self._rephrase_effect_modifiers(self.damage_at_slot_level)
        self.heal_at_slot_level = self._api.get_detail(('heal_at_slot_level',))  # additional parsing necessary - list
        self.heal_at_slot_level = self._rephrase_effect_modifiers(self.heal_at_slot_level)
        self.damage_at_character_level = self._api.get_detail(('damage', 'damage_at_character_level'))
        self.damage_at_character_level = self._rephrase_effect_modifiers(self.damage_at_character_level)
        self.heal_at_character_level = self._api.get_detail(('heal_at_character_level',))
        self.heal_at_character_level = self._rephrase_effect_modifiers(self.heal_at_character_level)
        self.dc_type = self._rephrase_saving_throw_type(self._api.get_detail(('dc', 'dc_type', 'name')))
        self.dc_success = self._api.get_detail(('dc', 'dc_success'))
        self.area_of_effect_type = self._api.get_detail(('area_of_effect', 'type'))
        self.area_of_effect_size = self._api.get_detail(('area_of_effect', 'size'))
        self.school = self._api.get_detail(('school', 'name'))


    def _rephrase_saving_throw_type(self, saving_throw_input):
        """
        rephrases the saving throw types to increase readability
        """

        if saving_throw_input == 'DEX':
            saving_throw_output = saving_throw_input.replace('DEX', 'Dexterity')
        elif saving_throw_input == 'STR':
            saving_throw_output = saving_throw_input.replace('STR', 'Strength')
        elif saving_throw_input == 'CON':
            saving_throw_output = saving_throw_input.replace('CON', 'Constitution')
        elif saving_throw_input == 'WIS':
            saving_throw_output = saving_throw_input.replace('WIS', 'Wisdom')
        elif saving_throw_input == 'INT':
            saving_throw_output = saving_throw_input.replace('INT', 'Intelligence')
        elif saving_throw_input == 'CHA':
            saving_throw_output = saving_throw_input.replace('CHA', 'Charisma')
        else: 
            saving_throw_output = saving_throw_input
        return saving_throw_output


    def _rephrase_effect_modifiers(self, input_string):
        """
        rephrases MOD to your Modifiers to increase readability
        """

        value_dict = input_string
        if type(value_dict) is dict: 
            for entry in value_dict.keys():
                if 'MOD' in value_dict[entry]:
                    value_dict[entry] = value_dict[entry].replace('MOD', 'your Modifiers')
        return value_dict
        


# region properties

    # string


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._clean_string(value)

    # string

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = self._clean_string(value)

    # string

    @property
    def higher_level(self):
        return self._higher_level

    @higher_level.setter
    def higher_level(self, value):
        self._higher_level = self._clean_string(value)

    # string
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = self._clean_string(value)

    # list
    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if value != 'empty':
            new_value = ''
            for entry in value:
                if entry == 'V':
                    new_entry = entry.replace('V', 'verbal,')

                if entry == 'S':
                    new_entry = entry.replace('S', 'somatic,')

                if entry == 'M':
                    new_entry = entry.replace('M', 'material')

                new_value = new_value + new_entry + ' '
            self._components = new_value
        else:
            self._components = 'empty'

    # string

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = self._clean_string(value)

    # bool
    @property
    def ritual(self):
        return self._ritual

    @ritual.setter
    def ritual(self, value):
        self._ritual = value

    # string
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = self._clean_string(value)

    # bool
    @property
    def concentration(self):
        return self._concentration

    @concentration.setter
    def concentration(self, value):
        self._concentration = value

    # string
    @property
    def casting_time(self):
        return self._casting_time

    @casting_time.setter
    def casting_time(self, value):
        self._casting_time = self._clean_string(value)

    # string
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self._clean_string(value)

    # string
    @property
    def attack_type(self):
        return self._attack_type

    @attack_type.setter
    def attack_type(self, value):
        self._attack_type = self._clean_string(value)

    # string
    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value):
        self._damage_type = self._clean_string(value)

    # dict
    @property
    def damage_at_slot_level(self):
        return self._damage_at_slot_level

    @damage_at_slot_level.setter
    def damage_at_slot_level(self, value):
        self._damage_at_slot_level = value

    # dict
    @property
    def heal_at_slot_level(self):
        return self._heal_at_slot_level

    @heal_at_slot_level.setter
    def heal_at_slot_level(self, value):
        self._heal_at_slot_level = value

    # dict
    @property
    def damage_at_character_level(self):
        return self._damage_at_character_level

    @damage_at_character_level.setter
    def damage_at_character_level(self, value):
        self._damage_at_character_level = value

    # dict
    @property
    def heal_at_character_level(self):
        return self._heal_at_character_level

    @heal_at_character_level.setter
    def heal_at_character_level(self, value):
        self._heal_at_character_level = value

    # string
    @property
    def dc_type(self):
        return self._dc_type

    @dc_type.setter
    def dc_type(self, value):
        self._dc_type = self._clean_string(value)

    # string
    @property
    def dc_success(self):
        return self._dc_success

    @dc_success.setter
    def dc_success(self, value):
        self._dc_success = self._clean_string(value)

    # string
    @property
    def area_of_effect_type(self):
        return self._area_of_effect_type

    @area_of_effect_type.setter
    def area_of_effect_type(self, value):
        self._area_of_effect_type = self._clean_string(value)

    # string
    @property
    def area_of_effect_size(self):
        return self._area_of_effect_size

    @area_of_effect_size.setter
    def area_of_effect_size(self, value):
        self._area_of_effect_size = self._clean_string(value)

    # string
    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = self._clean_string(value)

# endregion
