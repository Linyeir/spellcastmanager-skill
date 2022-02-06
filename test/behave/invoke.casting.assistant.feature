Feature: spellcast manager invoke casting assistant

    Scenario Outline: invoke casting assistant with existing spell
        Given an english speaking user
         When the user says "<invoke_casting_assistance_for_specific_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "<get_all_details_dialogs>"

    Examples: invoke casting assistance for specific spell            
        | invoke_casting_assistance_for_specific_spell                          | get_all_details_dialogs               |
        | i cast the spell fireball                                             | choose.spellslot.dialog               |
        | i summon the spell shocking grasp                                     | choose.character.level.dialog         |
        | We conjure the spell call your mother                                 | invalid.spell.error.dialog            |
        | Me invoke the spell bless                                             | has.no.castinglevel.dialog            |
        | I invoke the spell                                                    | no.spell.specified.error.dialog       |
        | I cast the spell Counterspell                                         | has.no.castinglevel.dialog            |

