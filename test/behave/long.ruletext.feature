# several tests for long ruletext

Feature: read long ruletext

    # - different existing spells
    # - different utterances
    Scenario Outline: read ruletext for existing spells
        Given an englisch speaking user
         When the user says "<request_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with "long.ruletext.dialog"

    Examples: request long ruletext             # table heading
        | request_with_existing_spell                   |       # column name
        | Give me the whole description for fireball    |
        | Long description of finger of death           |
        | What does divine favor do in detail           |
        | Long ruletext for eldritch blast              |
        | Long rules for druidcraft                     |



    # - different not existing spells
    # - different utterances
    Scenario Outline: no ruletext for not existing spells
        Given an englisch speaking user
         When ther user says "<request_with_not_existing_spell>"
         Then "spellcastmanager-skill" should reply with ""

    Examples: request long ruletext             # table heading
        | request_with_not_existing_spell               |       # column name
        | Give me the whole description for acid cloud  |
        | Long description of banish                    |
        | What does fire do in detail                   |
        | Long ruletext for kill                        |
        | Long rules for hall                           |



    # - no spell mentioned
    # - different utterances
    Scenario Outline: request without spell
        Given an englisch speaking user
         When the user says "<>"
         Then "spellcastmanager-skill" should reply with "ruletext.fallback.dialog"

    Examples: request long ruletext
        | request_without_spell     |
        | Give me a long ruletext   |
        | Long ruletext for         |
        | Explain the full rules    |