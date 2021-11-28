# several tests for long ruletext

Feature: spellcast manager read long ruletext

    # - different existing spells
    # - different utterances
    Scenario Outline: request long ruletext with existing spell
        Given an englisch speaking user
         When the user says "<request_long_ruletext_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with "long.ruletext.dialog"

    Examples: request long ruletext with existing spell     
        | request_long_ruletext_with_existing_spell     |
        | Give me the full ruletext for fireball        |       
        | Give me the whole description for fireball    |
        | Long description of finger of death           |
        | What does divine favor do in detail           |
        | Long ruletext for eldritch blast              |
        | Long rules for druidcraft                     |


    # - different not existing spells
    # - different utterances
    Scenario Outline: request long ruletext with invalid spells
        Given an englisch speaking user
         When ther user says "<request_long_ruletext_with_invalid_spell>"
         Then "spellcastmanager-skill" should reply with "ruletext.invalid.spell.dialog"

    Examples: request long ruletext with invalid spell            
        | request_long_ruletext_with_invalid_spell      |  
        | Give me the whole description for acid cloud  |
        | Long description of banish                    |
        | What does fire do in detail                   |
        | Long ruletext for kill                        |
        | Long rules for hall                           |



    # - no spell mentioned
    # - different utterances
    Scenario Outline: request without spell
        Given an englisch speaking user
         When the user says "give me the long ruletext for"
         Then "spellcastmanager-skill" should reply with "You have to specify a spell"

    Examples: request long ruletext without stating spell       
        | request_long_ruletext_without_stating_spell   |
        | give me the long ruletext for                 |
        | Give me a long ruletext                       |
        | Long ruletext for                             |
        | Explain the full rules                        |





