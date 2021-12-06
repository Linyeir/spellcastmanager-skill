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
    
    def __init__(self, intent_in, spell_name_in):
        self._intent = intent_in
        self._api_path = 'https://www.dnd5eapi.co/api/spells/'
        if spell_name_in is not None:
            self._spell_name = spell_name_in.replace(' ', '-')
        else:
            self._spell_name = 'empty'
            self._intent.log.warning('No Spellname specified')
        if self.api_reachable() == False:
            raise 'api not availlable on path'

    """
    returns true if api is reachable
    """
    def api_reachable(self):
        try:
            response = requests.get(self._api_path, timeout=5)
            response.raise_for_status()
            self._intent.log.info('api availlable')
            return True
        except requests.exceptions.HTTPError as errh:
            self._intent.log.exception(errh)
            return False
        except requests.exceptions.ConnectionError as errc:
            self._intent.log.exception(errc)
            return False
        except requests.exceptions.Timeout as errt:
            self._intent.log.exception(errt)
            return False
        except requests.exceptions.RequestException as err:
            self._intent.log.exception(err)
            return False

    """
    a robust api request
    - spellname is resolved by url since queries result in multiple results
    """
    def api_request(self, query=''):
        try:
            response = requests.get(self._api_path + self._spell_name, params=query, timeout=5)
            self._intent.log.exception(response)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            self._intent.log.exception(errh)
        except requests.exceptions.ConnectionError as errc:
            self._intent.log.exception(errc)
        except requests.exceptions.Timeout as errt:
            self._intent.log.exception(errt)
        except requests.exceptions.RequestException as err:
            self._intent.log.exception(err)


    """
    prepares a query result for reading
    """
    def clean_string(self, json_input):
        output_string = str(json_input).replace('[','').replace(']','').replace('"','').replace("'", '')
        return output_string 


    """
    returns the requested detail from the api
    - expects a tuple for "key"
    """
    def get_detail(self, key):
        if self._spell_name == 'empty':
            detail = 'empty'
        else:
            response = self.api_request()
            if response is not None:
                response_json = response.json()
                parsed_response = functools.reduce(dict.get, key, response_json)
                detail = self.clean_string(parsed_response)
            else:
                detail = 'empty'

        return detail