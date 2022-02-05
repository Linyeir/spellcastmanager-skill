import padatious

intent_container = padatious.IntentContainer('/opt/mycroft/skills/spellcastmanager-skill/temp_pad')

traing_utterances = ['what does spellcastmanager do',
    'what does the spellcast manager do',
    'what does spellcastmanager',
    'what can i do with spellcastmanager',
    'i need assistance with spellcastmanager',
    'i need help with the spellcastmanager',
    'how do i use the spellcastmanager',
    'spellcastmanager help',
    'spellcatmanager help please']


test_utterances = ['what does spellcastmanager do',
    'spellcastmanager help',
    'What do I do with spellcastmanager',
    'help',
    'Spellcastmanager',
    'help Spell',
    'I would very much like some assistance please',
    'I need assistance',
    'How does this Thing work',
    'What ca i do wit this spellcast manager thing']

intent_container.add_intent('help', traing_utterances, False)
intent_container.train()

for entry in test_utterances:
    entry_dict = intent_container.calc_intent(entry)
    print(entry_dict)


"""
results:
{'name': 'help', 'sent': ['what', 'does', 'spellcastmanager', 'do'], 'matches': {}, 'conf': 1.0}
{'name': 'help', 'sent': ['spellcastmanager', 'help'], 'matches': {}, 'conf': 1.0}
{'name': 'help', 'sent': 'what do i do with spellcastmanager', 'matches': {}, 'conf': 0.6713903771722669}
{'name': 'help', 'sent': 'help', 'matches': {}, 'conf': 0.15896761847554391}
{'name': 'help', 'sent': 'spellcastmanager', 'matches': {}, 'conf': 0.6723280620590926}
{'name': 'help', 'sent': 'help spell', 'matches': {}, 'conf': 0.0}
{'name': 'help', 'sent': 'i would very much like some assistance please', 'matches': {}, 'conf': 0.46033088961031177}
{'name': 'help', 'sent': 'i need assistance', 'matches': {}, 'conf': 0.4247065028681306}
{'name': 'help', 'sent': 'how does this thing work', 'matches': {}, 'conf': 0.3328145787693864}
{'name': 'help', 'sent': 'what ca i do wit this spellcast manager thing', 'matches': {}, 'conf': 0.5288085702631974}
"""


