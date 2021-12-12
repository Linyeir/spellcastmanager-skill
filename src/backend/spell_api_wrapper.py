import requests
import json
import functools


"""
A wrapper for the api on https://www.dnd5eapi.co/api/
Only the spells/directory is used 

Usage:
    - Instantiate inside of your intent 
    - get a detail via the get detail methode
"""
class Spell_api_wrapper():
    
    def __init__(self, spell_name_in):
        self._api_path = 'https://www.dnd5eapi.co/api/spells/'
        if spell_name_in is not None:
            self._spell_name = spell_name_in.replace(' ', '-')
        else:
            self._spell_name = 'empty'
        self._api_reachable = self.api_reachable()
        if self._api_reachable:
            self.response = self.api_request()
        else:
            raise 'api not availlable on path'
        

    """
    returns true if api is reachable
    """
    def api_reachable(self):
        try:
            response = requests.get(self._api_path, timeout=3)
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as errh:
            return False
        except requests.exceptions.ConnectionError as errc:
            return False
        except requests.exceptions.Timeout as errt:
            return False
        except requests.exceptions.RequestException as err:
            return False

    """
    a robust api request
    - spellname is resolved by url since queries result in multiple results
    """
    def api_request(self, query=''):
        try:
            response = requests.get(self._api_path + self._spell_name, params=query, timeout=5)
            response.raise_for_status()
            return response

        # for later to implement !!!                ###############################################################
        except requests.exceptions.HTTPError as errh:
            pass
        except requests.exceptions.ConnectionError as errc:
            pass
        except requests.exceptions.Timeout as errt:
            pass
        except requests.exceptions.RequestException as err:
            pass


    """
    returns the requested detail from the api
    - expects a tuple for "key"
    - if required, an index-/ range can be passed
    """
    def get_detail(self, key):
        if (self._spell_name == 'empty') or (not self._api_reachable):
            parsed_response = 'empty'
        else:
            if self.response is not None:
                response_json = self.response.json()
                parsed_response = functools.reduce(dict.get, key, response_json)
                if parsed_response is None:
                    parsed_response = 'empty'
            else:
                parsed_response = 'empty'

        return parsed_response