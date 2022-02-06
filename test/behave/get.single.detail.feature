Feature: spellcast manager read single detail

    Scenario Outline: request singledetail with existing spell
        Given an english speaking user
        When the user says "<request_single_detail_with_existing_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "<get_single_detail_dialogs>"

        Examples: request single detail with existing spell
            | request_single_detail_with_existing_spell                             | get_single_detail_dialogs                 |
            | i want some information about the spell fireball                      | get.single.detail.request.detail.dialog   |
            | range                                                                 | get.single.detail.range.dialog            |
            | no                                                                    | alright.dialog                            |          
            | no                                                                    | alright.dialog                            |
            | i want infos for the spell bless                                      | get.single.detail.request.detail.dialog   |
            | name                                                                  | get.single.detail.name.dialog             |
            | no                                                                    | alright.dialog                            |          
            | no                                                                    | alright.dialog                            |
            | i would like some information about the spell eldritch blast          | get.single.detail.request.detail.dialog   |
            | school                                                                | get.single.detail.school.dialog           |
            | no                                                                    | alright.dialog                            |          
            | no                                                                    | alright.dialog                            |
            | i would like some info about the spell fire bolt                      | get.single.detail.request.detail.dialog   |
            | range                                                                 | get.single.detail.range.dialog            |
            | no                                                                    | alright.dialog                            |          
            | no                                                                    | alright.dialog                            |


    Scenario Outline: request single detail with invalid spell
        Given an english speaking user
        When the user says "<request_single_detail_with_invalid_spell>"
        Then "spellcastmanager-skill" should reply with dialog from "invalid.spell.error.dialog"

        Examples: request single detail with invalid spell
            | request_single_detail_with_invalid_spell              |
            | i want some information about the spell arcane        |
            | i want infos for the spell banish                     |
            | i would like some information about the spell fire    |
            | i would like some info about the spell avocado        |

    Scenario Outline: request single detail without spellname
        Given an english speaking user
        When the user says "<request_single_detail_without_spellname>"
        Then "spellcastmanager-skill" should reply with dialog from "no.spell.specified.error.dialog"

        Examples: request single detail without spellname
            | request_single_detail_without_spellname               |
            | i want some information about the spell               |
            | i want infos for the spell                            |
            | i would like some information about the spell         |
    
    