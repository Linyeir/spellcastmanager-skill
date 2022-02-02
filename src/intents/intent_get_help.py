from pickle import TRUE
from .intent_base import IntentBase

class IntentGetHelp(IntentBase):
    def __init__(self):
        pass

    def execute(self, Spellcastmanager, message):

        rawhtml="""<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Help options</title>

<body>
    <div class="container mt-3 ">
        <h2>spellcast manager help options</h2>
        <div class="card bg-light text-dark">
            <div class="card-header">Option 1</div>
            <div class="card-body">You can generally ask about a specific spell.'</div>
        </div>
        <br>
        <div class="card bg-light text-dark">
            <div class="card-header">Option 2</div>
            <div class="card-body">You can ask for specific details regarding a spell.</div>
        </div>
        <br>
        <div class="card bg-light text-dark">
            <div class="card-header">Option 3</div>
            <div class="card-body">You can ask for all details i have about a spell</div>
        </div>
        <br>
        <div class="card bg-light text-dark">
            <div class="card-header">Option 4</div>
            <div class="card-body">The spellcast manager can guide you through the casting of a specific spell</div>
        </div>
    </div>
</body>

</html>
"""

        """Spellcastmanager.gui.show_image("https://raw.githubusercontent.com/Linyeir/spellcastmanager-skill/feature_gui/src/icon.png")"""
        Spellcastmanager.gui.show_html(rawhtml)

        terminate_help = False;
        Spellcastmanager.speak_dialog('help.get')

        while not terminate_help:

            options = ['You can generally ask about a specific spell',
                        'You can ask for specific details regarding a spell.',
                        'You can ask for all details i have about a spell',
                        'The spellcast manager can guide you through the casting of a specific spell']

            selection = Spellcastmanager.ask_selection(options, 'help.post.option')

            if selection == options[0]:
                Spellcastmanager.speak_dialog('help.option.all')        
            elif selection == options[1]:
                Spellcastmanager.speak_dialog('help.option.assistant')
            elif selection == options[2]:
                Spellcastmanager.speak_dialog('help.option.description')            
            elif selection == options[3]:
                Spellcastmanager.speak_dialog('help.option.detail')

            further_help = Spellcastmanager.ask_yesno('help.continue') 

            if further_help == 'no':
                  terminate_help = True

        Spellcastmanager.speak_dialog('help.terminate')