from mycroft.util.parse import match_one


class DetailNormalizer():
    """
    matches spoken attributes to written attribute name
    """
    def __init__(self):
        """
        initializes lists of spoken and written attribute names
        """
        self._spoken_attribute_names = ['name', 'description', 'higher level', 'range', 'components', 'material', 'ritual', 'duration', 'concentration', 'casting time', 'level', 'attack type', 'damage type', 'effect at casting level', 'damage at slot level', 'damage at character level', 'heal at slot level', 'heal at character level', 'minimum casting level', 'maximum casting level', 'minimum casting level', 'maximum casting level', 'saving throw type', 'saving throw success', 'area of effect type', 'area of effect size', 'school']
        self._attribute_names = ['name', 'desc', 'higher_level', 'range', 'components', 'material', 'ritual', 'duration', 'concentration', 'casting_time', 'level', 'attack_type', 'damage_type', 'at_casting_level', 'damage_at_slot_level', 'damage_at_character_level', 'heal_at_slot_level', 'heal_at_character_level', 'min_casting_level', 'max_casting_level', 'min_casting_level', 'max_casting_level', 'dc_type', 'dc_success', 'area_of_effect_type', 'area_of_effect_size', 'school']


    def match_spoken_detail_to_attribute(self, detail_input):
        """
        matches spoken attributes to written attribute name
        """
        matched_spoken_detail = match_one(detail_input, self._spoken_attribute_names)
        detail_index = self._spoken_attribute_names.index(matched_spoken_detail[0])
        attribute = self._attribute_names[detail_index]

        return attribute

    def get_spoken_attribute(self, attribute) -> str:
        """
        return the spoken attribute for a given technical description
        """

        attribute_map = dict(zip(self._attribute_names, self._spoken_attribute_names))

        readable_attribute = attribute_map.get(attribute)

        if readable_attribute is not None:
            return readable_attribute
        else:
            return 'NA'
