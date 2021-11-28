Feature: spellcast manager read long ruletext

    # - different existing spells
    # - different utterances
    Scenario Outline: request long ruletext with existing spell
        Given an english speaking user
         When the user says "<request_long_ruletext_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "long.ruletext.dialog"

    Examples: request long ruletext with existing spell     
        | request_long_ruletext_with_existing_spell         |
        | Give me the full ruletext for fireball            |
        | Give me the detailed ruletext for light           | 
        | Tell me the whole ruletext for healing word       |      
        | Give me the whole description for chain lightning |
        | Long description of finger of death               |
        | Tell me the long spelltext for incendiary cloud   |
        | Long ruletext for eldritch blast                  |
        | Long rules for druidcraft                         |
        | What does divine favor do in detail               |
        | What does revivify do exactly                     |
        | What is fireball exactly                          |


    # - different not existing spells
    # - different utterances
    Scenario Outline: request long ruletext with invalid spells
        Given an english speaking user
         When the user says "<request_long_ruletext_with_invalid_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "ruletext.invalid.spell.dialog"

    Examples: request long ruletext with invalid spell            
        | request_long_ruletext_with_invalid_spell      |  
        | Give me the whole description for acid cloud  |
        | Long description of banish                    |
        | What does fire do in detail                   |
        | Long ruletext for kill                        |
        | Long rules for hall                           |



    # - no spell mentioned
    # - different utterances
    Scenario: request without spell
        Given an english speaking user
         When the user says "request_long_ruletext_without_stating_spell"
         Then "spellcastmanager-skill" should reply with dialog from "ruletext.fallback.dialog"

#    Examples: request long ruletext without stating spell       
#        | request_long_ruletext_without_stating_spell   |
#        | give me the long ruletext for                 |
#        | Give me a long ruletext                       |
#        | Long ruletext for                             |
#        | Explain the full rules                        |





