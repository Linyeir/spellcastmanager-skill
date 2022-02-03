Feature: spellcast manager invoke casting assistant

    Scenario Outline: invoke casting assistant with existing spell
        Given an english speaking user
         When the user says "<request_all_details_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "<get_all_details_dialogs>"

    Examples: invoke casting assistant existing spell            
        | request_all_details_with_existing_spell                               | get_all_details_dialogs               |
        | Give me the details to the spell fireball                             | get.all.details.category.4.dialog     |
        | Tell me all the details to the spell bless                            | get.all.details.category.15.dialog    |
        | Read me the details to the spell burning hands                        | get.all.details.category.4.dialog     |
        | Give me a detailed version of the spell confusion                     | get.all.details.category.12.dialog    |
        | Tell me the detailed version for the spell create or destroy water    | get.all.details.category.13.dialog    |
        | Read me the detailed version of the spell darkness                    | get.all.details.category.13.dialog    |
        | details for the spell guardian of faith                               | get.all.details.category.4.dialog     |
        | detailed version of the spell gust of wind                            | get.all.details.category.12.dialog    |
        | detailed version for the spell heal                                   | get.all.details.category.7.dialog     |

