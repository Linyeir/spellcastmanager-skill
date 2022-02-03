from .intent_base import IntentBase
from ..response_builders.response_builder_get_all_details import ResponseBuilderGetAllDetails
from ..utils.spell_categorizer import SpellCategorizer
from ..utils.exceptions.api_not_reachable_error import APINotReachableError
from ..utils.exceptions.no_spell_specified_error import NoSpellSpecifiedError
from ..utils.exceptions.invalid_spell_error import InvalidSpellError
from ..utils.detail_normalizer import DetailNormalizer


class IntentGetAllDetails(IntentBase):
    def __init__(self):
        pass        

    def execute(self, Spellcastmanager, message):
        try:
            spell_name_input = super()._extract_spell_name(message)
            self._response_builder = ResponseBuilderGetAllDetails(spell_name_input)
            Spellcastmanager.set_context('spellname', self._response_builder.spell.name)
            response = self._response_builder.get_response()
            spell_categorizer = SpellCategorizer(response)
            spell_category = spell_categorizer.get_categorie_from_details()
        except APINotReachableError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('api.not.reachable.error')
        except NoSpellSpecifiedError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('no.spell.specified.error')
        except InvalidSpellError as err:
            Spellcastmanager.log.error(err)
            Spellcastmanager.speak_dialog('invalid.spell.error', {'name': spell_name_input})
            Spellcastmanager.remove_context('spellname')
        else:
            dialog = 'get.all.details.category.' + str(spell_category)
            Spellcastmanager.speak_dialog(dialog, response)
            self._continue(Spellcastmanager)
#            IntentGetAllDetails.all_details_gui(self, Spellcastmanager, response)

    def _continue(self, Spellcastmanager):
        """
        prompts user for more questions
        """
        to_continue = Spellcastmanager.get_response('prompt.questions', {'name': self._response_builder.spell.name}, validator=self._validate_yes_no, on_fail='get.single.detail.request.repetition', num_retries=1)
        if to_continue == 'yes':
            Spellcastmanager.speak_dialog('what.do.you.want.to.know', expect_response=True)
        else:
            Spellcastmanager.speak_dialog('alright')
            Spellcastmanager.remove_context('spellname')
    
    def _validate_yes_no(self, response):
        if response == 'yes' or response == 'no':
            return True
        else:
            return False


    def all_details_gui(self, Spellcastmanager, response):

        """
        A function to parse the response on to a gui.
        The displayed webpage is written with Bootstrap.
        """

        rawhtml = """<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Help options</title>

<body class="bg-light">
    <div class="container mt-3">
        <div class="card p-4">
            <div class="row">
                <h2 class="col-sm-11">all details for
        """

        rawhtml = rawhtml + response["name"]

        rawhtml = rawhtml + """</h2>
                <image
                    src="https://camo.githubusercontent.com/0c736947847ed2b1bdc33782e55b6eceaf3e3a3b934a187983ebeef185b6d8a6/68747470733a2f2f7261772e6769746861636b2e636f6d2f466f7274417765736f6d652f466f6e742d417765736f6d652f6d61737465722f737667732f736f6c69642f646963652d6432302e737667"
                    width="20" class="col-sm-1" />

            </div>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">attribute</th>
                        <th scope="col">value</th>
                    </tr>
                </thead>"""

        """?????
        for every attribute:
            rawhtml = rawhtml + ""<tbody>
                    <td>$attribute</td>
                    <td>$value</td>
                </tbody>

        """
        response.pop("name")

        for entry in response:

            rawhtml = rawhtml + """ <tbody>
                        <td>"""

            dn = DetailNormalizer()
            rawhtml = rawhtml + dn.get_spoken_attribute(entry)            

            rawhtml = rawhtml + """
            </td>
                        <td>"""

            rawhtml = rawhtml + response[entry]
            rawhtml = rawhtml + """</td >
                    </tbody>

            """

        rawhtml = rawhtml + """
            </table>
        </div>
    </div>
</body>

</html>"""

        Spellcastmanager.gui.show_html(rawhtml)
