Feature: spellcast manager read ruletext

    # - different existing spells
    # - different utterances
    Scenario Outline: request ruletext with existing spell
        Given an english speaking user
         When the user says "<request_ruletext_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "<get_description_dialogs>"

    Examples: request ruletext with existing spell
        | request_ruletext_with_existing_spell                          | get_description_dialogs       |
        | Give me the ruletext for the spell fireball                   | get.spell.description.dialog  |  
        | no                                                            | alright.dialog                |
        | Tell me the rules for the spell healing word                  | get.spell.description.dialog  |
        | no                                                            | alright.dialog                |
        | Give me a description for the spell chain lightning           | get.spell.description.dialog  |
        | no                                                            | alright.dialog                |
        | description of the spell finger of death                      | get.spell.description.dialog  |
        | no                                                            | alright.dialog                |


    # - different not existing spells
    # - different utterances
    Scenario Outline: request ruletext with invalid spells
        Given an english speaking user
         When the user says "<request_ruletext_with_invalid_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "invalid.spell.error.dialog"

    Examples: request ruletext with invalid spell
        | request_ruletext_with_invalid_spell           |
        | Give me the ruletext for the spell avocado    |
        | Tell me the rules for the spell help          |
        | Give me a description for the spell hass      |
        | description of the spell asdf                 |
        | describe the spell schadenfreude              |
        | Read me the ruletext for the spell gr??nkohl   |
        | ruletext for the spell frodo                  |
        | rules for the spell hallo                     |
        | What does the spell morgenrot do              |
        | What does the spell wdvierzig do exactly      |
        | What is the spell gelbfieber exactly          |
        | What is the spell alte zwiebeln               |
        | Describe the spell purple bolt of hatred      |
        | Explain the spell saurer regen                |
        | Tell me about the spell climate change        |



    # - no spell mentioned
    # - different utterances
    Scenario Outline: request ruletext without stating spell
        Given an english speaking user
         When the user says "<request_ruletext_without_stating_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "no.spell.specified.error.dialog"

    Examples: request ruletext without stating spell
        | request_ruletext_without_stating_spell        |
        | What does the spell do                        |
        | Explain the spell                             |
        | Long ruletext for the spell                   |
        | Tell me about the spell                       |





