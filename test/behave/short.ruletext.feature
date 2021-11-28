Feature: spellcast manager read short ruletext

    Scenario Outline: request short ruletext with existing spell
        Given an english speaking user
         When the user says "<request_short_ruletext_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "short.ruletext.dialog"

    Examples: request short ruletext with existing spell            
        | request_short_ruletext_with_existing_spell                        |
        | Give me the details to the spell fireball                         |
        | Tell me the details to the spell bless                            |
        | Read me the details to the spell burning hands                    |
        | Give me a short version of the spell confusion                    |
        | Tell me the compact version of the spell create or destroy water  |
        | Read me the compact descripton of the spell darkness              |
        | Give me a short explanation of the spell detect evil and good     |
        | Give me the summary of the spell divine favor                     |
        | What does the spell eldritch blast do in short                    |
        | Explain the spell gate in short                                   |
        | details for the spell gentle repose                               |
        | short ruletext for the spell guardian of faith                    |
        | short version of the spell gust of wind                           |
        | short description of the spell heal                               |