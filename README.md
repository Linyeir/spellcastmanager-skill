# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/dice-d20.svg" card_color="#D81159" width="50" height="50" style="vertical-align:bottom"/> Spellcastmanager

Helps you with spellcasting in D&D 5e

## About

Guide you through casting a spell in the 5th edition of dungeons and dragons
uses this api: https://www.dnd5eapi.co/ from u/adrpadua

## Examples

- "Start spellcast manager"
- "Open spellcast manager"

## Credits

Linyeir
RobinRother
AlexandraSchmalz

## Category

**Entertainment**

## Tags

#Spellcast
#D&d
#Dungeons
#Dragons
#5e

# rules

- we use drawIo, when applicable for illustrations
- we use the feature branch workflow for version control (see doc/featureBranchWorkflow.drawio)
- we use the english language for coding, utterances and assistant language support to avoid compatibility issues (with mycoft)

# list of intents

- skillStartIntent (starts the skill and provides short explanation)
- skillTerminationIntent (ends the skill)
- helpIntent (explains every other intent)
- repeatHelpSubIntent (allows the user to ask again about a specific skill)
- fullRuleTextIntent (reads the full ruletext for the specified spell)
- shortRuleTextIntent (reads a resumee of the ruletext for the specified spell)
- ruleDetailSubIntent (allows the user to ask again about rule details for the earlier specified spell)
- ruleDetailIntent (allows the user to ask again about rule details for the specified spell)
- basicCastingRulesIntent (explains how spellcasting works in D&D 5e)
- castingExamplesSubIntent (provides an optional example to the basicCastingRulesIntent)
- listFilteredSpellsIntent (reads a filtered list of spells)
- spellAssistantIntent (guides the user through the casting of a spell)
- rollForMeIntent (rolls dice for the user)
- [repeat intent] (repeats the last intent)

consult doc/intent_diagram.drawio to learn about the intent structure

the respective utterances are documented in doc/utterances.md
