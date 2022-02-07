import requests
import functools
from .exceptions.api_not_reachable_error import APINotReachableError
from .exceptions.invalid_spell_error import InvalidSpellError
from .exceptions.no_spell_specified_error import NoSpellSpecifiedError


class APIWrapper():
    """
    A wrapper for the api on https://www.dnd5eapi.co/api/
    Only the spells/directory is used

    Usage:
        - Instantiate inside of your intent
        - get a detail via the get detail methode
    """

    def __init__(self, spell_name_in):
        """
        parses the spells name, converts it to a form, that is suitable ro query the api, and than executes the query
        If no spell name is passed, an error is raised
        """
        self._api_path = 'https://www.dnd5eapi.co/api/spells/'
        if spell_name_in is None:
            raise NoSpellSpecifiedError()
        self._spell_name = spell_name_in.replace(' ', '-').lower()
        if self.api_reachable():
            self._response = self.api_request()


    def api_reachable(self):
        """
        returns true if api is reachable
        """

        try:
            response = requests.get(self._api_path, timeout=3)
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as errh:
            raise APINotReachableError(errh)
        except requests.exceptions.ConnectionError as errc:
            raise APINotReachableError(errc)
        except requests.exceptions.Timeout as errt:
            raise APINotReachableError(errt)
        except requests.exceptions.RequestException as err:
            raise APINotReachableError(err)


    def api_request(self, query=''):
        """
        a robust api request
        - spellname is resolved by url since queries result in multiple results
        """

        try:
            response = requests.get(
                self._api_path + self._spell_name, params=query, timeout=3)
            response.raise_for_status()
            return response
        except:
            raise InvalidSpellError(self._spell_name)


    def get_detail(self, key):
        """
        returns the requested detail from the api
        - expects a tuple for "key"
        - if required, an index-/ range can be passed
        """

        response_json = self._response.json()
        try:
            parsed_response = functools.reduce(dict.get, key, response_json)
        except:
            parsed_response = 'empty'
        if parsed_response is None:
            parsed_response = 'empty'
        return parsed_response
