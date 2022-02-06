Feature: spellcast manager read all details

    Scenario Outline: request all details with existing spell
        Given an english speaking user
        When the user says "<request_all_details_with_existing_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "<get_all_details_dialogs>"

        Examples: request all details with existing spell
            | request_all_details_with_existing_spell                            | get_all_details_dialogs            |
            | Give me the details to the spell fireball                          | get.all.details.category.4.dialog  |
            | no                                                                 | alright.dialog                     |
            | Tell me all the details to the spell bless                         | get.all.details.category.15.dialog |
            | no                                                                 | alright.dialog                     |
            | Give me a detailed version of the spell confusion                  | get.all.details.category.12.dialog |
            | no                                                                 | alright.dialog                     |
            | Tell me the detailed version for the spell create or destroy water | get.all.details.category.13.dialog |
            | no                                                                 | alright.dialog                     |


    Scenario Outline: request all details with invalid spell
        Given an english speaking user
        When the user says "<request_all_details_with_invalid_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "invalid.spell.error.dialog"

        Examples: request all details with invalid spell
            | request_all_details_with_invalid_spell          |
            | Give me the details to the spell acid cloud     |
            | Tell me all the details to the spell arcane     |
            | Read me the details to the spell banish         |
            | Give me a detailed version of the spell fire    |
            | Tell me the detailed version for the spell kill |
            | Read me the detailed version of the spell hall  |
            | details for the spell help                      |
            | detailed version of the spell climate change    |
            | detailed version for the spell protection       |

    Scenario Outline: request all details without stating spell
        Given an english speaking user
        When the user says "<request_all_details_without_stating_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "no.spell.specified.error.dialog"

        Examples: request all details without stating spell
            | request_all_details_without_stating_spell  |
            | Give me the details to the spell           |
            | Tell me all the details to the spell       |
            | Read me the details to the spell           |
            | Give me a detailed version of the spell    |
            | Tell me the detailed version for the spell |
            | Read me the detailed version of the spell  |
            | details for the spell                      |
            | detailed version of the spell              |
            | detailed version for the spell             |
