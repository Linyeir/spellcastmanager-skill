from ..utils.exceptions.invalid_spell_category_error import InvalidSpellCategoryError


"""
A class that holds a list of detail configurations which can be compared with the passed dict
"""
class SpellCategorizer():

    def __init__(self, details):
        self._detail_list = list(details.keys())
        self._categories = {0: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'attack_type', 'area_of_effect_type', 'area_of_effect_size', 'dc_type', 'dc_success'],
            1: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'attack_type', 'area_of_effect_type', 'area_of_effect_size'], 
            2: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'attack_type', 'dc_type', 'dc_success'],  
            3: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'attack_type'],    
            4: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'area_of_effect_type', 'area_of_effect_size', 'dc_type', 'dc_success'], 
            5: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'area_of_effect_type', 'area_of_effect_size'],  
            6: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level', 'dc_type', 'dc_success'],  
            7: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'at_casting_level', 'min_casting_level', 'max_casting_level'],     
            8: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'attack_type', 'area_of_effect_type', 'area_of_effect_size', 'dc_type', 'dc_success'],   
            9: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'attack_type', 'area_of_effect_type', 'area_of_effect_size'],     
            10: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'attack_type', 'dc_type', 'dc_success'],     
            11: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'attack_type'],      
            12: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'area_of_effect_type', 'area_of_effect_size', 'dc_type', 'dc_success'],   
            13: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'area_of_effect_type', 'area_of_effect_size'],      
            14: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level', 'dc_type', 'dc_success'],     
            15: ['name', 'school', 'level', 'components', 'material', 'ritual', 'concentration', 'casting_time', 'duration', 'range', 'damage_type', 'higher_level']}  


    """
    converts the passed detail dict and the list of detail dicts into sets, compares them, and when they match, it returns the number of the matched list of details
    """
    def get_categorie_from_details(self)-> int:
        category = None
        for category_number in self._categories.keys():
            if set(self._categories[category_number]) == set(self._detail_list):
                category = category_number
                
        if category is None:
            print(self._detail_list)
            raise InvalidSpellCategoryError(self._detail_list)

        return category


   