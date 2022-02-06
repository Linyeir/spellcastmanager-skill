Feature: spellcast manager invoke casting assistant

    Scenario Outline: invoke casting assistant with existing spell
        Given an english speaking user
         When the user says "<invoke_casting_assistance_for_specific_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "<invoke_casting_assistant_dialogs>"

    Examples: invoke casting assistance for specific spell            
        | invoke_casting_assistance_for_specific_spell                          | invoke_casting_assistant_dialogs      |
        | i cast the spell fireball                                             | choose.spellslot.dialog               |
        | 3                                                                     | inflict.aoe.damage.dialog             |
        | i summon the spell shocking grasp                                     | choose.characterlevel.dialog          |
        | 1                                                                     | inflict.damage.dialog                 |
        | We conjure the spell bless                                            | has.no.castinglevel.dialog            |
        | Me invoke the spell Eldritch Blast                                    | choose.characterlevel.dialog          |
        | 1                                                                     | inflict.damage.dialog                 |

    Scenario Outline: invoke casting assistant with invalid spell
        Given an english speaking user
        When the user says "<invoke_casting_assistant_with_invalid_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "invalid.spell.error.dialog"

        Examples: invoke casting assistant with invalid spell
            | invoke_casting_assistant_with_invalid_spell   |
            | I cast the spell Climate Change               |
            | I conjure the spell Hatred                    |
            | We summon the spell Avocado                   |
        

    Scenario Outline: invoke casting assistant without spellname
        Given an english speaking user
        When the user says "<invoke_casting_assistant_without_spellname>"
        Then "spellcastmanager-skill" should reply with dialog from "invalid.spell.error.dialog"

        Examples: invoke casting assistant without spellname
            | invoke_casting_assistant_without_spellname    |
            | I cast the spell Climate Change               |
            | I conjure the spell Hatred                    |
            | We summon the spell Avocado                   |


