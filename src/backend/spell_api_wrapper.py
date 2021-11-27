import requests
import json


"""
returns true if api is reachable
"""
def reachable():
    response = requests.get('https://www.dnd5eapi.co/api/spells/')
    if response.status_code == 200:
        return True
    else:
        return False

"""
a robust api request
- spellname is resolved by url since queries result in multiple results
"""
def robust_request(spell_name, query=''):
    try:
        response = requests.get('https://www.dnd5eapi.co/api/spells/'+spell_name, params=query, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


"""
prepares a query result for reading
"""
def clean_string(json_input):
    output_string = str(json_input).replace('[','').replace(']','').replace('"','').replace("'", '')
    return output_string 

"""
returns the full ruletext
- spell_name is reformattedt to match api format
- ruletext is requested from api
- ruletext is converted to a string and cleaned up
"""
def get_full_ruletext(spell_name):
    spell_name = spell_name.replace(' ', '-')
    response = robust_request(spell_name)
    if response is not None:
        response = response.json()
        ruletext = clean_string(response['desc'])
    else:
        ruletext = 'empty'

    return ruletext